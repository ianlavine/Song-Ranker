"""album covers

Revision ID: d61a628aac84
Revises: 9fe193810951
Create Date: 2021-11-18 20:38:22.185099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd61a628aac84'
down_revision = '9fe193810951'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('album', sa.Column('cover', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('album', 'cover')
    # ### end Alembic commands ###
