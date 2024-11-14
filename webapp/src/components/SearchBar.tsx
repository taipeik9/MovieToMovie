import { useEffect, useState } from "react";
import "./SearchBar.css";

export const SearchBar = ({
  setResults,
  setClear,
  movies,
  clear,
}: {
  setResults: any;
  setClear: any;
  movies: string[];
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
      const filteredMovies = movies.filter((movie: string) =>
        movie.toLowerCase().includes(val.toLowerCase())
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
