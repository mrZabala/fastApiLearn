from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from core.database import get_db
from core.build_response import build_response
from models.db.movie_entity import MovieEntity
from models.movies_models.MovieListResponse import MovieListResponse
from models.movies_models.response_status import ResponseStatus
from models.movies_models.create_movie_model import CreateMovie
from models.movies_models.update_movie_model import UpdateMovie
from services.movie_services import (
    get_all_movies_service,
    get_movie_by_filter_service,
    get_movies_with_limit_service,
    bulk_import_movies_service,
    create_movie_service,
    get_movie_by_director_service
)
from repository.movie_repository import update_movie, delete_movie, get_movie_by_id
from services.mappers.movie_mapper import map_movie

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("/all", response_model=MovieListResponse)
def get_all_movies(db: Session = Depends(get_db)):
    movies = get_all_movies_service(db)
    return build_response(
        status=ResponseStatus.SUCCESS if movies else ResponseStatus.EMPTY,
        data=movies or [],
        message=f"Se encontraron {len(movies)} películas" if movies else "No hay películas"
    )


@router.get("/filter", response_model=MovieListResponse)
def get_movies_by_filter(
    year: int = Query(None),
    category: str = Query(None),
    director: str = Query(None),
    db: Session = Depends(get_db)
):
    movies = get_movie_by_filter_service(db, year, category, director)
    return build_response(
        status=ResponseStatus.SUCCESS if movies else ResponseStatus.EMPTY,
        data=movies or [],
        message=f"Se encontraron {len(movies)} películas"
    )

@router.get("/director", response_model=MovieListResponse)
def get_movie_by_director(
    director: str,
    db: Session = Depends(get_db)         
):
    directors = get_movie_by_director_service(db, director)
    return build_response(
        status=ResponseStatus.SUCCESS if directors else ResponseStatus.EMPTY,
        data=directors or [],
        message=f"Se encontraron {len(directors)} directores"
    )

@router.get("/limited", response_model=MovieListResponse)
def get_movies_limited(
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    movies = get_movies_with_limit_service(db, limit)
    return build_response(
        status=ResponseStatus.SUCCESS if movies else ResponseStatus.EMPTY,
        data=movies or [],
        message=f"Se encontraron {len(movies)} películas"
    )


@router.get("/paginated", response_model=MovieListResponse)
def get_movies_paginated(
    limit: int = Query(20, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    movies = db.query(MovieEntity).offset(offset).limit(limit).all()

    return build_response(
        status=ResponseStatus.SUCCESS if movies else ResponseStatus.EMPTY,
        data=[map_movie(m) for m in movies],
        message=f"Se encontraron {len(movies)} películas (offset={offset})"
    )

@router.post("/", response_model=MovieListResponse)
async def create_movie(movie: CreateMovie, db: Session = Depends(get_db)):
    result = await create_movie_service(db, movie.model_dump())
    return build_response(
        status=ResponseStatus.SUCCESS,
        data=result,
        message="Película creada"
    )


@router.post("/import", response_model=MovieListResponse)
async def bulk_import_movies(
    query: str = Query(None),
    count: int = Query(100, ge=1),
    db: Session = Depends(get_db)
):
    result = await bulk_import_movies_service(db, query, count)
    return build_response(
        status=ResponseStatus.SUCCESS if result["imported"] > 0 else ResponseStatus.EMPTY,
        data=result,
        message=result.get("message", "")
    )

@router.get("/debug/count")
def debug_count(db: Session = Depends(get_db)):
    from sqlalchemy import text
    return {
        "orm_count": db.query(MovieEntity).count(),
        "raw_sql_count": db.execute(text("SELECT COUNT(*) FROM movie")).scalar()
    }

@router.get("/id/{movie_id}", response_model=MovieListResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = get_movie_by_id(db, movie_id)
    return build_response(
        status=ResponseStatus.SUCCESS if movie else ResponseStatus.EMPTY,
        data=map_movie(movie) if movie else [],
        message="OK" if movie else "Película no encontrada"
    )

@router.put("/id/{movie_id}", response_model=MovieListResponse)
def update_movie_endpoint(movie_id: int, movie: UpdateMovie, db: Session = Depends(get_db)):
    updated = update_movie(db, movie_id, movie.to_update_dict())
    return build_response(
        status=ResponseStatus.SUCCESS if updated else ResponseStatus.ERROR,
        data=map_movie(updated) if updated else [],
        message="Película actualizada" if updated else "Película no encontrada"
    )

@router.delete("/id/{movie_id}", response_model=MovieListResponse)
def delete_movie_endpoint(movie_id: int, db: Session = Depends(get_db)):
    deleted = delete_movie(db, movie_id)
    return build_response(
        status=ResponseStatus.SUCCESS if deleted else ResponseStatus.ERROR,
        data=[],
        message="Película eliminada" if deleted else "Película no encontrada"
    )