import os
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

OMDB_API_URL = "https://www.omdbapi.com/"


GENERIC_QUERIES = [
    "the", "man", "love", "war", "life", "dark", "blood",
    "night", "fire", "lost", "star", "dead", "city", "time",
    "world", "last", "new", "old", "big", "little", "secret",
    "black", "white", "red", "blue", "green", "gold", "silver"
]