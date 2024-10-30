from typing import Union, Tuple
import json
import time

from collections import deque


# Purely for testing and timing
def print_path(path: list[str], ids_to_text: dict[str]):
    if path:
        for i, id in enumerate(path):
            if i:
                print(" -> ", end="")
            print(ids_to_text.get(id, ""), end="")


def convert_path(path: list[str], ids_to_text: dict[str]):
    converted_path = None
    if path:
        converted_path = []
        for id in path:
            converted_path.append(ids_to_text.get(id, ""))
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
def time_find_path(
    start_movie: str,
    destination_movie: str,
    graph: dict[set[str]],
    ids_to_text: dict[str],
) -> Tuple[list[str], float]:
    start_time = time.time()
    path = convert_path(find_path(start_movie, destination_movie, graph), ids_to_text)
    return time.time() - start_time, path


# Purely for testing and timing
if __name__ == "__main__":
    movie_data = {}
    with open("hash-tables/graph.json", "r") as f:
        movie_data["graph"] = json.load(f)
    with open("hash-tables/ids-to-text.json", "r") as f:
        movie_data["ids_to_text"] = json.load(f)
    with open("hash-tables/movies-to-tconst.json", "r") as f:
        movie_data["movies_to_tconst"] = json.load(f)

    # converting all lists to sets for more effecient traversal
    for id in movie_data["graph"]:
        movie_data["graph"][id] = set(movie_data["graph"][id])

    times = []
    for i in range(5):
        times.append(time_find_path("tt0032904", "tt1648216", movie_data["graph"]))
    print(times)

    print("Avg Time", sum(times) / len(times), "seconds over", len(times), "calls")
