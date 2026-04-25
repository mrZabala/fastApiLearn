# models/movies_models/movie_model.py
from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    title: str
    director: str
    category: str
    year: int