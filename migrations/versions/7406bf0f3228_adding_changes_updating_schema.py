"""adding changes,updating schema

Revision ID: 7406bf0f3228
Revises: d14eb31d28e3
Create Date: 2023-01-16 21:33:56.489153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7406bf0f3228'
down_revision = 'd14eb31d28e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('public_id', sa.String(length=50), nullable=True))
        batch_op.create_unique_constraint(None, ['public_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('public_id')

    # ### end Alembic commands ###
