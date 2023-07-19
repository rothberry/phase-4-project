"""added to Property model

Revision ID: f8f4128c7b35
Revises: be550894b88c
Create Date: 2023-07-18 11:44:49.680206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8f4128c7b35'
down_revision = 'be550894b88c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bedrooms', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('bathrooms', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('floors', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('garage', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('pool', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.drop_column('pool')
        batch_op.drop_column('garage')
        batch_op.drop_column('floors')
        batch_op.drop_column('bathrooms')
        batch_op.drop_column('bedrooms')

    # ### end Alembic commands ###