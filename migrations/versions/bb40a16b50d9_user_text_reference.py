"""user_text_reference

Revision ID: bb40a16b50d9
Revises: 9b6a1275c0f5
Create Date: 2024-06-19 16:08:40.043389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb40a16b50d9'
down_revision: Union[str, None] = '9b6a1275c0f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('text', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key("fk_user_texts", 'text', 'user_account', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("fk_user_texts", 'text', type_='foreignkey')
    op.drop_column('text', 'user_id')
    # ### end Alembic commands ###