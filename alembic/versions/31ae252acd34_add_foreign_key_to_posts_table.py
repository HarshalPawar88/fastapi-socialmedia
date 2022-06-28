"""add foreign key to posts table

Revision ID: 31ae252acd34
Revises: 0109ebdebf42
Create Date: 2022-06-27 17:28:24.768839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31ae252acd34'
down_revision = '0109ebdebf42'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id',sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table='users',
                             local_cols=['owner_id'], remote_cols=['id'], ondelete= "CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
