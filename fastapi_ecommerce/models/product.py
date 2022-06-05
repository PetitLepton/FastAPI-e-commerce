from decimal import Decimal
from unicodedata import numeric

from passlib.context import CryptContext
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from .base import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Numeric(2), nullable=False)

    category_id = Column(ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="products")
