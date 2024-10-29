from typing import Union
import json
import time

from collections import deque


# Purely for testing and timing
def print_path(
    path: list[str],
    tconst_to_movies: dict[str],
    nconst_to_people: dict[str],
):
    if path:
        for i, id in enumerate(path):
            if i:
                print(" -> ", end="")
            if i % 2 == 0:
                print(tconst_to_movies.get(id, ""), end="")
            else:
                print(nconst_to_people.get(id, ""), end="")


def convert_path(
    path: list[str], tconst_to_movies: dict[str], nconst_to_people: dict[str]
):
    converted_path = None
    if path:
        converted_path = []
        for i, id in enumerate(path):
            if i % 2 == 0:
                converted_path.append(tconst_to_movies.get(id, ""))
            else:
                converted_path.append(nconst_to_people.get(id, ""))
    return converted_path


def find_path(
    start_movie: str, destination_movie: str, graph: dict[set[str]]
) -> Union[None, list[str]]:
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
        for neighbour in graph.get(current, []):
            if neighbour not in visited:
                queue.append(((neighbour), path))
    # No path was found
    return None


# Purely for testing and timing
def run_find_path(graph):
    start_time = time.time()
    find_path("tt0032904", "tt1648216", graph)
    return time.time() - start_time


# Purely for testing and timing
if __name__ == "__main__":
    movie_data = {}
    with open("hash-tables/tconst-to-nconst.json", "r") as f:
        movie_data["tconst_to_nconst"] = json.load(f)
    with open("hash-tables/nconst-to-tconst.json", "r") as f:
        movie_data["nconst_to_tconst"] = json.load(f)

    for tconst in movie_data["tconst_to_nconst"]:
        movie_data["tconst_to_nconst"][tconst] = set(
            movie_data["tconst_to_nconst"][tconst]
        )

    for nconst in movie_data["nconst_to_tconst"]:
        movie_data["nconst_to_tconst"][nconst] = set(
            movie_data["nconst_to_tconst"][nconst]
        )

    graph = {**movie_data["nconst_to_tconst"], **movie_data["tconst_to_nconst"]}

    times = []
    for i in range(5):
        times.append(run_find_path(graph))
    print(times)

    print("Avg Time", sum(times) / len(times), "seconds over", len(times), "calls")
