from fastapi import FastAPI
from api.movie_controller import router as movie_router

app = FastAPI()

app.include_router(movie_router)