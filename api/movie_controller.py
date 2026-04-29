from core.utils import generate_id
from fastapi import APIRouter
from models.movies_models.MovieListResponse import MovieListResponse
from models.movies_models.response_status import ResponseStatus
from core.build_response import build_response
from services.movie_services import (
    get_all_movies_service, get_movie_detail_service, 
    get_movies_with_limit_service, bulk_import_movies_service
)
from fastapi import Depends, Query
from sqlalchemy.orm import Session
from core.database import get_db

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.get("/all", response_model=MovieListResponse)
def get_all_movies(db: Session = Depends(get_db)):
    """Obtener todas las películas de la BD"""
    movies = get_all_movies_service(db)

    if not movies:
        return build_response(
            status=ResponseStatus.EMPTY,
            data=[],
            message="No hay películas guardadas"
        )

    return build_response(
        status=ResponseStatus.SUCCESS,
        data=movies,
        message=f"Se encontraron {len(movies)} películas"
    )


@router.get("/limited", response_model=MovieListResponse)
def get_movies_limited(
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Obtener películas con límite (máx 100)"""
    movies = get_movies_with_limit_service(db, limit)

    if not movies:
        return build_response(
            status=ResponseStatus.EMPTY,
            data=[],
            message="No hay películas disponibles"
        )

    return build_response(
        status=ResponseStatus.SUCCESS,
        data=movies,
        message=f"Se encontraron {len(movies)} películas"
    )


@router.post("/import", response_model=dict)
async def bulk_import_movies(
    query: str = Query(..., description="Término de búsqueda en OMDb"),
    count: int = Query(100, ge=1, le=100, description="Cantidad de películas a importar (máx 100)"),
    db: Session = Depends(get_db)
):
    """
    ✨ Importar hasta 100 películas de OMDb en una sola operación
    
    Ejemplo: /movies/import?query=marvel&count=100
    """
    result = await bulk_import_movies_service(db, query, count)
    
    return build_response(
        status=ResponseStatus.SUCCESS if result["imported"] > 0 else ResponseStatus.EMPTY,
        data=result,
        message=result.get("message", "")
    )