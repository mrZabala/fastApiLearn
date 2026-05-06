"""add soft delete to movies

Revision ID: 8d261b860641
Revises: 27783b18b5a4
Create Date: 2026-05-06 15:00:12.098486

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d261b860641'
down_revision: Union[str, Sequence[str], None] = '27783b18b5a4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
