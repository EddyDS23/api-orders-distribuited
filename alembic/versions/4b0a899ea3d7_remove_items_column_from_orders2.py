"""remove items column from orders2

Revision ID: 4b0a899ea3d7
Revises: 15143ebe4bd2
Create Date: 2026-01-17 19:41:31.686475

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b0a899ea3d7'
down_revision: Union[str, Sequence[str], None] = '15143ebe4bd2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
