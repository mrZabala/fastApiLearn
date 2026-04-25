from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
import random

app = FastAPI()
app.title = "Weso API"
app.version = "0.1.0"
response_class=HTMLResponse
automatic_id = random.randint(1000, 9999) # Generate a random ID for new movies

movies = [
    {"id": automatic_id, "title": "Inception", "director": "Christopher Nolan", "category": "Sci-Fi", "year": 2010},
    {"id": automatic_id, "title": "The Matrix", "director": "Lana Wachowski, Lilly Wachowski", "category": "Action", "year": 1999},
    {"id": automatic_id, "title": "Interstellar", "director": "Christopher Nolan", "category": "Sci-Fi", "year": 2014}
]

# Define a home endpoint
@app.get('/', tags=["Home"]) #define a rout and enpoint's tag name
def home():#Endpoint action
    return "Weso" #Endpoint response


# Define more endpoints for movies
@app.get('/movies', tags=["Movies"])
def get_all_movies():
    return movies
    # return response_class(content="<h1>Movies</h1><p>List of movies will be here.</p>")

@app.get('/movies/id/{id}', tags=["Movies"])
def get_movie_by_id(id: int):
    for movie in movies:
        if movie['id'] == id:
            return movie
    return {"error": "Movie not found"}

@app.get('/movies/{query}', tags=["Movies"]) #query can be either title or director
def get_movie_by_reference(query: str):
    for movie in movies:
        if movie['title'] == query or movie['director'] == query:
            return movie
    return {"error": "Movie not found"}

@app.get('/movies/{title}', tags=["Movies"]) #query can be either title or director
def get_movie_by_title(title: str):
    for movie in movies:
        if movie['title'] == title:
            return {"title": movie['title']}
    return {"error": "Movie not found"}

@app.get('/movies/year/{year}', tags=["Movies"]) #query can be either title or director
def get_movie_by_year(year: int):
    for movie in movies:
        if movie['year'] == year:
            return {"year": movie['year']}
    return {"error": "Movie not found"}

@app.get('/movies/', tags=["Movies"]) #query params
def get_movie_by_category(category: str, year: int):
    for movie in movies:
        if movie['category'] == category:
            return movie
    return {"error": "Movie not found"}

@app.post('/movies', tags=["movies"])
def create_movies(id: int = Body(automatic_id), title: str = Body(...), director: str = Body(...), category: str = Body(...), year: int = Body(...)):
    movies.append({
        'id': id,
        'title': title,
        'director': director,
        'category': category,
        'year': year
    })
    return movies

@app.put('/movies/{id}', tags=["movies"])
def update_movie(id: int, title: str = Body(...), director: str = Body(...), category: str = Body(...), year: int = Body(...)):
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['director'] = director
            movie['category'] = category
            movie['year'] = year
            return movie
    return {"error": "Movie not found"}