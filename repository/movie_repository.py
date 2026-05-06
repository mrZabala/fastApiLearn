# repository/movie_repository.py

from datetime import datetime
import httpx
from sqlalchemy.orm import Session
from core.config import GENERIC_QUERIES, OMDB_API_KEY, OMDB_API_URL
from models.db.movie_entity import MovieEntity


def get_all_movies(db: Session):
    return db.query(MovieEntity).filter(MovieEntity.is_deleted == False).all()

def get_movie_by_id(db: Session, movie_id: int):
    return db.query(MovieEntity).filter(
        MovieEntity.id == movie_id,
        MovieEntity.is_deleted == False
    ).first()

def get_movie_by_title(db: Session, title: str):
    return db.query(MovieEntity).filter(
        MovieEntity.title == title,
        MovieEntity.is_deleted == False
    ).first()

def get_movie_by_director(db: Session, director: str):
    return db.query(MovieEntity).filter(
        MovieEntity.director == director,
        MovieEntity.is_deleted == False
    ).all()

def get_movie_by_imdb_id(db: Session, imdb_id: str):
    return db.query(MovieEntity).filter(
        MovieEntity.imdb_id == imdb_id,
        MovieEntity.is_deleted == False
    ).first()

def get_movie_by_filter(db: Session, year=None, category=None, director=None):
    query = db.query(MovieEntity).filter(MovieEntity.is_deleted == False)
    if year:
        query = query.filter(MovieEntity.year == year)
    if category:
        query = query.filter(MovieEntity.category == category)
    if director:
        query = query.filter(MovieEntity.director == director)
    return query.all()

def get_movies_with_limit(db: Session, limit: int):
    return db.query(MovieEntity).filter(
        MovieEntity.is_deleted == False
    ).limit(limit).all()

def get_movie_count(db: Session):
    return db.query(MovieEntity).filter(MovieEntity.is_deleted == False).count()

def create_movie(db: Session, movie_data: dict):
    movie = MovieEntity(**movie_data)
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie

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
    movie.is_deleted = True
    movie.deleted_at = datetime.utcnow()
    db.commit()
    db.refresh(movie)
    return movie

def bulk_save_movies(db: Session, movies_list: list):
    count = 0
    for movie_data in movies_list:
        try:
            db.begin_nested()
            movie = MovieEntity(**movie_data)
            db.add(movie)
            db.flush()
            count += 1
        except Exception:
            db.rollback()
            continue
    db.commit()
    return count


async def search_movies_omdb(query: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            OMDB_API_URL,
            params={"apikey": OMDB_API_KEY, "s": query}
        )
        return response.json()

async def get_movie_detail_omdb(title: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            OMDB_API_URL,
            params={"apikey": OMDB_API_KEY, "t": title}
        )
        return response.json()

async def search_movies_omdb_paginated(query: str, max_results: int = 100):
    all_movies = []
    page = 1
    async with httpx.AsyncClient() as client:
        while len(all_movies) < max_results:
            response = await client.get(
                OMDB_API_URL,
                params={"apikey": OMDB_API_KEY, "s": query, "page": page}
            )
            data = response.json()
            if data.get("Response") == "False":
                break
            results = data.get("Search", [])
            if not results:
                break
            all_movies.extend(results)
            total_results = int(data.get("totalResults", 0))
            if len(all_movies) >= total_results:
                break
            page += 1
    return all_movies[:max_results]

async def search_movies_omdb_any(max_results: int = 100):
    all_movies = {}
    async with httpx.AsyncClient() as client:
        for query in GENERIC_QUERIES:
            if len(all_movies) >= max_results:
                break
            page = 1
            while len(all_movies) < max_results:
                response = await client.get(
                    OMDB_API_URL,
                    params={"apikey": OMDB_API_KEY, "s": query, "page": page}
                )
                data = response.json()
                if data.get("Response") == "False":
                    break
                for item in data.get("Search", []):
                    imdb_id = item.get("imdbID")
                    if imdb_id and imdb_id not in all_movies:
                        all_movies[imdb_id] = item
                total_results = int(data.get("totalResults", 0))
                if len(all_movies) >= total_results or page * 10 >= total_results:
                    break
                page += 1
    return list(all_movies.values())[:max_results]