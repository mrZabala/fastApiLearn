from models.movies_models.movie_model import Movie
from models.db.movie_entity import MovieEntity

def map_movie(entity: MovieEntity) -> Movie:
    return Movie.model_validate(entity)