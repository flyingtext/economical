"""add visibility column to models"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0003"
down_revision = "0002"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "models",
        sa.Column(
            "visibility",
            sa.String(length=50),
            nullable=False,
            server_default="private",
        ),
    )


def downgrade() -> None:
    op.drop_column("models", "visibility")

