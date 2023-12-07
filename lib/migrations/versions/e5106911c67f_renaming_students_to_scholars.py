"""Renaming students to scholars

Revision ID: e5106911c67f
Revises: 791279dd0760
Create Date: 2023-12-07 20:16:32.330747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5106911c67f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
