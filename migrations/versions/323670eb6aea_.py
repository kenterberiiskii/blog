"""empty message

Revision ID: 323670eb6aea
Revises: dc568ccd1a77
Create Date: 2023-03-23 14:21:30.868112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '323670eb6aea'
down_revision = 'dc568ccd1a77'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(length=120), server_default='', nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(length=120), server_default='', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    # ### end Alembic commands ###
