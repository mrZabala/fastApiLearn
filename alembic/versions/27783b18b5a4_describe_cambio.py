"""describe cambio

Revision ID: 27783b18b5a4
Revises: aa85b1c168b7
Create Date: 2026-04-29 16:42:08.443578

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '27783b18b5a4'
down_revision: Union[str, Sequence[str], None] = 'aa85b1c168b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
