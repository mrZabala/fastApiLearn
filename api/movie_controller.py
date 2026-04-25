from core.utils import generate_id
from models import CreateMovie, UpdateMovie, Movie
from fastapi import APIRouter

router = APIRouter(prefix="/movies", tags=["Movies"])  # ← prefijo y tag

movies = [
    {"id": generate_id(), "title": "Inception", "director": "Christopher Nolan", "category": "Sci-Fi", "year": 2010},
    {"id": generate_id(), "title": "The Matrix", "director": "Wachowski Sisters", "category": "Action", "year": 1999},
]

@router.get("/")
def get_all_movies():
    return movies

@router.get("/search")  # ← debe ir ANTES de /{id}
def search_movie(query: str):
    return [
        movie for movie in movies
        if query.lower() in movie["title"].lower()
        or query.lower() in movie["director"].lower()
    ]

@router.get("/{id}")
def get_movie_by_id(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return {"error": "Movie not found"}

@router.post("/")
def create_movie(new_movie: CreateMovie):
    movie = new_movie.model_dump()
    movie["id"] = generate_id()
    movies.append(movie)
    return movie

@router.put("/{id}")
def update_movie(id: int, updated_movie: UpdateMovie):
    for movie in movies:
        if movie["id"] == id:
            movie.update(updated_movie.model_dump())
            return movie
    return {"error": "Movie not found"}

@router.delete("/{id}")
def delete_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            return {"message": "Deleted"}
    return {"error": "Movie not found"}