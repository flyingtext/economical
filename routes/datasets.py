"""Dataset catalog and detail views."""

from flask import Blueprint, render_template
from ws import emit_dataset_update

bp = Blueprint("datasets", __name__, url_prefix="/datasets")


@bp.get("/")
def catalog():
    """List available datasets."""
    return render_template("datasets/catalog.html")


@bp.get("/<int:dataset_id>")
def detail(dataset_id: int):
    """Show dataset details."""
    emit_dataset_update(dataset_id, {"message": f"dataset {dataset_id} viewed"})
    return render_template("datasets/detail.html", dataset_id=dataset_id)
