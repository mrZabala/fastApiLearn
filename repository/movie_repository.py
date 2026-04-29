import httpx
from sqlalchemy.orm import Session
from models.db.movie_entity import MovieEntity

OMDB_API_URL = "https://www.omdbapi.com/"
OMDB_API_KEY = "8a90e22f"


def get_all_movies(db: Session):
    return db.query(MovieEntity).all()


def create_movie(db: Session, movie_data: dict):
    movie = MovieEntity(**movie_data)
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie


def get_movie_by_id(db: Session, movie_id: int):
    return db.query(MovieEntity).filter(MovieEntity.id == movie_id).first()


def update_movie(db: Session, movie_id: int, update_data: dict):
    movie = get_movie_by_id(db, movie_id)
    if not movie:
        return None

    for key, value in update_data.items():
        setattr(movie, key, value)

    db.commit()
    db.refresh(movie)
    return movie


def delete_movie(db: Session, movie_id: int):
    movie = get_movie_by_id(db, movie_id)
    if not movie:
        return None

    db.delete(movie)
    db.commit()
    return movie


async def search_movies_omdb(query: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            OMDB_API_URL,
            params={
                "apikey": OMDB_API_KEY,
                "s": query
            }
        )
        return response.json()


async def get_movie_detail_omdb(title: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            OMDB_API_URL,
            params={
                "apikey": OMDB_API_KEY,
                "t": title
            }
        )
        return response.json()


def get_movie_by_title(db: Session, title: str):
    return db.query(MovieEntity).filter(MovieEntity.title == title).first()


def get_movie_by_imdb_id(db: Session, imdb_id: str):
    return db.query(MovieEntity).filter(MovieEntity.imdb_id == imdb_id).first()


def get_movies_with_limit(db: Session, limit: int):
    return db.query(MovieEntity).limit(limit).all()


def save_movie(db: Session, movie_data: dict):
    movie = MovieEntity(
        title=movie_data.get("title"),
        year=movie_data.get("year"),
        imdb_id=movie_data.get("imdb_id"),
        category=movie_data.get("category"),
        poster=movie_data.get("poster"),
        director=movie_data.get("director"),
        plot=movie_data.get("plot")
    )

    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie


def bulk_save_movies(db: Session, movies_list: list):
    """Guardar múltiples películas a la vez"""
    count = 0
    for movie_data in movies_list:
        try:
            movie = MovieEntity(**movie_data)
            db.add(movie)
            count += 1
        except Exception:
            continue
    
    db.commit()
    return count


def get_movie_count(db: Session):
    """Obtener cantidad total de películas en BD"""
    return db.query(MovieEntity).count()