from passlib.context import CryptContext
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property

from .base import Base

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return password_context.hash(password)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(255), unique=True)
    hashed_password = Column(String(255))

    @hybrid_property
    def password(self) -> str:
        return self.hashed_password

    @password.setter
    def password(self, password: str) -> None:
        self.hashed_password = get_password_hash(password)

    def is_correct_password(self, password: str):
        return verify_password(password, self.hashed_password)