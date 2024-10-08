"""add showing property to vehicle

Revision ID: 83b55418c62f
Revises: a92031241698
Create Date: 2024-08-31 19:24:36.710759

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '83b55418c62f'
down_revision: Union[str, None] = 'a92031241698'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vehicles', sa.Column('showing', sa.Boolean(), nullable=False,server_default=sa.sql.expression.false()))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vehicles', 'showing')
    # ### end Alembic commands ###
