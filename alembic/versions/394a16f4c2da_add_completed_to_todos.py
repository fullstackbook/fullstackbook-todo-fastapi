"""add completed to todos

Revision ID: 394a16f4c2da
Revises: 049c5ab5051e
Create Date: 2022-07-29 21:58:58.112832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '394a16f4c2da'
down_revision = '049c5ab5051e'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("alter table todos add column completed boolean not null default false")


def downgrade():
    op.execute("alter table todos drop column completed")
