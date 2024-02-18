"""added unique on title

Revision ID: 59a63d85643e
Revises: cceb4c7f600b
Create Date: 2023-06-06 16:53:58.569552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59a63d85643e'
down_revision = 'cceb4c7f600b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notes', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['title'])
        batch_op.drop_column('published')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('published', sa.BOOLEAN(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
