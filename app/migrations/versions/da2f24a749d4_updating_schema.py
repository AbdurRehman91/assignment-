"""updating schema

Revision ID: da2f24a749d4
Revises: 7406bf0f3228
Create Date: 2023-01-17 19:37:46.080386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da2f24a749d4'
down_revision = '7406bf0f3228'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('listing', schema=None) as batch_op:
        batch_op.alter_column('user',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('listing', schema=None) as batch_op:
        batch_op.alter_column('user',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
