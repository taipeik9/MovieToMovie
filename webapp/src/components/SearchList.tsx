import "./SearchList.css";

export const SearchList = ({
  setSelection,
  setClear,
  movies,
}: {
  setSelection: any;
  setClear: any;
  movies: string[];
}) => {
  return (
    <div className="results-list">
      {movies &&
        movies.map((movie: string) => (
          <div
            className="search-result"
            onClick={() => {
              setSelection(movie);
              setClear(true);
            }}
            key={movie}
          >
            {movie}
          </div>
        ))}
    </div>
  );
};
