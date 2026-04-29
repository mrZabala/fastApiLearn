from fastapi import FastAPI
from api.movie_controller import router as movie_router
from core.database import Base, engine


app = FastAPI()
    
app.include_router(movie_router)


Base.metadata.create_all(bind=engine)