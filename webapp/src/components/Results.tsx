import "./Results.css";

export const Results = ({
  solution,
}: {
  solution: { order: number; id: string; name: string; url: string }[];
}) => {
  return (
    <div className="results-container">
      {solution.map(
        (item: { order: number; id: string; name: string; url: string }) => (
          <div className="result-item-container">
            <img className="result-image" key={item.url} src={item.url} />
            <div key={item.id}>{item.name}</div>
          </div>
        )
      )}
    </div>
  );
};
