from pydantic import BaseModel

class CreateMovie(BaseModel):  
    title: str
    director: str
    category: str
    year: int