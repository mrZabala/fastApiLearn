from pydantic import BaseModel
from typing import Optional

class UpdateMovie(BaseModel): 
    title: Optional[str] = None
    director: Optional[str] = None
    category: Optional[str] = None
    year: Optional[int] = None