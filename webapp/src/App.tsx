import { useEffect, useState } from "react";
import "./App.css";
import { Search } from "./components/Search";
import { SearchButton } from "./components/SearchButton";
import { Results } from "./components/Results";

function App() {
  const [searching, setSearching] = useState(false);
  const [start, setStart] = useState("");
  const [dest, setDest] = useState("");
  const [solution, setSolution] = useState([]);

  useEffect(() => {
    if (searching) {
      const getPath = async (start: string, dest: string) => {
        const response = await fetch(
          `http://0.0.0.0:80/?start=${encodeURIComponent(
            start
          )}&dest=${encodeURIComponent(dest)}`
        );
        const sol = await response.json();
        setSolution(sol.detail);
      };
      getPath(start, dest);
      setSearching(false);
    }
  }, [searching]);

  return (
    <div className="App">
      <div className="container">
        <h1>Movie to Movie Solver</h1>
        <div className="search-container">
          <Search setSelection={setStart} />
          <Search setSelection={setDest} />
        </div>
        {start} ---- {dest}
        <SearchButton onClick={() => setSearching(true)} />
        {solution && <Results solution={solution} />}
      </div>
    </div>
  );
}

export default App;
