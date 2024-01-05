"""Rename

Revision ID: 142f48ba6764
Revises: d256eb7ffc10
Create Date: 2023-12-03 18:39:12.838241

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '142f48ba6764'
down_revision: Union[str, None] = 'd256eb7ffc10'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hased_password', sa.String(), nullable=False))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('users', 'hased_password')
    # ### end Alembic commands ###