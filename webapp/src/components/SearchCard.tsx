import { useEffect, useState } from "react";
import { Movie } from "../assets/types";
import "./SearchCard.css";

export const SearchCard = ({ movie }: { movie: Movie | null }) => {
  const [url, setUrl] = useState("");

  useEffect(() => {
    const getImage = async (movie: Movie) => {
      const response = await fetch(`http://0.0.0.0:80/image/${movie.id}/`);
      const url = await response.json();

      setUrl(url.detail);
    };
    if (movie) getImage(movie);
  }, [movie]);

  return (
    <>
      {movie && (
        <div className="search-card">
          <img className="search-card-image" src={url} />
          {movie.name}
        </div>
      )}
    </>
  );
};
