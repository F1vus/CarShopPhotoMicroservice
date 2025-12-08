from typing import Union

from fastapi import FastAPI

from app.api.photos_router import router

__all__ = ("create_app",)

def create_app() -> FastAPI:
    app = FastAPI()

    include_routers(app)

    return app


def include_routers(app: FastAPI) -> None:
    app.include_router(router)

