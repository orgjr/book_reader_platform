/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // pega todos os templates Django
    "./core/templates/**/*.html", // se usar apps com templates internos
  ],
  darkMode: "class", // habilita dark mode via classe 'dark'
  theme: {
    extend: {}, // aqui você adiciona cores, fontes etc
  },
  plugins: [],
};
