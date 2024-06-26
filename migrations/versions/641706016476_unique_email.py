"""unique email

Revision ID: 641706016476
Revises: 98c131f1a337
Create Date: 2024-06-30 18:47:10.221906

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '641706016476'
down_revision: Union[str, None] = '98c131f1a337'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint("ck_user_account_email", 'user_account', ['email'])
    op.create_unique_constraint("ck_user_account_name", 'user_account', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("ck_user_account_email", 'user_account', type_='unique')
    op.drop_constraint("ck_user_account_name", 'user_account', type_='unique')
    # ### end Alembic commands ###
