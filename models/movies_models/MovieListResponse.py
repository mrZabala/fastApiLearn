from typing import List, Optional, Union, Dict
from pydantic import BaseModel
from models.movies_models.movie_model import Movie
from models.movies_models.response_status import ResponseStatus

class MovieListResponse(BaseModel):
    status: ResponseStatus
    message: Optional[str] = None
    data: Union[List[Movie], List, Dict] = []
    
    class Config:
        # Permite que Pydantic sea más flexible
        arbitrary_types_allowed = True