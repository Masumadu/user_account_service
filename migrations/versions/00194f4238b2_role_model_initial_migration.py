"""role_model_initial_migration

Revision ID: 00194f4238b2
Revises: 6910b7845d2c
Create Date: 2023-06-11 14:27:36.941685

"""
import sqlalchemy as sa
from alembic import op

import app

# revision identifiers, used by Alembic.
revision = "00194f4238b2"
down_revision = "6910b7845d2c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "roles",
        sa.Column("id", app.utils.guid.GUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("created_by", app.utils.guid.GUID(), nullable=False),
        sa.Column("updated_by", app.utils.guid.GUID(), nullable=False),
        sa.Column("deleted_by", app.utils.guid.GUID(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("roles")
    # ### end Alembic commands ###