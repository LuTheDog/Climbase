/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.{html,js}"],
  theme: {
    extend: {
      colors: {
        'secondary': '#1f487e',
        'primary': '#acd9ec',
        'navbar-primary': '#1d3461',
        'background-primary': '#d7d7d7'
      },
    },
  },
  plugins: [],
}
