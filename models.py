from sqlalchemy import Column, Integer, String, JSON, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///features.db"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


class FeatureConfig(Base):
    __tablename__ = "feature_configs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    config = Column(JSON, nullable=False)


def init_db() -> None:
    """Create database tables."""
    Base.metadata.create_all(bind=engine)
