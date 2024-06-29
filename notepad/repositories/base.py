"""
A module providing base repository functionalities for interacting with databases asynchronously using SQLAlchemy.
"""

from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    """
    Provides a base structure for repositories that interact with the database asynchronously.
    """

    def __init__(self, async_session: AsyncSession) -> None:
        self.session = async_session
