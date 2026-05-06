"""add soft delete to movies

Revision ID: a8cab6b41aff
Revises: 8d261b860641
Create Date: 2026-05-06 15:11:12.874552

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8cab6b41aff'
down_revision: Union[str, Sequence[str], None] = '8d261b860641'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
