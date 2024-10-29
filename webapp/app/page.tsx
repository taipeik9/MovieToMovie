import { Autocomplete, Container, Typography } from "@mui/material";

export default async function Home() {
  const response = await fetch("http://0.0.0.0/movies", {
    cache: "no-store",
  });
  const movieTitles = response.json();

  return (
    <Container>
      <Typography variant="h1">Movie to Movie Solver</Typography>

      {/* <Autocomplete></Autocomplete> */}
    </Container>
  );
}
