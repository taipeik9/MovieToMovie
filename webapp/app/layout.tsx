import { theme } from "@/app/(assets)/theme";
import { ThemeProvider } from "@mui/material";
import { Outfit } from "next/font/google";

export const metadata = {
  title: "Movie to Movie Solver",
  description: "A BFS search for Movie to Movie game",
};

const outfit = Outfit({
  weight: ["300", "400", "500", "700"],
  subsets: ["latin"],
  display: "swap",
  variable: "--font-outfit",
});

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={outfit.variable} style={{ margin: 0 }}>
        <ThemeProvider theme={theme}>{children}</ThemeProvider>
      </body>
    </html>
  );
}
