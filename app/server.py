import json

from search import find_path, convert_path

from contextlib import asynccontextmanager
from fastapi import FastAPI

movie_data = {}


@asynccontextmanager
async def load_data(app: FastAPI):
    with open("hash-tables/tconst-to-nconst.json", "r") as f:
        movie_data["tconst_to_nconst"] = json.load(f)
    with open("hash-tables/nconst-to-tconst.json", "r") as f:
        movie_data["nconst_to_tconst"] = json.load(f)
    with open("hash-tables/tconst-to-movies.json", "r") as f:
        movie_data["tconst_to_movies"] = json.load(f)
    with open("hash-tables/nconst-to-people.json", "r") as f:
        movie_data["nconst_to_people"] = json.load(f)
    with open("hash-tables/movies-to-tconst.json", "r") as f:
        movie_data["movies_to_tconst"] = json.load(f)
    yield
    movie_data.clear()


app = FastAPI(lifespan=load_data)


@app.get("/")
async def get_path(start: str, dest: str):
    return convert_path(
        find_path(
            start_movie=movie_data["movies_to_tconst"][start],
            destination_movie=movie_data["movies_to_tconst"][dest],
            tconst_to_nconst=movie_data["tconst_to_nconst"],
            nconst_to_tconst=movie_data["nconst_to_tconst"],
        ),
        tconst_to_movies=movie_data["tconst_to_movies"],
        nconst_to_people=movie_data["nconst_to_people"],
    )
