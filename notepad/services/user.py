"""
Module containing the UserService class for orchestrating user-related business logic.
"""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from notepad.core.database import get_session
from notepad.repositories.user import UserRepository
from notepad.schemas.user import UserDB as UserDBScheme


class UserService:
    """
    Encapsulates the business logic for user operations, leveraging the UserRepository for data persistence.
    """

    def __init__(self, async_session: AsyncSession) -> None:
        self.repository = UserRepository(async_session)

    async def create(
        self, name: str, email: str, password: str
    ) -> UserDBScheme:
        """
        Creates a new user in the system and returns the user object.
        """

        user = await self.repository.create(name, email, password)
        return user

    @staticmethod
    def get_service(
        async_session: Annotated[AsyncSession, Depends(get_session)]
    ) -> UserService:
        """Static factory method for creating an instance of UserService for FastAPI dependency injection."""

        return UserService(async_session)
