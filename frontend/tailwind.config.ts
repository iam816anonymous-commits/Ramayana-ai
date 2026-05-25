import type { Config } from "tailwindcss";

export default {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
        sacred: {
          dark: "#0a0a0a",
          gold: "#d4af37",
          warm: "#fdf5e6",
          accent: "#8b4513",
        },
      },
    },
  },
  plugins: [],
} satisfies Config;
