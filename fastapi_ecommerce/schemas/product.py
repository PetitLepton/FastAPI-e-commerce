from typing import Optional

from pydantic import BaseModel, constr


class Category(BaseModel):
    id: Optional[int]
    name: constr(min_length=2, max_length=50)

    class Config:
        orm_mode = True
