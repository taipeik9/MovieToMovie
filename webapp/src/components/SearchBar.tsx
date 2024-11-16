import { useEffect, useState } from "react";
import "./SearchBar.css";
import { Movie } from "../assets/types";

export const SearchBar = ({
  setResults,
  setClear,
  movies,
  clear,
}: {
  setResults: any;
  setClear: any;
  movies: Movie[];
  clear: boolean;
}) => {
  const [input, setInput] = useState("");

  useEffect(() => {
    setInput("");
    setResults([]);
    setClear(false);
  }, [clear]);

  const handleChange = async (val: string) => {
    setInput(val);
    if (val.length >= 1) {
      const filteredMovies = movies.filter((movie: Movie) =>
        movie.name.toLowerCase().includes(val.toLowerCase())
      );
      setResults(filteredMovies);
    } else {
      setResults([]);
    }
  };

  return (
    <div className="input-wrapper">
      <input
        placeholder="Type to search..."
        value={input}
        onChange={(e) => handleChange(e.target.value)}
      />
    </div>
  );
};
