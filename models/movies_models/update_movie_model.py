from pydantic import BaseModel
from typing import Optional
from core.enums.status import StatusMovie

class UpdateMovie(BaseModel): 
    title: Optional[str] = None
    director: Optional[str] = None
    category: Optional[str] = None
    year: Optional[int] = None
