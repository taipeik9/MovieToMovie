import "./SearchButton.css";

export const SearchButton = ({ onClick }: { onClick: Function }) => {
  return (
    <button className="search-button" onClick={() => onClick()}>
      Search
    </button>
  );
};
