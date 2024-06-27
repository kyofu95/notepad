from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from notepad.models.user import User as UserModel


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, name: str, email: str, password: str) -> UserModel:
        new_user = UserModel(name=name, email=email, password=password)

        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)

        return new_user

    async def find_by_email(self, email: str) -> UserModel | None:
        results = await self.session.execute(
            select(UserModel).where(
                (UserModel.email == email) & UserModel.active.is_(True)
            )
        )
        return results.scalar_one_or_none()
