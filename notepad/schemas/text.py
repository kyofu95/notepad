"""This module defines a Pydantic schema for a Text scheme."""

from datetime import datetime

from pydantic import BaseModel

from .tag import Tag


class TextBase(BaseModel):
    """Base schema for a text entry."""

    content: str
    title: str


class Text(TextBase):
    """Pydantic schema for a text entity."""

    created_at: datetime
    last_update_date: datetime | None

    tags: list[Tag] = []


class TextDB(TextBase):
    """A pydantic schema tailored for database interactions."""

    id: int
    created_at: datetime
    last_update_date: datetime | None
    deleted: bool

    user: "User"
    tags: list[Tag] = []

    class Config:
        """Configuration settings for the TextDB schema when used with ORMs."""

        orm_mode = True
