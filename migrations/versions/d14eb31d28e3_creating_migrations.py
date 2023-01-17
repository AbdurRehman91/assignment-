"""creating migrations

Revision ID: d14eb31d28e3
Revises: 
Create Date: 2023-01-16 21:19:01.792092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd14eb31d28e3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('listing', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user', sa.Integer(), nullable=False))
        batch_op.drop_constraint('listing_restaurant_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['user'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('restaurant')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('listing', schema=None) as batch_op:
        batch_op.add_column(sa.Column('restaurant', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('listing_restaurant_fkey', 'user', ['restaurant'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('user')

    # ### end Alembic commands ###
