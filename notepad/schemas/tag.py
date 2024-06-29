"""This module defines a Pydantic schema for a Tag scheme."""

from pydantic import BaseModel, ConfigDict


class TagBase(BaseModel):
    """Base pydantic scheme."""

    name: str


class Tag(TagBase):
    """Pydantic schema for a tag entity."""

    model_config = ConfigDict(from_attributes=True)


TagDB = Tag
