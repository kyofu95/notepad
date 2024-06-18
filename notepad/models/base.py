"""Base module for database models."""

from typing_extensions import Annotated

from sqlalchemy.orm import DeclarativeBase, mapped_column


class BaseModel(DeclarativeBase):
    """
    This class provides a foundation for defining database models.
    """


int_primarykey = Annotated[int, mapped_column(primary_key=True)]
