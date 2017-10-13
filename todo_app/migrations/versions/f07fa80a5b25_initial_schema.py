"""initial schema

Revision ID: f07fa80a5b25
Revises: 
Create Date: 2017-10-13 17:40:32.808018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f07fa80a5b25'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_model')
    # ### end Alembic commands ###
