"""rename plots to plot

Revision ID: fbf8f97ddb9c
Revises: e8d5e2398e5a
Create Date: 2026-05-06 15:17:37.802805

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fbf8f97ddb9c'
down_revision: Union[str, Sequence[str], None] = 'e8d5e2398e5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
