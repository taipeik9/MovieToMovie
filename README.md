# Movie-to-Movie Speedrunner

Version  1.0 

Solver for movie-to-movie online game -> https://movietomovie.com/

## What it does

This app finds the shortest possible path between two movies connecting through cast members. Its based on the movietomovie game linked above^. 

**Pattern:**

movie -> cast member -> movie -> cast member -> movie

**Example:** (Reservoir Dogs to Finding Nemo)

Reservoir Dogs -> Harvey Keitel -> The Last Temptation of Christ -> Willem Dafoe -> Finding Nemo

## What the solver looks like

![app-demonstration](./readme-assets/demo.gif)

## How to use it

Below you will find instructions on how to run the app.

### API

Ensure that you have python installed and I also recommend creating a virtual environment before installing the packages.

1. Navigate to the app folder `cd app`
2. Activate your virtual environment (I personally use anaconda)
3. Install the python packages in requirements.txt `pip install -r requirements.txt`
4. Run `uvicorn server:app --host 0.0.0.0 --port 80`

*Note:* If you want to use the webapp, ensure that the host and port flags are included in this execute^.

### Web app

Ensure that you have npm (Node Package Manager) installed.

1. Navigate to the webapp folder `cd webapp`
2. Install the dependencies `npm install`
3. Spin up the server `npm run dev`
4. Navigate to  http://localhost:5173/

## How it works

The webapp takes user input and filters through all of the possible movies. When a user clicks on the movie title it gets saved into the React state and then when a user clicks submit, the start and destination movie titles are sent to the back end. The back end converts the movie titles into their respective ids and then conducts a Breadth First Search (BFS) on the adjacency matrix that was built using the publicly available imdb data. The structure of the adjacency matrix is: movie name: [array of cast members] and person: [array of movies they are in]. The shortest path is found and then sent back to the front end where it is displayed.

If you are interested in the data cleaning and the graph set up, all of it is in the movie-db-testing.ipynb python notebook. Warning, you will need to download the imdb dataset to run this notebook, and there are some blocks in there that will take a pretty long time to run as its working with a ton of data. (skip over the tmdb dataset, I don't use it in the final version)

## Routes

The webapp only has one route, its the root "/". This is the single page application.

*API Routes*

**GET:** /

This route runs the solver and takes a starting movie and destination movie as query parameters. The param names are "start" and "dest".

ex. usage:

http://0.0.0.0/?start=Mr.%20%26%20Mrs.%20Smith%20(1941)&dest=on%20the%20line%20(2022)

**GET:** /movies/

This route returns the full list of available movies along with their respective ids, also referred to as "tconst".

ex. usage:

http://0.0.0.0/movies/

**GET:** /images/[image-id]

This route returns the url for the imdb image for a movie or cast member. image-id refers to the movie or cast member's id (tconst/nconst).

ex. usage:

http://0.0.0.0/image/tt8949056

## Limitations and looking forward

- Right now the data is static. There is no efficient way to update the data. I would love to further develop it so that you can run a python script that will download the latest imdb data, update the datasets, and then scrape all of the new photos needed.

- I used number of ratings to determine which movies to include in the dataset, however, I forgot to account for the year. Movies that are newer, that should be considered valid may be under the review threshold, so that needs to be corrected.

- Sometimes it won't find the exact shortest path. This limitation is out of my control. The publicly available imdb data does not really include every single cast member. Some of the lesser known cast members are omitted. However, this is not the case for movie-to-movie. They include every single cast member so sometimes the solver may take one or two more edges to get to the goal. 

- It also sometimes finds a path that is impossible on movie-to-movie. I ran into this issue when it included a movie that a person was in but the movie was animated. So, for some reason, it wasn't included in their movie list on movie-to-movie. I may add an option to get the next found path in the BFS, so if the path is wrong, then the user can just find the next best path (which may be of equivalent distance). Or maybe it could exclude cast members / movies? Not sure yet, this addition seems a bit ambitious.