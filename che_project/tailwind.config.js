/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      colors: {
        buttonGr: "#068323",
      },
    },
  },
  plugins: [require("flowbite/plugin")],
};
