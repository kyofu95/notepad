"""This module defines a Pydantic schema for a User scheme."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr

from .text import Text, TextDB


class UserBase(BaseModel):
    """Base pydantic schema for a user profile."""

    name: str


class UserCreate(UserBase):
    """User schema for creating a new user account."""

    email: EmailStr
    password: str


class User(UserBase):
    """Pydantic schema for a user entity."""

    created_at: datetime

    texts: list[Text]


class UserDB(User):
    """A pydantic schema tailored for database interactions."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    last_login_date: datetime
    last_update_date: datetime
    active: bool

    texts: list[TextDB]
