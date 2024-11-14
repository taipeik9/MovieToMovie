import "./SearchButton.css";

export const SearchButton = ({ onClick }: { onClick: Function }) => {
  return (
    <div>
      <button className="search-button" onClick={() => onClick()}>
        Search
      </button>
    </div>
  );
};
