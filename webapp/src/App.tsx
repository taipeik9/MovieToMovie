import { SearchBar } from "./components/SearchBar";
import "./App.css";
import { useEffect, useState } from "react";

function App() {
  const [results, setResults] = useState([]);
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const fetchMovies = async () => {
      const response = await fetch("http://0.0.0.0:80/movies");
      const movies = await response.json();

      setMovies(movies.detail);
      console.log(movies.detail.length);
    };

    fetchMovies();
  }, []);

  return (
    <div className="App">
      <div className="search-bar-container">
        {movies.length > 0 && (
          <SearchBar setResults={setResults} movies={movies} />
        )}
        <div>Search Results</div>
      </div>
    </div>
  );
}

export default App;
