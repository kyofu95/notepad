"""This module defines a Pydantic schema for a Tag scheme."""

from pydantic import BaseModel


class TagBase(BaseModel):
    """Base pydantic scheme."""

    name: str


class Tag(TagBase):
    """Pydantic schema for a tag entity."""

    class Config:
        """Configuration settings for the Tag schema when used with ORMs."""

        orm_mode = True


TagDB = Tag
