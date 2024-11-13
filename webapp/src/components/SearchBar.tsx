import { useState } from "react";
import "./SearchBar.css";

export const SearchBar = ({
  setResults,
  movies,
}: {
  setResults: any;
  movies: string[];
}) => {
  // const [input, setInput] = useState("");

  const handleChange = async (val: string) => {
    if (val.length >= 1) {
      const filteredMovies = movies.filter((movie: string) =>
        movie.toLowerCase().includes(val.toLowerCase())
      );
      setResults(filteredMovies);
    } else {
      setResults([]);
    }
    // setInput(val);
  };

  return (
    <div className="input-wrapper">
      <input
        placeholder="Type to search..."
        // value={input}
        onChange={(e) => handleChange(e.target.value)}
      />
    </div>
  );
};
