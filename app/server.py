import json

from search import time_find_path

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

movie_data = {}


@asynccontextmanager
async def load_data(app: FastAPI):
    with open("hash-tables/graph.json", "r") as f:
        movie_data["graph"] = json.load(f)
    with open("hash-tables/ids-to-text.json", "r") as f:
        movie_data["ids_to_text"] = json.load(f)
    with open("hash-tables/movies-to-tconst.json", "r") as f:
        movie_data["movies_to_tconst"] = json.load(f)
    movie_data["list"] = sorted(list(movie_data["movies_to_tconst"].keys()))
    movie_data["movies_to_tconst"] = {
        k.lower(): v for k, v in movie_data["movies_to_tconst"].items()
    }

    # converting all lists to sets for more efficient traversal
    for id in movie_data["graph"]:
        movie_data["graph"][id] = set(movie_data["graph"][id])
    yield
    movie_data.clear()


app = FastAPI(lifespan=load_data)

origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get_path(start: str, dest: str):
    time, path = time_find_path(
        start_movie=movie_data["movies_to_tconst"][start.lower()],
        destination_movie=movie_data["movies_to_tconst"][dest.lower()],
        graph=movie_data["graph"],
        ids_to_text=movie_data["ids_to_text"],
    )
    return {"traversalTime": time, "detail": path}


@app.get("/movies")
async def get_movie_titles():
    return {"detail": movie_data["list"]}
