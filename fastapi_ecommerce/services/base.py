from typing import Any, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session


class BaseCRUD:
    def __init__(self, model, session: Session) -> None:
        self.session = session
        self.model = model

    async def create(self, **kwargs) -> Any:
        instance = self.model(**kwargs)
        self.session.add(instance)
        self.session.commit()
        return instance

    async def read(self, **kwargs) -> Optional[Any]:
        return self.session.execute(select(self.model).filter_by(**kwargs)).scalar()

    async def read_all(self) -> Optional[list[Any]]:
        return self.session.execute(select(self.model)).scalars().all()

    async def delete(self, id: int) -> None:
        instance = await self.read(id=id)
        if instance:
            self.session.delete(instance)
            self.session.commit()