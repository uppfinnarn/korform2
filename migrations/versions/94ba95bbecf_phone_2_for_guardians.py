"""Phone 2 for guardians

Revision ID: 94ba95bbecf
Revises: 13466a1627a5
Create Date: 2015-07-12 15:08:00.985062

"""

# revision identifiers, used by Alembic.
revision = '94ba95bbecf'
down_revision = '13466a1627a5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('guardian', sa.Column('phone2', sa.String(length=15), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('guardian', 'phone2')
    ### end Alembic commands ###
