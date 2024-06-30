"""This module defines the user model, encompassing user details and activity tracking."""

from datetime import datetime
from typing import TYPE_CHECKING, Callable, Optional

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel, int_primarykey
from .text import Text

# Pylint: func.now is not callable
if TYPE_CHECKING:
    func: Callable


class User(BaseModel):
    """Represents a user account in the system, storing personal information and activity logs."""

    __tablename__ = "user_account"

    id: Mapped[int_primarykey]
    name: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    last_login_date: Mapped[Optional[datetime]]
    last_update_date: Mapped[Optional[datetime]]
    active: Mapped[bool] = mapped_column(default=True)
    is_admin: Mapped[bool] = mapped_column(default=False)

    texts: Mapped[list[Text]] = relationship(
        back_populates="user", lazy="selectin"
    )
