"""This module defines the user model, encompassing user details and activity tracking."""

from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel, int_primarykey


class User(BaseModel):
    """Represents a user account in the system, storing personal information and activity logs."""

    __tablename__ = "user_account"

    id: Mapped[int_primarykey]
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    last_login_date: Mapped[datetime]
    last_update_date: Mapped[datetime]
    active: Mapped[bool] = mapped_column(default=True)
