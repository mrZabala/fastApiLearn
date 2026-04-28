from pydantic import BaseModel
from core.enums.status import StatusMovie

class Movie(BaseModel):
    id: int
    title: str
    director: str
    category: str
    year: int
    status: StatusMovie
