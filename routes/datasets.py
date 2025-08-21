"""Dataset catalog and detail views."""

from flask import Blueprint, render_template

bp = Blueprint("datasets", __name__, url_prefix="/datasets")


@bp.get("/")
def catalog():
    """List available datasets."""
    return render_template("datasets/catalog.html")


@bp.get("/<int:dataset_id>")
def detail(dataset_id: int):
    """Show dataset details."""
    return render_template("datasets/detail.html", dataset_id=dataset_id)
