from typing import Annotated

from fastapi import APIRouter, Body, Depends
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from api.v1.dto.ranking import Ranking
from api.v1.helpers.database import fetch_rankings
from database.db import get_session
from models.ranking import Rank

ranking_router = APIRouter()

tags = ['ranking']


@ranking_router.get("/", tags=tags, response_model=list[Ranking])
async def ranking_base(session: AsyncSession = Depends(get_session)):
    async with session.begin():
        return await fetch_rankings(session)


@ranking_router.post("/", tags=tags, response_model=list[Ranking])
async def ranking_base(
        ranking: Annotated[Rank, Body(embed=False)],
        session: AsyncSession = Depends(get_session)
):
    async with session.begin():
        session.add(ranking)
        session.commit()
    return await fetch_rankings(session)


@ranking_router.delete("/{id}/", tags=tags, response_model=list[Ranking])
async def delete_ranking(id: int, session: AsyncSession = Depends(get_session)):
    statement = select(Rank).where(Rank.id == id)
    async with session.begin():
        results = await session.exec(statement)
        await session.delete(results.one())
        session.commit()
    return await fetch_rankings(session)


@ranking_router.put("/{id}/", tags=tags, response_model=list[Ranking])
async def update_ranking(
        id: int,
        ranking: Annotated[Rank, Body(embed=False)],
        session: AsyncSession = Depends(get_session)
):
    statement = select(Rank).where(Rank.id == id)
    async with session.begin():
        results = await session.exec(statement)
        rank=results.one()
        rank.name=ranking.name
        rank.net_points=ranking.net_points
        session.add(rank)
        session.commit()
    return await fetch_rankings(session)
