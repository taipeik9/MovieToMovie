import { SearchBar } from "./components/SearchBar";
import "./App.css";
import { useState } from "react";

function App() {
  const [results, setResults] = useState([]);

  return (
    <div className="App">
      <div className="search-bar-container">
        <SearchBar setResults={setResults} />
        <div>Search Results</div>
      </div>
    </div>
  );
}

export default App;
