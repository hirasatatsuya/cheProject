/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./che_project_app/templates/**/*.html",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("flowbite/plugin")],
};
