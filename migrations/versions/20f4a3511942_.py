"""empty message

Revision ID: 20f4a3511942
Revises: 38d7053dd9ff
Create Date: 2022-08-17 17:47:08.497255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20f4a3511942'
down_revision = '38d7053dd9ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_no', sa.Integer(), nullable=True))
        batch_op.drop_column('registration_no')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('registration_no', sa.INTEGER(), nullable=True))
        batch_op.drop_column('employee_no')

    # ### end Alembic commands ###
