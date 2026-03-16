import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://xvadur.com",
  compressHTML: true,
  build: {
    inlineStylesheets: "auto",
  },
});
