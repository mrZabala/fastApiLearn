from typing import List, Optional
from pydantic import BaseModel
from models.movies_models.movie_model import Movie
from models.movies_models.response_status import ResponseStatus

class MovieListResponse(BaseModel):
    status: ResponseStatus
    message: Optional[str] = None
    data: List[Movie]