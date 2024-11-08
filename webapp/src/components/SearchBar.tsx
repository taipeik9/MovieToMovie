import { useState } from "react";
import "./SearchBar.css";

export const SearchBar = ({ setResults }: { setResults: any }) => {
  const [input, setInput] = useState("");

  const fetchMovies = async (val: string) => {
    const response = await fetch("http://0.0.0.0:80/movies");
    const movies = await response.json();

    const filteredMovies = movies.detail;
    setResults(movies.detail);
  };

  const handleChange = async (val: string) => {
    fetchMovies(val);
    setInput(val);
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
