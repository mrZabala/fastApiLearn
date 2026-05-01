from pydantic import BaseModel, Field
from typing import Optional

class UpdateMovie(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    director: Optional[str] = None
    category: Optional[str] = None
    year: Optional[int] = Field(None, ge=1888, le=2100)
    status: Optional[str] = None
    poster: Optional[str] = None
    plot: Optional[str] = None

    def to_update_dict(self) -> dict:
        # Solo retorna los campos enviados (excluye None)
        return self.model_dump(exclude_none=True)