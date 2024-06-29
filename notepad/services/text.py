"""
Module containing the TextService class for orchestrating text-related business logic.
"""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from notepad.core.database import get_session
from notepad.models.user import User as UserModel
from notepad.repositories.text import TextRepository
from notepad.schemas.text import TextDB as TextDBSchema
from notepad.schemas.user import User as UserSchema


class TextService:
    """
    Encapsulates the business logic for text operations, leveraging the TextRepository for data persistence.
    """

    def __init__(self, async_session: AsyncSession) -> None:
        self.repository = TextRepository(async_session)

    async def create(
        self, user: UserSchema, content: str, title: str
    ) -> TextDBSchema:
        """
        Creates a new text entry associated with a user and returns the text object.
        """

        # shut up, mypy
        user_model = UserModel(**user.model_dump())
        text = await self.repository.create(user_model, content, title)
        return text

    @staticmethod
    def get_service(
        async_session: Annotated[AsyncSession, Depends(get_session)]
    ) -> TextService:
        """Static factory method for creating an instance of TextService for FastAPI dependency injection."""

        return TextService(async_session)
