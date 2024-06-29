"""This module defines a Pydantic schema for a Text scheme."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict

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

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    last_update_date: datetime | None
    deleted: bool

    user: "User"
    tags: list[Tag] = []
