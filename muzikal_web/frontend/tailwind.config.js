/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors');

module.exports = {
  content: [
    "./src/**/*.{html,js}",
    "./templates/**/*.{html,js}"
  ],
  theme: {
    extend: {

    },
    colors: {
      'red': '#941B0C',
      'dark-red': '#621708',
      'dark-brown': '#220901',
      'yellow': '#F6AA1C',
      'orange': '#BC3908',
      'random': '#ddf6fe',
      transparent: 'transparent',
      current: 'currentColor',
      black: colors.black,
      white: colors.white,
      gray: colors.slate,
      green: colors.emerald,
      purple: colors.violet,
      pink: colors.fuchsia,
    },
    fontFamily: {
      'title': ['Cinzel', 'sans-serif'],
      'text': ['Old Standard TT', 'serif'],
      'goth': ['Old London', 'serif']
    }
  },
  plugins: [],
}