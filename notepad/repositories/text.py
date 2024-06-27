from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from notepad.models.text import Text as TextModel
from notepad.models.user import User as UserModel


class TextRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(
        self, user: UserModel, content: str, title: str
    ) -> TextModel:

        text = TextModel(content=content, title=title)

        text.user = user

        self.session.add(text)
        await self.session.commit()
        await self.session.refresh(text)

        return text

    async def get_last_n(self, count: int = 5) -> list[TextModel]:
        results = await self.session.execute(
            select(TextModel)
            .order_by(TextModel.last_update_date.desc())
            .limit(count)
        )
        return results.scalars().all()
