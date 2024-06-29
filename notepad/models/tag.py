"""This module provides models for managing tags and their associations with text content."""

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel, int_primarykey

# Pylint: 'X' is not defined
if TYPE_CHECKING:
    from .text import Text


class Tag(BaseModel):
    """Represents a Tag entity in the database."""

    __tablename__ = "tag"

    id: Mapped[int_primarykey]
    name: Mapped[str]

    text_tag_associations: Mapped[list["TextTag"]] = relationship(
        back_populates="tag", lazy="selectin"
    )

    texts: AssociationProxy[list["Text"]] = association_proxy(
        "text_tag_associations",
        "text",
        creator=lambda text_obj: TextTag(text=text_obj),
    )


class TextTag(BaseModel):
    """Represents a mapping between a Tag and a Text entities."""

    __tablename__ = "texttag"

    id: Mapped[int_primarykey]
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"))
    text_id: Mapped[int] = mapped_column(ForeignKey("text.id"))

    tag: Mapped["Tag"] = relationship(
        back_populates="text_tag_associations", lazy="selectin"
    )
    text: Mapped["Text"] = relationship(
        back_populates="text_tag_associations", lazy="selectin"
    )
