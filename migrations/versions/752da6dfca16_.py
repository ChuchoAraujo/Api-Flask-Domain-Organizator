"""empty message

Revision ID: 752da6dfca16
Revises: a0cbc0e00c49
Create Date: 2023-04-06 17:52:51.069271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '752da6dfca16'
down_revision = 'a0cbc0e00c49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('message', sa.String(length=180), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
