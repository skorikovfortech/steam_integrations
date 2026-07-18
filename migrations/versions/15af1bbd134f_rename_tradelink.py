"""rename tradelink

Revision ID: 15af1bbd134f
Revises: 59d78d2c5404
Create Date: 2026-07-16 17:28:28.955327

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '15af1bbd134f'
down_revision: Union[str, Sequence[str], None] = '59d78d2c5404'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_constraint(op.f('user_trade_ling_key'), 'user', type_='unique')
    op.alter_column('user', 'trade_ling', new_column_name='trade_link')
    op.create_unique_constraint('user_trade_link_key', 'user', ['trade_link'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('user_trade_link_key', 'user', type_='unique')
    op.alter_column('user', 'trade_link', new_column_name='trade_ling')
    op.create_unique_constraint(op.f('user_trade_ling_key'), 'user', ['trade_ling'], postgresql_nulls_not_distinct=False)
