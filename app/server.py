import json

from search import time_find_path, convert_path

from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
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
    with open("hash-tables/images.json", "r") as f:
        movie_data["images"] = json.load(f)
    movie_data["list"] = sorted(
        [
            {"id": movie_data["movies_to_tconst"][key], "name": key}
            for key in movie_data["movies_to_tconst"]
        ],
        key=lambda x: x["name"],
    )
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
        start_movie=movie_data["movies_to_tconst"].get(start.lower(), None),
        destination_movie=movie_data["movies_to_tconst"].get(dest.lower(), None),
        graph=movie_data["graph"],
    )

    return {
        "traversalTime": time,
        "detail": convert_path(
            path, ids_to_text=movie_data["ids_to_text"], urls=movie_data["images"]
        ),
    }


@app.get("/movies/")
async def get_movie_titles():
    return {"detail": movie_data["list"]}


@app.get("/image/{id}")
async def get_images(id: str):
    if id not in movie_data["images"].keys():
        raise HTTPException(status_code=404, detail="id not found")
    return {"detail": movie_data["images"][id]}
