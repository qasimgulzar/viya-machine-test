from fastapi import FastAPI, APIRouter

from api.v1.ranking import ranking_router
from database.db import init_db

app = FastAPI()
router = APIRouter()


@app.on_event("startup")
async def on_startup():
    await init_db()


app.include_router(ranking_router, prefix='/api/v1/ranking')
app.include_router(router)
