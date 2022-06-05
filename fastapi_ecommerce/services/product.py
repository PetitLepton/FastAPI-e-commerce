from typing import Optional

from fastapi_ecommerce.models import Category
from sqlalchemy import select
from sqlalchemy.orm import Session


class CategoryCRUD:
    def __init__(self, session: Session) -> None:
        self.session = session

    async def create(self, name: str) -> Category:
        category = Category(name=name)
        self.session.add(category)
        self.session.commit()
        return category

    async def read(self, **kwargs) -> Optional[Category]:
        return self.session.execute(select(Category).filter_by(**kwargs)).scalar()

    async def read_all(self) -> Optional[list[Category]]:
        return self.session.execute(select(Category)).scalars().all()

    async def delete(self, id: int) -> None:
        Category = await self.read(id=id)
        if Category:
            self.session.delete(Category)
            self.session.commit()