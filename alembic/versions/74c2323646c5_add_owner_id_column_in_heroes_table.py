"""Add owner_id column in heroes table

Revision ID: 74c2323646c5
Revises: 
Create Date: 2025-04-30 10:46:07.248442

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74c2323646c5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("heroes", sa.Column("owner_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        "fk_heroes_owner_id_players", #name of constraint
        "heroes", # source table
        "players", # target table
        ["owner_id"], # source col
        ["id"] # target col
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("fk_heroes_owner_id_players", "heroes", type_="foreignkey")
    op.drop_column("heroes", "owner_id")
