"use client";
import { Autocomplete, Container, TextField, Typography } from "@mui/material";

export default async function Home() {
  const response = await fetch("http://0.0.0.0/movies", {
    cache: "no-store",
  });
  const movieTitles = await response.json();

  const renderInput = async (params: any) => {
    return <TextField {...params} label="Movie" />;
  };

  return (
    <Container>
      <Typography variant="h1">Movie to Movie Solver</Typography>

      <Autocomplete
        disablePortal
        options={movieTitles.detail}
        sx={{ width: 300 }}
        renderInput={renderInput}
      />
    </Container>
  );
}
