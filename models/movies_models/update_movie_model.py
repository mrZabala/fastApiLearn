# models/movies_models/update_movie_model.py
from pydantic import BaseModel
from typing import Optional

class UpdateMovie(BaseModel):  # ← quita el guión bajo
    title: Optional[str] = None
    director: Optional[str] = None
    category: Optional[str] = None
    year: Optional[int] = None