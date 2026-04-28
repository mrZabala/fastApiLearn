from typing import Any, Optional
from models.movies_models.response_status import ResponseStatus
from models.movies_models.MovieListResponse import MovieListResponse


def build_response(
    status: ResponseStatus,
    data: Any,
    message: Optional[str] = None
) -> MovieListResponse:

    return MovieListResponse(
        status=status,
        message=message,
        data=data
    )