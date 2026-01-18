"""remove items column from orders

Revision ID: a2e7340baa75
Revises: 4b0a899ea3d7
Create Date: 2026-01-17 22:05:46.029086

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2e7340baa75'
down_revision: Union[str, Sequence[str], None] = '4b0a899ea3d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
