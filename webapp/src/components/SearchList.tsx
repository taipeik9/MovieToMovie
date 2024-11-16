import "./SearchList.css";

export const SearchList = ({
  setSelection,
  setClear,
  movies,
}: {
  setSelection: any;
  setClear: any;
  movies: { id: string; name: string }[];
}) => {
  return (
    <div className="results-list">
      {movies &&
        movies.map((movie: { id: string; name: string }) => (
          <div
            className="search-result"
            onClick={() => {
              setSelection(movie.name);
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
