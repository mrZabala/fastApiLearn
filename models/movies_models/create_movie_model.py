# models/movies_models/create_movie_model.py
from pydantic import BaseModel

class CreateMovie(BaseModel):  
    title: str
    director: str
    category: str
    year: int