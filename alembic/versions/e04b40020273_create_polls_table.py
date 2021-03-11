"""create_polls_table

Revision ID: e04b40020273
Revises: 7d03c23b529b
Create Date: 2021-03-02 09:11:32.058237

"""
import enum
from alembic import op
import sqlalchemy as sa

pg = sa.dialects.postgresql

class PollType(enum.Enum):
    text = 1
    image = 2


# revision identifiers, used by Alembic.
revision = 'e04b40020273'
down_revision = '7d03c23b529b'
branch_labels = None
depends_on = None


def upgrade():
    # create_type=False
    op.create_table(
        'polls',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('type', pg.ENUM(PollType, create_type=False), nullable=False),
        sa.Column('is_add_choices_active', sa.Boolean, nullable=False),
        sa.Column('is_voting_active', sa.Boolean, nullable=False),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
    )


def downgrade():
    op.drop_table('polls')
