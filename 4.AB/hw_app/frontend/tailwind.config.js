/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js}",
    "./templates/**/*.{html,js}",
    "node_modules/preline/dist/*.js"
  ],
  theme: {
    fontFamily: {
      display: ['"Exo 2"', "sans-serif"],
      body: ['"Alegreya Sans"', "sans-serif"],
    },
    colors: {
      "my-dark": {
        DEFAULT: "#222831",
        100: "#1f242c",
        200: "#1b2027",
        300: "#181c22",
        400: "#14181d",
        500: "#111419",
        600: "#0e1014",
        700: "#0a0c0f",
        800: "#07080a",
        900: "#030405",
      },
      "my-gray": {
        DEFAULT: "#393e46",
        100: "#33383f",
        200: "#2e3238",
        300: "#282b31",
        400: "#22252a",
        500: "#1d1f23",
        600: "#17191c",
        700: "#111315",
        800: "#0b0c0e",
        900: "#060607",
      },
      "my-light": {
        DEFAULT: "#eeeeee",
        100: "#d6d6d6",
        200: "#bebebe",
        300: "#a7a7a7",
        400: "#8f8f8f",
        500: "#777777",
        600: "#5f5f5f",
        700: "#474747",
        800: "#303030",
        900: "#181818",
      },
      "my-yellow": {
        DEFAULT: "#ffd369",
        100: "#e6be5f",
        200: "#cca954",
        300: "#b3944a",
        400: "#997f3f",
        500: "#806a35",
        600: "#66542a",
        700: "#4c3f1f",
        800: "#332a15",
        900: "#19150a",
      },
    },
    extend: {},
  },
  plugins: [
    require('preline/plugin')
  ],
};
