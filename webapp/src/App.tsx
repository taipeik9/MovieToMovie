import React, { useEffect, useState } from "react";
import Select from "react-select";
import "./App.css";

type MoviesResponse = { detail: string[] };

const createOptions = (movies: string[]) => {
  return movies.map((movie: string) => {
    return { value: movie, label: movie };
  });
};

function App() {
  const [movies, setMovies] = useState<string[] | null>(null);

  useEffect(() => {
    const loadMovies = async () => {
      const response = await fetch("http://0.0.0.0/movies");
      const movies: MoviesResponse = await response.json();
      setMovies(movies.detail);
    };
    loadMovies();
  }, []);

  return (
    <div className="wrapper">
      <div className="container">
        <h1>Movie to Movie</h1>
        {movies && (
          <>
            <input list="data" />
            <datalist>
              {movies.map((movie) => (
                <option key={movie}>{movie}</option>
              ))}
            </datalist>
          </>
        )}
      </div>
    </div>
  );
}

export default App;
