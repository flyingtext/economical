from pathlib import Path

from flask import Blueprint, render_template, abort

bp = Blueprint("docs", __name__, url_prefix="/docs")


@bp.get("/specification/<path:page>")
def specification(page: str):
    """Serve markdown files from docs/specification as simple pages."""
    md_path = Path("docs/specification") / f"{page}.md"
    if not md_path.exists():
        abort(404)
    content = md_path.read_text(encoding="utf-8")
    return render_template("docs/markdown.html", content=content)
