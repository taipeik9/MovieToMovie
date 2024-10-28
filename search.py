import json
from typing import Union

from collections import deque

with open("hash-tables/tconst-to-nconst.json", "r") as f:
    tconst_to_nconst = json.load(f)
with open("hash-tables/nconst-to-tconst.json", "r") as f:
    nconst_to_tconst = json.load(f)
with open("hash-tables/tconst-to-movies.json", "r") as f:
    tconst_to_movies = json.load(f)
with open("hash-tables/nconst-to-people.json", "r") as f:
    nconst_to_people = json.load(f)
with open("hash-tables/movies-to-tconst.json", "r") as f:
    movies_to_tconst = json.load(f)


def print_path(path):
    if path:
        for i, id in enumerate(path):
            if i:
                print(" -> ", end="")
            if i % 2 == 0:
                print(tconst_to_movies.get(id, ""), end="")
            else:
                print(nconst_to_people.get(id, ""), end="")


def find_path(start_movie: str, destination_movie: str) -> Union[None, list[str]]:
    if start_movie == destination_movie:
        return [start_movie]

    visited = set()
    queue = deque([(start_movie, [])])

    while queue:
        current, path = queue.popleft()
        path = path + [current]

        if current == destination_movie:
            return path

        if current in visited:
            continue

        visited.add(current)
        for nconst in tconst_to_nconst.get(current, []):
            for next_tconst in nconst_to_tconst.get(nconst, []):
                if next_tconst not in visited:
                    queue.append(((next_tconst), path + [nconst]))
    # No path was found
    return None


start = "The Shining (1980)"
destination = "I Know What You Did Last Summer (1997)"

path = find_path(movies_to_tconst[start], movies_to_tconst[destination])
print_path(path)
