from fastapi_ecommerce.models.user import User
from sqlalchemy.orm import Session

from .base import BaseCRUD


class UserCRUD(BaseCRUD):
    def __init__(self, session: Session) -> None:
        super().__init__(User, session)
