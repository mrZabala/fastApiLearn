from sqlalchemy import Column, Integer, String
from core.database import Base

class MovieEntity(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    director = Column(String, nullable=True)
    category = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    status = Column(String, default="Creado")
    imdb_id = Column(String, unique=True, nullable=True, index=True)
    poster = Column(String, nullable=True)
    plot = Column(String, nullable=True)