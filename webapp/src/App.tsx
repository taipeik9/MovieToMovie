import "./App.css";
import { Search } from "./components/Search";

function App() {
  return (
    <div className="App">
      <div className="container">
        <div className="search-container">
          <Search />
          <Search />
        </div>
      </div>
    </div>
  );
}

export default App;
