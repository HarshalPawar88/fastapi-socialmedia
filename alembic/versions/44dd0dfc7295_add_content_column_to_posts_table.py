"""add content column to posts table

Revision ID: 44dd0dfc7295
Revises: 6b1f4a2c6224
Create Date: 2022-06-27 17:23:37.224505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44dd0dfc7295'
down_revision = '6b1f4a2c6224'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
