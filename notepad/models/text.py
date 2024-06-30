"""This module provides text model for content management within the application."""

from datetime import datetime
from typing import TYPE_CHECKING, Callable

from sqlalchemy import ForeignKey, func
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel, int_primarykey
from .tag import TextTag

# Pylint: func.now is not callable
if TYPE_CHECKING:
    func: Callable
    from .tag import Tag
    from .user import User


class Text(BaseModel):
    """Represents a text entity in the database."""

    __tablename__ = "text"

    id: Mapped[int_primarykey]
    content: Mapped[str]
    title: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    last_update_date: Mapped[datetime] = mapped_column(default=func.now())
    deleted: Mapped[bool] = mapped_column(default=False)

    user: Mapped["User"] = relationship(back_populates="texts", lazy="selectin")

    text_tag_associations: Mapped[list["TextTag"]] = relationship(
        back_populates="text", lazy="selectin"
    )

    tags: AssociationProxy[list["Tag"]] = association_proxy(
        "text_tag_associations",
        "tag",
        creator=lambda tag_obj: TextTag(tag=tag_obj),
    )
