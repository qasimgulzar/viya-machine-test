from typing import Annotated

from fastapi import APIRouter, Body, Depends
from sqlalchemy import case, text
from sqlalchemy.orm import aliased
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from api.v1.dto.ranking import Ranking
from database.db import get_session
from models.ranking import Rank

ranking_router = APIRouter()

tags = ['ranking']


@ranking_router.get("/", tags=tags, response_model=list[Ranking])
async def ranking_base(session: AsyncSession = Depends(get_session)):
    async with session.begin():
        query = """
            SELECT rank.id,
            rank.name,
            rank.net_points,
            CASE
                WHEN CAST(R.c as numeric) > 1 THEN R.id
                ELSE rank.id::text
            END AS ranking
            FROM rank left outer join (select concat(min(id), 'T') as id, CAST(count(*) as numeric) as c, net_points
            from rank
            group by net_points) R on R.net_points = rank.net_points
            ORDER BY rank.net_points desc;
        """
        result = await session.execute(text(query))
        rankings = result.fetchall()
        return [Ranking.from_orm(rank) for rank in rankings]


@ranking_router.post("/", tags=tags, response_model=Ranking)
async def ranking_base(
        ranking: Annotated[Rank, Body(embed=False)],
        session: AsyncSession = Depends(get_session)
) -> Ranking:
    print(ranking)
    async with session.begin():
        session.add(ranking)
        session.commit()
        session.refresh(ranking)
    return Ranking.from_orm(ranking)
