"""
Module containing the TextRepository class for managing text-related database operations.
"""

from sqlalchemy import select

from notepad.models.text import Text as TextModel
from notepad.models.user import User as UserModel

from .base import BaseRepository


class TextRepository(BaseRepository):
    """Extends the BaseRepository to manage text-specific database operations."""

    async def create(
        self, user: UserModel, content: str, title: str
    ) -> TextModel:
        """Creates a new text entry in the database associated with a user and returns the text object."""

        text = TextModel(content=content, title=title)

        text.user = user

        self.session.add(text)
        await self.session.commit()
        await self.session.refresh(text)

        return text

    async def get_last_n(self, count: int = 5) -> list[TextModel]:
        """
        Retrieves the last N text entries from the database, ordered by their update date in descending order.
        """

        results = await self.session.execute(
            select(TextModel)
            .order_by(TextModel.last_update_date.desc())
            .limit(count)
        )
        return results.scalars().all()
