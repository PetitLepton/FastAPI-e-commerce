from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi_ecommerce.models import User, get_session
from fastapi_ecommerce.schemas import User as UserSerializer
from fastapi_ecommerce.services.user import UserCRUD
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=list[UserSerializer], status_code=status.HTTP_200_OK)
async def get_users(session: Session = Depends(get_session)):
    user_crud = UserCRUD(session=session)
    return await user_crud.read_all()


@router.post("/", response_model=UserSerializer, status_code=status.HTTP_201_CREATED)
async def create_user_registration(
    request: UserSerializer, session: Session = Depends(get_session)
):

    user_crud = UserCRUD(session=session)

    user = await user_crud.read(email=request.email)

    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email address already exists.",
        )

    new_user = await user_crud.create(
        name=request.name, email=request.email, password=request.password
    )
    return new_user


@router.get("/{id}", response_model=UserSerializer, status_code=status.HTTP_200_OK)
async def get(id: int, session: Session = Depends(get_session)) -> Optional[User]:
    return await UserCRUD(session).read(id=id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete(id: int, session: Session = Depends(get_session)) -> None:
    await UserCRUD(session).delete(id=id)
