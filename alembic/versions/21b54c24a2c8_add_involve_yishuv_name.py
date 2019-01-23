"""add involve_yishuv_name

Revision ID: 21b54c24a2c8
Revises: 1c7c31b1c31d
Create Date: 2018-09-30 13:12:36.146666

"""

# revision identifiers, used by Alembic.
revision = '21b54c24a2c8'
down_revision = '1c7c31b1c31d'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('involved', sa.Column('involve_yishuv_name', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('involved', 'involve_yishuv_name')
    ### end Alembic commands ###