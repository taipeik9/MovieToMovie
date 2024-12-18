import { Movie } from "../assets/types";
import "./SearchButton.css";

export const SearchButton = ({
  onClick,
  start,
  dest,
}: {
  onClick: Function;
  start: Movie | null;
  dest: Movie | null;
}) => {
  return (
    <button
      className="search-button"
      onClick={() => onClick()}
      disabled={!start || !dest}
    >
      Search
    </button>
  );
};
