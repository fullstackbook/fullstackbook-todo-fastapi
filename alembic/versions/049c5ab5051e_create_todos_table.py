"""create todos table

Revision ID: 049c5ab5051e
Revises: 
Create Date: 2022-07-27 16:52:56.499567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '049c5ab5051e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "todos",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String),
        sa.Column("completed", sa.Boolean)
    )


def downgrade():
    op.drop_table("todos")
