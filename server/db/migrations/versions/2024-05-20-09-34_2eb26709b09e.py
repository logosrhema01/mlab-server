"""empty message

Revision ID: 2eb26709b09e
Revises: 1e6d68941d37
Create Date: 2024-05-20 09:34:08.238535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2eb26709b09e'
down_revision = '1e6d68941d37'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_key_pairs', 'public_key',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=20000),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_key_pairs', 'public_key',
               existing_type=sa.String(length=20000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=False)
    # ### end Alembic commands ###
