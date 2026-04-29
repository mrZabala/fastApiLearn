def map_movie(movie):
    return {
        "id": movie.id,
        "title": movie.title,
        "director": movie.director,
        "category": movie.category,
        "year": movie.year,
        "status": movie.status
    }