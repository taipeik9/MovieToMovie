import { Movie } from "../assets/types";
import "./SearchList.css";

export const SearchList = ({
  setSelection,
  setClear,
  movies,
}: {
  setSelection: any;
  setClear: any;
  movies: Movie[];
}) => {
  return (
    <div className="results-list">
      {movies &&
        movies.map((movie: Movie) => (
          <div
            className="search-result"
            onClick={() => {
              setSelection(movie);
              setClear(true);
            }}
            key={movie.id}
          >
            {movie.name}
          </div>
        ))}
    </div>
  );
};
