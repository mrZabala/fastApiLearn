from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Movie(BaseModel):
    id: int
    title: str
    director: Optional[str] = None
    category: Optional[str] = None
    year: Optional[int] = None
    status: str
    imdb_id: Optional[str] = None
    poster: Optional[str] = None
    plot: Optional[str] = None
    is_deleted: bool = False
    deleted_at: Optional[datetime] = None
    model_config = {"from_attributes": True}