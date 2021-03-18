"""add author_id to TagModel

Revision ID: 54c5cfda6874
Revises: eb561f735473
Create Date: 2021-03-18 09:42:13.269229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54c5cfda6874'
down_revision = 'eb561f735473'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('user_model', 'user_model', ['author_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('author_id')

    # ### end Alembic commands ###
