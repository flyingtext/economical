from flask import Blueprint, jsonify

bp = Blueprint("api_datasets", __name__, url_prefix="/api/datasets")

DATASETS = [
    {"id": 1, "name": "Dataset 1", "description": "First dataset"},
    {"id": 2, "name": "Dataset 2", "description": "Second dataset"},
]


@bp.get("/")
def list_datasets():
    """Return all datasets."""
    return jsonify(DATASETS)


@bp.get("/<int:dataset_id>")
def dataset_detail(dataset_id: int):
    """Return details for a single dataset."""
    dataset = next((d for d in DATASETS if d["id"] == dataset_id), None)
    if dataset is None:
        return jsonify({"error": "Dataset not found"}), 404
    return jsonify(dataset)
