"""
Module containing the TagService class for orchestrating tag-related business logic.
"""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from notepad.core.database import get_session
from notepad.repositories.tag import TagRepository
from notepad.schemas.tag import Tag as TagScheme
from notepad.schemas.text import Text as TextScheme

from notepad.models.text import Text as TextModel

class TagService:
    """
    Encapsulates the business logic for tag operations, leveraging the TagRepository for data persistence.
    """

    def __init__(self, async_session: AsyncSession) -> None:
        self.repository = TagRepository(async_session)

    async def create(self, text: TextScheme, name: str) -> TagScheme:
        """
        Creates a new tag associated with a given text entry and returns the tag object.
        """

        text_model = TextModel(**text.model_dump())
        tag = await self.repository.create(text_model, name)
        return TagScheme.model_validate(tag, from_attributes=True)

    @staticmethod
    def get_service(
        async_session: Annotated[AsyncSession, Depends(get_session)]
    ) -> TagService:
        """Static factory method for creating an instance of TagService for FastAPI dependency injection."""

        return TagService(async_session)
