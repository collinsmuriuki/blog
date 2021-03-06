"""Add subscribers table

Revision ID: 5adddf56cabc
Revises: 3ecd94d90897
Create Date: 2019-10-28 00:20:53.887930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5adddf56cabc'
down_revision = '3ecd94d90897'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscribers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscribers_email'), 'subscribers', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_subscribers_email'), table_name='subscribers')
    op.drop_table('subscribers')
    # ### end Alembic commands ###
