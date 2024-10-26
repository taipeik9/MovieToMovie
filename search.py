import json
from collections import deque

with open("movie-data.json", "r") as f:
    movie_data = json.load(f)
with open("people-data.json", "r") as f:
    people_data = json.load(f)
with open("names-data.json", "r") as f:
    names_data = json.load(f)

# Convert person_ids to strings for consistency with people_data
movie_to_people = {
    movie: [str(entry["id"]) for entry in cast] for movie, cast in movie_data.items()
}

# Reformat people_data to have strings as keys
person_to_movies = {str(person_id): movies for person_id, movies in people_data.items()}
names = {str(person_id): names for person_id, names in names_data.items()}


def print_path(path):
    for i, name in enumerate(path):
        if i:
            print(" -> ", end="")
        if i % 2 == 0:
            print(name, end="")
        else:
            print(names_data[name], end="")
    print()


# Breadth-First Search (BFS) function to find path between movies
def find_path(start_movie, destination_movie):
    if start_movie == destination_movie:
        return [start_movie]

    queue = deque([(start_movie, [])])
    visited = set()  # To avoid re-processing nodes

    while queue:
        current_movie, path = queue.popleft()
        path = path + [current_movie]

        if current_movie == destination_movie:
            return path

        if current_movie in visited:
            continue
        visited.add(current_movie)

        for person_id in movie_to_people.get(current_movie, []):
            for next_movie in person_to_movies.get(person_id, []):
                if next_movie not in visited:
                    queue.append((next_movie, path + [person_id]))

    # If no path is found
    return None


start = "Slumdog Millionaire (2008)"
destination = "Teenage Mutant Ninja Turtles (2014)"
path = find_path(start, destination)
if path:
    print_path(path)
else:
    print("No path found.")
