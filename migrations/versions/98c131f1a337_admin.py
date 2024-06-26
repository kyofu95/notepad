"""admin

Revision ID: 98c131f1a337
Revises: bb40a16b50d9
Create Date: 2024-06-27 21:46:14.436312

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "98c131f1a337"
down_revision: Union[str, None] = "bb40a16b50d9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "text",
        "last_update_date",
        existing_type=postgresql.TIMESTAMP(),
        nullable=False,
    )
    op.add_column(
        "user_account", sa.Column("is_admin", sa.Boolean(), nullable=False)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user_account", "is_admin")
    op.alter_column(
        "text",
        "last_update_date",
        existing_type=postgresql.TIMESTAMP(),
        nullable=True,
    )
    # ### end Alembic commands ###
