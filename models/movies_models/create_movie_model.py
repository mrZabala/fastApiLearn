from pydantic import BaseModel, Field
from typing import Optional

class CreateMovie(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    director: str = Field(..., min_length=1)
    category: str = Field(..., min_length=1)
    year: int = Field(..., ge=1888, le=2100)
    imdb_id: Optional[str] = None
    poster: Optional[str] = None
    plot: Optional[str] = None