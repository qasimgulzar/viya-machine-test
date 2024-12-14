from typing import Optional

from pydantic import BaseModel


class Ranking(BaseModel):
    id: Optional[int]
    name: str
    net_points: int
    ranking: Optional[str]
    # Enable ORM serialization
    model_config = {
        "from_attributes": True
    }
