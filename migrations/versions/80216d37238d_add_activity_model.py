"""Add Activity model

Revision ID: 80216d37238d
Revises: 
Create Date: 2024-11-05 20:47:56.010622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80216d37238d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('intensity', sa.String(length=50), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('activities')
    # ### end Alembic commands ###
