from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UpdateMovie(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    director: Optional[str] = Field(None, min_length=1)
    category: Optional[str] = Field(None, min_length=1)
    year: Optional[int] = Field(None, ge=1888, le=2100)
    imdb_id: Optional[str] = None
    poster: Optional[str] = None
    plot: Optional[str] = None
    is_deleted: Optional[bool] = None
    deleted_at: Optional[datetime] = None
    def to_update_dict(self):
        return {k: v for k, v in self.model_dump().items() if v is not None}