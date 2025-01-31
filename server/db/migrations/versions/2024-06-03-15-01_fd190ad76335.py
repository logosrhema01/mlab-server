"""empty message

Revision ID: fd190ad76335
Revises:
Create Date: 2024-06-03 15:01:30.639662

"""
from alembic import op
import sqlalchemy as sa
import ormar


# revision identifiers, used by Alembic.
revision = 'fd190ad76335'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('datasets',
    sa.Column('id', ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('git_name', sa.String(length=200), nullable=False),
    sa.Column('clone_url', sa.String(length=300), nullable=False),
    sa.Column('private', sa.Boolean(), nullable=True),
    sa.Column('owner_id', sa.String(length=200), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('jobs',
    sa.Column('id', ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('model_id', ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
    sa.Column('model_name', sa.String(length=200), nullable=False),
    sa.Column('owner_id', sa.String(length=100), nullable=False),
    sa.Column('parameters', sa.JSON(none_as_null=True), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ml_models',
    sa.Column('id', ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('version', sa.String(length=200), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('git_name', sa.String(length=200), nullable=False),
    sa.Column('clone_url', sa.String(length=300), nullable=False),
    sa.Column('owner_id', sa.String(length=200), nullable=False),
    sa.Column('parameters', sa.JSON(none_as_null=True), nullable=True),
    sa.Column('private', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_key_pairs',
    sa.Column('id', ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
    sa.Column('user_id', sa.String(length=200), nullable=False),
    sa.Column('public_key', sa.String(length=20000), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('results',
    sa.Column('id', ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
    sa.Column('owner_id', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('result_type', sa.String(length=7), nullable=False),
    sa.Column('job', ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=True),
    sa.Column('dataset_id', ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
    sa.Column('status', sa.String(length=300), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('metrics', sa.JSON(none_as_null=True), nullable=True),
    sa.Column('files', sa.JSON(none_as_null=True), nullable=True),
    sa.Column('parameters', sa.JSON(none_as_null=True), nullable=True),
    sa.Column('pretrained_model', sa.String(length=300), nullable=True),
    sa.Column('predictions', sa.JSON(none_as_null=True), nullable=True),
    sa.ForeignKeyConstraint(['job'], ['jobs.id'], name='fk_results_jobs_id_job'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    op.drop_table('user_key_pairs')
    op.drop_table('ml_models')
    op.drop_table('jobs')
    op.drop_table('datasets')
    # ### end Alembic commands ###
