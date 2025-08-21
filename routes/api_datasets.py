from flask import Blueprint, jsonify

from models import Dataset
from models.db import SessionLocal

bp = Blueprint("api_datasets", __name__, url_prefix="/api/datasets")


@bp.get("/")
def list_datasets():
    """Return all datasets stored in the database."""
    with SessionLocal() as session:
        datasets = session.query(Dataset).all()
        return jsonify(
            [
                {
                    "id": d.id,
                    "name": d.name,
                    "description": d.description,
                }
                for d in datasets
            ]
        )


@bp.get("/<string:dataset_id>")
def dataset_detail(dataset_id: str):
    """Return details for a single dataset."""
    with SessionLocal() as session:
        dataset = session.get(Dataset, dataset_id)
        if dataset is None:
            return jsonify({"error": "Dataset not found"}), 404
        return jsonify({"id": dataset.id, "name": dataset.name, "description": dataset.description})
