"use client";
import { createTheme } from "@mui/material";

export const theme = createTheme({
  palette: {
    primary: { main: "#03210b" },
  },
  typography: {
    fontFamily: "var(--font-outfit)",
    h1: {
      fontSize: "3em",
      fontWeight: 500,
    },
    h2: {
      fontSize: "2em",
      fontWeight: 400,
    },
    h3: {
      fontSize: "1em",
      fontWeight: 300,
    },
  },
});
