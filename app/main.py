from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.photos_router import router
from app.db.session import sessionmanager

def include_routers(fast_app: FastAPI) -> None:
    fast_app.include_router(router)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://f1vus.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


include_routers(app)

@app.on_event("startup")
async def on_startup():
    sessionmanager.init_db()

@app.on_event("shutdown")
async def on_shutdown():
    await sessionmanager.close()




