from repository.movie_repository import (
    create_movie, get_all_movies, get_movie_by_imdb_id, 
    get_movie_by_title, get_movies_with_limit, search_movies_omdb, 
    save_movie, get_movie_detail_omdb, bulk_save_movies,
    get_movie_count
)
from core.enums.status import StatusMovie
from services.mappers.movie_mapper import map_movie


async def search_movies_service(query: str):
    """Buscar películas en OMDb por query"""
    data = await search_movies_omdb(query)

    if data.get("Response") == "False":
        return []

    movies = []
    for item in data.get("Search", []):
        movies.append({
            "title": item.get("Title"),
            "director": "N/A", 
            "category": item.get("Type"),
            "year": int(item.get("Year", 0)),
            "imdb_id": item.get("imdbID"),
            "poster": item.get("Poster"),
            "status": StatusMovie.CREATED.value
        })

    return movies


async def get_movie_detail_service(title: str, db):
    """Obtener detalles de película de OMDb y guardar en BD"""
    data = await get_movie_detail_omdb(title)

    if data.get("Response") == "False":
        return None

    existing_movie = get_movie_by_title(db, data.get("Title"))

    if existing_movie:
        return map_movie(existing_movie)

    new_movie = {
        "title": data.get("Title"),
        "director": data.get("Director"),
        "category": data.get("Genre"),
        "year": int(data.get("Year", 0)),
        "imdb_id": data.get("imdbID"),
        "poster": data.get("Poster"),
        "plot": data.get("Plot"),
        "status": StatusMovie.CREATED.value
    }

    saved_movie = create_movie(db, new_movie)
    return map_movie(saved_movie)


def get_all_movies_service(db):
    """Obtener todas las películas"""
    data = get_all_movies(db)

    if not data:
        return []

    return [map_movie(m) for m in data]


def get_movies_with_limit_service(db, limit: int):
    """Obtener películas con límite"""
    if limit > 100:
        limit = 100

    data = get_movies_with_limit(db, limit)

    if not data:
        return []

    return [map_movie(m) for m in data]


async def bulk_import_movies_service(db, query: str, count: int = 100):
    """Importar múltiples películas de OMDb en una sola operación"""
    if count > 100:
        count = 100
    
    data = await search_movies_omdb(query)
    
    if data.get("Response") == "False":
        return {"imported": 0, "message": "No se encontraron películas"}
    
    movies_to_import = []
    for item in data.get("Search", [])[:count]:
        existing = get_movie_by_imdb_id(db, item.get("imdbID"))
        
        if not existing:
            movies_to_import.append({
                "title": item.get("Title"),
                "director": "N/A",
                "category": item.get("Type"),
                "year": int(item.get("Year", 0)) if item.get("Year") else None,
                "imdb_id": item.get("imdbID"),
                "poster": item.get("Poster"),
                "plot": "N/A",
                "status": StatusMovie.CREATED.value
            })
    
    if not movies_to_import:
        return {"imported": 0, "message": "Todas las películas ya existen en la BD"}
    
    saved_count = bulk_save_movies(db, movies_to_import)
    
    return {
        "imported": saved_count,
        "message": f"Se importaron {saved_count} películas correctamente",
        "total_in_db": get_movie_count(db)
    }