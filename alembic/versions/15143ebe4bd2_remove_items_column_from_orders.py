"""remove items column from orders

Revision ID: 15143ebe4bd2
Revises: 9d240085e59b
Create Date: 2026-01-17 19:39:46.605978

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '15143ebe4bd2'
down_revision: Union[str, Sequence[str], None] = '9d240085e59b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
