from fastapi import FastAPI

from app.api.photos_router import router
from app.db.session import sessionmanager

def include_routers(fast_app: FastAPI) -> None:
    fast_app.include_router(router)

app = FastAPI()

include_routers(app)

@app.on_event("startup")
async def on_startup():
    sessionmanager.init_db()

@app.on_event("shutdown")
async def on_shutdown():
    await sessionmanager.close()




