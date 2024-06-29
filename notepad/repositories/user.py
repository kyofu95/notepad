"""
Module containing the UserRepository class for managing user-related database operations.
"""

from sqlalchemy import select

from notepad.models.user import User as UserModel

from .base import BaseRepository


class UserRepository(BaseRepository):
    """
    Extends the BaseRepository to manage user-specific database operations.
    """

    async def create(self, name: str, email: str, password: str) -> UserModel:
        """
        Creates a new user entity in the database and returns the user object.
        """

        new_user = UserModel(name=name, email=email, password=password)

        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)

        return new_user

    async def find_by_email(self, email: str) -> UserModel | None:
        """
        Finds a user by their email address.
        """

        results = await self.session.execute(
            select(UserModel).where(
                (UserModel.email == email) & UserModel.active.is_(True)
            )
        )
        return results.scalar_one_or_none()
