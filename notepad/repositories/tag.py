from sqlalchemy.ext.asyncio import AsyncSession

from notepad.models.tag import Tag as TagModel
from notepad.models.tag import TextTag as TextTagModel
from notepad.models.text import Text as TextModel


class TagRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, text: TextModel, name: str) -> TagModel:
        tag = TagModel(name=name)

        texttag = TextTagModel()
        texttag.tag = tag
        texttag.text = text

        self.session.add(tag, texttag)
        await self.session.commit()
        await self.session.refresh(tag)

        return tag
