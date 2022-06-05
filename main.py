from fastapi import FastAPI
from fastapi_ecommerce.settings import db_settings
from fastapi_ecommerce.urls import product_router, user_router

app = FastAPI()


# @app.get("/")
# def index():
#     return {"message": "OK"}


def create_application():
    app = FastAPI()
    app.include_router(user_router, prefix="/users", tags=["Users"])
    app.include_router(product_router, prefix="/products", tags=["Products"])
    return app


app = create_application()