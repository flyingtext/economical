"""create user tables"""

from alembic import op
import sqlalchemy as sa

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False, unique=True),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("contact", sa.String(length=255)),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
    )
    op.create_table(
        "password_reset_tokens",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("token", sa.String(length=255), nullable=False, unique=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
    )
    op.create_table(
        "active_sessions",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("token", sa.String(length=255), nullable=False, unique=True),
        sa.Column("ip", sa.String(length=45)),
        sa.Column("login_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("active_sessions")
    op.drop_table("password_reset_tokens")
    op.drop_table("users")
