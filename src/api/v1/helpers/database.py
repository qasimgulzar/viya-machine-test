import functools

import yaml
from sqlalchemy import text

from api.v1.dto.ranking import Ranking


@functools.cache
def load_raw_queries():
    with open('raw-sql-statements.yaml') as f:
        return yaml.load(f, Loader=yaml.FullLoader)


async def fetch_rankings(session):
    query = load_raw_queries().get('SQL_STATEMENTS').get('SELECT_ALL_RANKINGS')

    result = await session.execute(text(query))
    rankings = result.fetchall()
    return [Ranking.from_orm(rank) for rank in rankings]
