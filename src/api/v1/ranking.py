from typing import Annotated

from fastapi import APIRouter, Body, Depends
from sqlalchemy import case, text
from sqlalchemy.orm import aliased
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from api.v1.dto.ranking import Ranking
from api.v1.helpers.database import load_raw_queries
from database.db import get_session
from models.ranking import Rank

ranking_router = APIRouter()

tags = ['ranking']


@ranking_router.get("/", tags=tags, response_model=list[Ranking])
async def ranking_base(session: AsyncSession = Depends(get_session)):
    query = load_raw_queries().get('SQL_STATEMENTS').get('SELECT_ALL_RANKINGS')
    async with session.begin():
        result = await session.execute(text(query))
        rankings = result.fetchall()
        return [Ranking.from_orm(rank) for rank in rankings]


@ranking_router.post("/", tags=tags, response_model=Rank)
async def ranking_base(
        ranking: Annotated[Rank, Body(embed=False)],
        session: AsyncSession = Depends(get_session)
) -> Ranking:
    print(ranking)
    async with session.begin():
        session.add(ranking)
        session.commit()
        session.refresh(ranking)
    return ranking
