"""empty message

Revision ID: 4f953349e0d
Revises: 469f8388d38
Create Date: 2014-08-06 23:04:53.853892

"""

# revision identifiers, used by Alembic.
revision = '4f953349e0d'
down_revision = '469f8388d38'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('no_answer', sa.Boolean(), nullable=True))
    op.alter_column('event', 'sort_date',
               existing_type=sa.DATE(),
               nullable=False)
    op.add_column('korist', sa.Column('created', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('korist', 'created')
    op.alter_column('event', 'sort_date',
               existing_type=sa.DATE(),
               nullable=True)
    op.drop_column('event', 'no_answer')
    ### end Alembic commands ###