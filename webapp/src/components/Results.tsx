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
          <div key={item.id} className="result-item-container">
            <img className="result-image" src={item.url} />
            <div>{item.name}</div>
          </div>
        )
      )}
    </div>
  );
};
