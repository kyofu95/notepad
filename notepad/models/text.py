"""This module provides text model for content management within the application."""

from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import BaseModel, int_primarykey


class Text(BaseModel):
    """Represents a text entity in the database."""

    __tablename__ = "text"

    id: Mapped[int_primarykey]
    content: Mapped[str]
    title: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    last_update_date: Mapped[datetime]
    deleted: Mapped[bool] = mapped_column(default=False)

    texttags: Mapped[list["TextTag"]] = relationship(back_populates="text", lazy="selectin")
