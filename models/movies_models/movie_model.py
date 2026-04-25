from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    title: str
    director: str
    category: str
    year: int