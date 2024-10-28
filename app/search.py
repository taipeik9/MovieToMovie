from typing import Union

from collections import deque


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
    start_movie: str,
    destination_movie: str,
    tconst_to_nconst: dict[str],
    nconst_to_tconst: dict[str],
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
        for nconst in tconst_to_nconst.get(current, []):
            for next_tconst in nconst_to_tconst.get(nconst, []):
                if next_tconst not in visited:
                    queue.append(((next_tconst), path + [nconst]))
    # No path was found
    return None
