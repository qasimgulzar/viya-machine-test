from typing import Optional

from sqlmodel import Field, SQLModel


class Rank(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, )
    name: str = Field()
    net_points: int = Field()
