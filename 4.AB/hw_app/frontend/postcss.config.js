module.exports = {
  plugins: [
    require("postcss-import"),
    require("tailwindcss/nesting"),
    require("tailwindcss"),
    require("autoprefixer"),
    require("postcss-preset-env"),
    require("cssnano")({
      preset: "default",
    }),
  ],
};
