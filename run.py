#!/usr/bin/env python3
"""Universal dev entrypoint for Flask or FastAPI apps.

Usage examples:
    python run.py
    python run.py --host 0.0.0.0 --port 8000
    python run.py --reload
    python run.py --app mypkg.web:app
    python run.py --app mypkg.web:create_app --factory

Why this file exists:
- New contributors can start the server without knowing the internal layout.
- Works for both Flask (WSGI) and ASGI apps (FastAPI/Starlette) with uvicorn.
"""
from __future__ import annotations

import argparse
import importlib
import inspect
import os
import sys
from types import ModuleType
from typing import Any, Optional, Tuple


def _maybe_load_dotenv(env_file: Optional[str]) -> None:
    """Load .env if python-dotenv is available.
    Only explain *why* we skip when the package is missing.
    """
    try:
        from dotenv import load_dotenv  # type: ignore
    except Exception:
        # Skipped on purpose: keep runtime deps minimal for users who don't need .env
        return

    if env_file:
        load_dotenv(env_file, override=False)
    else:
        load_dotenv(override=False)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Economical dev server")
    parser.add_argument(
        "--host",
        default=os.getenv("HOST", "127.0.0.1"),
        help="Bind host (default: env HOST or 127.0.0.1)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.getenv("PORT", "5000")),
        help="Bind port (default: env PORT or 5000)",
    )
    parser.add_argument(
        "--reload",
        action="store_true" if os.getenv("RELOAD") is None else (os.getenv("RELOAD", "0") == "1"),
        help="Enable auto-reload (default: env RELOAD==1 or flag)",
    )
    parser.add_argument(
        "--app",
        default=os.getenv("APP", "app:app"),
        help=(
            "Target app in 'module:attr' or 'module' form. "
            "Tried in order: attr then 'create_app'. Default: app:app"
        ),
    )
    parser.add_argument(
        "--factory",
        action="store_true",
        help="Force using a create_app() factory if available",
    )
    parser.add_argument(
        "--env-file",
        default=os.getenv("ENV_FILE"),
        help="Optional path to .env file",
    )
    return parser.parse_args()


def _import_module(dotted: str) -> ModuleType:
    try:
        return importlib.import_module(dotted)
    except Exception as exc:
        raise SystemExit(f"✖ Failed to import module '{dotted}': {exc}")


def _load_attr(mod: ModuleType, attr: str) -> Any:
    try:
        return getattr(mod, attr)
    except AttributeError:
        raise SystemExit(
            f"✖ Attribute '{attr}' not found in module '{mod.__name__}'. "
            f"Provide a valid --app value like 'pkg.module:app' or ':create_app'."
        )


def _resolve_app(target: str, force_factory: bool) -> Tuple[Any, bool]:
    """Return (app_instance_or_callable, is_factory_used)."""
    if ":" in target:
        mod_name, attr = target.split(":", 1)
    else:
        mod_name, attr = target, "app"

    mod = _import_module(mod_name)

    if force_factory:
        factory = _load_attr(mod, attr if attr else "create_app")
        if not callable(factory):
            raise SystemExit("✖ --factory requires a callable like create_app().")
        return factory(), True

    # Prefer concrete instance 'app' if present
    obj: Optional[Any] = None
    if attr:
        obj = getattr(mod, attr, None)
    if obj is None:
        obj = getattr(mod, "create_app", None)
        if callable(obj):
            return obj(), True
        raise SystemExit(
            "✖ Could not find 'app' or 'create_app' in the target module.\n"
            "  Try --app yourpkg.module:create_app --factory"
        )

    # If attribute is a factory, call it
    if callable(obj) and _looks_like_factory(obj):
        return obj(), True

    return obj, False


def _looks_like_factory(obj: Any) -> bool:
    try:
        sig = inspect.signature(obj)
    except (TypeError, ValueError):
        return False
    return callable(obj) and len(sig.parameters) == 0


def _is_flask_app(obj: Any) -> bool:
    # Avoid hard dependency on Flask; rely on shape
    return hasattr(obj, "run") and hasattr(obj, "jinja_env")


def _run_flask(app: Any, host: str, port: int, reload_: bool) -> None:
    # Debug implies reloader; keep behavior consistent with Flask defaults
    app.run(host=host, port=port, debug=reload_, use_reloader=reload_)


def _run_asgi(app: Any, host: str, port: int, reload_: bool) -> None:
    try:
        import uvicorn  # type: ignore
    except Exception as exc:
        raise SystemExit(
            "✖ ASGI app detected but 'uvicorn' is not installed.\n"
            "  pip install uvicorn  # or add to requirements-dev.txt\n"
            f"  (original import error: {exc})"
        )
    uvicorn.run(app, host=host, port=port, reload=reload_, log_level="info")


def main() -> None:
    args = _parse_args()
    _maybe_load_dotenv(args.env_file)

    host = str(args.host)
    try:
        port = int(args.port)
    except Exception as exc:
        raise SystemExit(f"✖ Invalid --port value: {exc}")

    app, used_factory = _resolve_app(args.app, args.factory)

    print(
        (
            "▶ Starting dev server for '%s' (factory=%s) on %s:%d, reload=%s"
        )
        % (args.app, used_factory, host, port, bool(args.reload))
    )

    if _is_flask_app(app):
        _run_flask(app, host, port, bool(args.reload))
    else:
        # Treat everything else as ASGI
        _run_asgi(app, host, port, bool(args.reload))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⏹ Stopped by user")
        sys.exit(0)
