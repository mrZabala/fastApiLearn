from pydantic import BaseModel
from typing import Any, Optional
from models.movies_models.response_status import ResponseStatus

class MovieListResponse(BaseModel):
    status: ResponseStatus
    message: Optional[str] = None
    data: Any = []

    model_config = {"arbitrary_types_allowed": True}