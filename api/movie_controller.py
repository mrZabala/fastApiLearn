from core.utils import generate_id
from models import CreateMovie, UpdateMovie, Movie
from fastapi import APIRouter
from fastapi import HTTPException
from core.enums.status import StatusMovie
from models.movies_models.MovieListResponse import MovieListResponse
from models.movies_models.response_status import ResponseStatus
from core.enums.status import StatusMovie
from core.build_response import build_response

router = APIRouter(prefix="/movies", tags=["Movies"])

movies = [
    {"id": generate_id(), "title": "Inception", "director": "Christopher Nolan", "category": "Sci-Fi", "year": 2010, "status": StatusMovie.CREATED},
    {"id": generate_id(), "title": "The Matrix", "director": "Wachowski Sisters", "category": "Action", "year": 1999,  "status": StatusMovie.CREATED},
]

@router.get("/", response_model=MovieListResponse)
def get_all_movies():
    if not movies:
        return build_response(
            status=ResponseStatus.EMPTY,
            data=[],
            message="No hay películas registradas"
        )

    return build_response(
        status=ResponseStatus.SUCCESS,
        data=movies
    )


@router.get("/search", response_model=MovieListResponse)
def search_movie(query: str):
    result = [
        movie for movie in movies
        if query.lower() in movie["title"].lower()
        or query.lower() in movie["director"].lower()
    ]

    if not result:
        return build_response(
            status=ResponseStatus.EMPTY,
            data=[],
            message="No results found"
        )

    return build_response(
        status=ResponseStatus.SUCCESS,
        data=result
    )


@router.get("/{id}", response_model=MovieListResponse)
def get_movie_by_id(id: int):
    for movie in movies:
        if movie["id"] == id:
            return build_response(
                status=ResponseStatus.SUCCESS,
                data=[movie]
            )

    raise HTTPException(status_code=404, detail="Movie not found")


@router.post("/", response_model=MovieListResponse)
def create_movie(new_movie: CreateMovie):
    movie = new_movie.model_dump()
    movie["id"] = generate_id()
    movie["status"] = StatusMovie.CREATED
    movies.append(movie)

    return build_response(
        status=ResponseStatus.SUCCESS,
        data=[movie],
        message="Movie created"
    )


# ✅ UPDATE
@router.put("/{id}", response_model=MovieListResponse)
def update_movie(id: int, updated_movie: UpdateMovie):
    for movie in movies:
        if movie["id"] == id:
            update_data = updated_movie.model_dump(exclude_unset=True)
            movie.update(update_data)
            movie["status"] = StatusMovie.UPDATED

            return build_response(
                status=ResponseStatus.SUCCESS,
                data=[movie],
                message="Movie updated"
            )

    raise HTTPException(status_code=404, detail="Movie not found")


# ✅ DELETE
@router.delete("/{id}", response_model=MovieListResponse)
def delete_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            movie["status"] = StatusMovie.DELETED

            return build_response(
                status=ResponseStatus.SUCCESS,
                data=[movie],
                message="Movie deleted"
            )

    raise HTTPException(status_code=404, detail="Movie not found")