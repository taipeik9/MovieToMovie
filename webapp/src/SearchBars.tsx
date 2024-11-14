import { SearchBar } from "./components/SearchBar";
import { useEffect, useState } from "react";
import { SearchList } from "./components/SearchList";

export const SearchBars = () => {
  const [results, setResults] = useState([]);
  const [movies, setMovies] = useState([]);
  const [selection, setSelection] = useState("");
  const [clear, setClear] = useState(false);

  useEffect(() => {
    const fetchMovies = async () => {
      const response = await fetch("http://0.0.0.0:80/movies");
      const moviesObj = await response.json();

      setMovies(moviesObj.detail);
    };

    fetchMovies();
  }, []);

  return (
    <div className="search-bar-container">
      {movies.length > 0 && (
        <SearchBar
          setResults={setResults}
          setClear={setClear}
          movies={movies}
          clear={clear}
        />
      )}
      <SearchList
        movies={results}
        setSelection={setSelection}
        setClear={setClear}
      />
      <div>{selection}</div>
    </div>
  );
};
