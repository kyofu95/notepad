"""
Module containing the TagRepository class for managing tag-related database operations.
"""

from notepad.models.tag import Tag as TagModel
from notepad.models.tag import TextTag as TextTagModel
from notepad.models.text import Text as TextModel

from .base import BaseRepository


class TagRepository(BaseRepository):
    """
    Extends the BaseRepository to manage tag-specific database operations.
    """

    async def create(self, text: TextModel, name: str) -> TagModel:
        """
        Creates a new tag and associates it with a given text entry.
        """

        tag = TagModel(name=name)

        texttag = TextTagModel()
        texttag.tag = tag
        texttag.text = text

        self.session.add_all((tag, texttag))
        await self.session.commit()
        await self.session.refresh(tag)

        return tag
