from typing import Optional

from pydantic import BaseModel, EmailStr, constr


class User(BaseModel):
    id: Optional[int]
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
