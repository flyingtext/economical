"""Dataclasses representing core ERD entities.

These models are derived from the sitemap and ERD mapping
at ``docs/sitemap_erd.md`` to provide a lightweight
schema scaffold for future database integration.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional


@dataclass
class User:
    id: int
    name: str
    email: str
    affiliation: Optional[str] = None
    role: str = "user"
    preferences_json: Dict[str, object] = field(default_factory=dict)
    password_hash: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Team:
    id: int
    name: str
    description: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Dataset:
    id: int
    name: str
    description: str
    tags: List[str] = field(default_factory=list)
    visibility: str = "private"
    owner_id: int = 0
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class DatasetVersion:
    dataset_id: int
    origin: str
    version_tag: str
    changelog: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class DatasetUsage:
    dataset_id: int
    views: int = 0
    downloads: int = 0
    api_calls: int = 0
    last_accessed: Optional[datetime] = None


@dataclass
class Model:
    id: int
    name: str
    description: str
    model_type: str
    owner_id: int
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Project:
    id: int
    name: str
    description: str
    owner_id: int
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Dashboard:
    id: int
    name: str
    description: str
    owner_id: int
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class MapView:
    id: int
    name: str
    description: str
    layer_config: Dict[str, object] = field(default_factory=dict)


@dataclass
class Post:
    id: int
    content: str
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Comment:
    id: int
    post_id: int
    content: str
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Like:
    id: int
    post_id: int
    user_id: int
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Notification:
    id: int
    message: str
    type: str
    is_read: bool = False
    created_at: datetime = field(default_factory=datetime.utcnow)
