"""empty message

Revision ID: e1b15953b9c5
Revises: b4b9bb8934a9
Create Date: 2024-06-17 15:26:08.670371

"""
from alembic import op
import sqlalchemy as sa
import ormar


# revision identifiers, used by Alembic.
revision = 'e1b15953b9c5'
down_revision = 'b4b9bb8934a9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ml_models', sa.Column('default_model', sa.String(length=200), nullable=True))
    op.add_column('results', sa.Column('dataset_path', ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=True))
    op.alter_column('results', 'dataset_id',
               existing_type=sa.CHAR(length=32),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('results', 'dataset_id',
               existing_type=sa.CHAR(length=32),
               nullable=False)
    op.drop_column('results', 'dataset_path')
    op.drop_column('ml_models', 'default_model')
    # ### end Alembic commands ###
