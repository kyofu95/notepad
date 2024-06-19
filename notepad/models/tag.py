"""This module provides models for managing tags and their associations with text content."""

from sqlalchemy import ForeignKey
from sqlalchemy.ext.associationproxy import association_proxy, AssociationProxy
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel, int_primarykey


class Tag(BaseModel):
    """Represents a Tag entity in the database."""

    __tablename__ = "tag"

    id: Mapped[int_primarykey]
    name: Mapped[str]

    # texttags: Mapped[list["TextTag"]] = relationship(back_populates="tag", lazy="selectin")

    text_tag_associations: Mapped[list["TextTag"]] = relationship(back_populates="tag", lazy="selectin")

    texts: AssociationProxy[list["Text"]] = association_proxy(
        "text_tag_associations", "text", creator=lambda text_obj: TextTag(text=text_obj)
    )


class TextTag(BaseModel):
    """Represents a mapping between a Tag and a Text entities."""

    __tablename__ = "texttag"

    id: Mapped[int_primarykey]
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"))
    text_id: Mapped[int] = mapped_column(ForeignKey("text.id"))

    # tag: Mapped["Tag"] = relationship(back_populates="texttags", lazy="selectin")
    tag: Mapped["Tag"] = relationship(back_populates="text_tag_associations", lazy="selectin")
    text: Mapped["Text"] = relationship(back_populates="text_tag_associations", lazy="selectin")
