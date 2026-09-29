import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#f3f6ff",
          100: "#e7eeff",
          500: "#4f6df4",
          600: "#4159d8",
          900: "#0f172a",
        },
      },
      boxShadow: {
        soft: "0 10px 25px rgba(79, 109, 244, 0.15)",
      },
    },
  },
  plugins: [],
};

export default config;
