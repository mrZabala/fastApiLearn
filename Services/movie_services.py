from repository.movie_repository import (
    create_movie, get_all_movies, get_movie_by_imdb_id, search_movies_omdb_any,
    get_movie_by_title, get_movies_with_limit, search_movies_omdb,
    save_movie, get_movie_detail_omdb, bulk_save_movies,
    get_movie_count, search_movies_omdb_paginated, search_movies_omdb_any  
)
from core.enums.status import StatusMovie
from services.mappers.movie_mapper import map_movie
from core.enums.status import StatusMovie
from services.mappers.movie_mapper import map_movie


async def search_movies_service(query: str):
    data = await search_movies_omdb(query)
    if data.get("Response") == "False":
        return []

    return [
        {
            "title": item.get("Title"),
            "director": "N/A",
            "category": item.get("Type"),
            "year": int(item.get("Year", 0)),
            "imdb_id": item.get("imdbID"),
            "poster": item.get("Poster"),
            "status": StatusMovie.CREATED.value
        }
        for item in data.get("Search", [])
    ]

async def get_movie_detail_service(title: str, db):
    data = await get_movie_detail_omdb(title)
    if data.get("Response") == "False":
        return None

    existing_movie = get_movie_by_title(db, data.get("Title"))
    if existing_movie:
        return map_movie(existing_movie)

    saved_movie = create_movie(db, {
        "title": data.get("Title"),
        "director": data.get("Director"),
        "category": data.get("Genre"),
        "year": parse_year(data.get("Year")),
        "imdb_id": data.get("imdbID"),
        "poster": data.get("Poster"),
        "plot": data.get("Plot"),
        "status": StatusMovie.CREATED.value
    })
    return map_movie(saved_movie)

def get_all_movies_service(db):
    data = get_all_movies(db)
    return [map_movie(m) for m in data] if data else []

def get_movies_with_limit_service(db, limit: int):
    data = get_movies_with_limit(db, min(limit, 100))
    return [map_movie(m) for m in data] if data else []


async def bulk_import_movies_service(db, query: str = None, count: int = 100):
    """Importar películas — con query o sin criterio"""
    count = min(count, 100)

    # Con query usa paginación, sin query usa términos genéricos
    if query:
        search_results = await search_movies_omdb_paginated(query, max_results=count)
    else:
        search_results = await search_movies_omdb_any(max_results=count)

    if not search_results:
        return {"imported": 0, "message": "No se encontraron películas"}

    movies_to_import = [
        {
            "title": item.get("Title"),
            "director": "N/A",
            "category": item.get("Type"),
            "year": parse_year(item.get("Year")),
            "imdb_id": item.get("imdbID"),
            "poster": item.get("Poster"),
            "plot": "N/A",
            "status": StatusMovie.CREATED.value
        }
        for item in search_results
        if not get_movie_by_imdb_id(db, item.get("imdbID"))  # solo las que no existen
    ]

    if not movies_to_import:
        return {"imported": 0, "message": "Todas las películas ya existen en la BD"}

    saved_count = bulk_save_movies(db, movies_to_import)

    return {
        "imported": saved_count,
        "message": f"Se importaron {saved_count} películas correctamente",
        "total_in_db": get_movie_count(db)
    }

def parse_year(year_str):
    """Convierte '2019', '2019–', '2019-2021' a int de forma segura"""
    if not year_str:
        return None
    try:
        return int(str(year_str).strip().split("–")[0].split("-")[0])
    except (ValueError, AttributeError):
        return None