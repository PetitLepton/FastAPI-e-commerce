from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi_ecommerce.models import Category, get_session
from fastapi_ecommerce.schemas import Category as CategorySerializer
from fastapi_ecommerce.services.product import CategoryCRUD
from sqlalchemy.orm import Session

router = APIRouter()


@router.get(
    "/categories/", response_model=list[CategorySerializer], status_code=status.HTTP_200_OK
)
async def get_categories(session: Session = Depends(get_session)):
    category_crud = CategoryCRUD(session=session)
    return await category_crud.read_all()


@router.post(
    "/categories/", response_model=CategorySerializer, status_code=status.HTTP_201_CREATED
)
async def create_category_registration(
    request: CategorySerializer, session: Session = Depends(get_session)
):

    category_crud = CategoryCRUD(session=session)

    category = await category_crud.read(name=request.name)

    if category:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A Category with this email address already exists.",
        )

    new_Category = await category_crud.create(name=request.name)
    return new_Category


@router.get("/categories/{id}", response_model=CategorySerializer, status_code=status.HTTP_200_OK)
async def get(id: int, session: Session = Depends(get_session)) -> Optional[Category]:
    return await CategoryCRUD(session).read(id=id)


@router.delete("/categories/{id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete(id: int, session: Session = Depends(get_session)) -> None:
    await CategoryCRUD(session).delete(id=id)
