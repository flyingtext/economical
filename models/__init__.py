"""SQLAlchemy ORM models for core entities.

This module replaces earlier dataclass scaffolds with proper SQLAlchemy
models aligned with the ERD described in ``docs/ERD.md``.  Only a subset of
entities required by the application are implemented here.
"""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from .db import Base


def _uuid() -> str:
    """Return a new UUID4 string."""

    return str(uuid.uuid4())


class Dataset(Base):
    """Dataset information available in the catalog."""

    __tablename__ = "datasets"

    id = Column(String(36), primary_key=True, default=_uuid)
    name = Column(String(255), nullable=False)
    description = Column(String, nullable=False)
    tags = Column(String, default="")
    visibility = Column(String(50), default="private")
    owner_id = Column(String(36), nullable=False)
    owner_type = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    versions = relationship(
        "DatasetVersion", back_populates="dataset", cascade="all, delete-orphan"
    )
    usage = relationship(
        "DatasetUsage", back_populates="dataset", uselist=False, cascade="all, delete-orphan"
    )


class DatasetVersion(Base):
    """Version history for datasets."""

    __tablename__ = "dataset_versions"

    id = Column(String(36), primary_key=True, default=_uuid)
    dataset_id = Column(String(36), ForeignKey("datasets.id"), nullable=False)
    version_tag = Column(String(100), nullable=False)
    changelog = Column(String, default="")
    origin = Column(String, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

    dataset = relationship("Dataset", back_populates="versions")


class DatasetUsage(Base):
    """Usage statistics for datasets."""

    __tablename__ = "dataset_usage"

    id = Column(String(36), primary_key=True, default=_uuid)
    dataset_id = Column(String(36), ForeignKey("datasets.id"), nullable=False)
    views = Column(Integer, default=0)
    downloads = Column(Integer, default=0)
    api_calls = Column(Integer, default=0)
    last_accessed = Column(DateTime)

    dataset = relationship("Dataset", back_populates="usage")


class Model(Base):
    """Machine learning or analytical model metadata."""

    __tablename__ = "models"

    id = Column(String(36), primary_key=True, default=_uuid)
    name = Column(String(255), nullable=False)
    description = Column(String, nullable=False)
    model_type = Column(String(50), nullable=False)
    visibility = Column(String(50), default="private")
    owner_id = Column(String(36), nullable=False)
    owner_type = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Notification(Base):
    """User notification records."""

    __tablename__ = "notifications"

    id = Column(String(36), primary_key=True, default=_uuid)
    user_id = Column(String(36), nullable=False)
    message = Column(String, nullable=False)
    type = Column(String(50), nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)


__all__ = [
    "Dataset",
    "DatasetVersion",
    "DatasetUsage",
    "Model",
    "Notification",
]
