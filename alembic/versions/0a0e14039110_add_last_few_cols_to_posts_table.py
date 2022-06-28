"""add last few cols to posts table

Revision ID: 0a0e14039110
Revises: 31ae252acd34
Create Date: 2022-06-27 17:35:45.093840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a0e14039110'
down_revision = '31ae252acd34'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default= 'True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                         nullable=False, server_default= sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created')
    pass
