/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        'yinmn-blue': '#3d5a80',
        'powder-blue': '#98c1d9',
        'light-cyan': '#e0fbfc',
        'burnt-sienna': '#ee6c4d',
        'gunmetal': '#293241'
      }
    },
  },
  plugins: [
    require('prettier-plugin-tailwindcss'),
    require('@tailwindcss/forms')
  ],
}
