from pydantic import BaseModel
from core.enums.status import StatusMovie
class CreateMovie(BaseModel):  
    title: str
    director: str
    category: str
    year: int
    
    