"""artists table

Revision ID: 607e1b8ca5b3
Revises: 1700f2965c6c
Create Date: 2021-11-09 15:26:48.403120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '607e1b8ca5b3'
down_revision = '1700f2965c6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('artist')
    # ### end Alembic commands ###