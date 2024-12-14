from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

import settings
from api.v1.ranking import ranking_router
from database.db import init_db

app = FastAPI()
router = APIRouter()


@app.on_event("startup")
async def on_startup():
    await init_db()


app.include_router(ranking_router, prefix='/api/v1/ranking')
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOWED_ORIGINS,
    allow_methods=settings.CORS_ALLOWED_METHODS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_headers=settings.CORS_ALLOWED_HEADERS,
)
