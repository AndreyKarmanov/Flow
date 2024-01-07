/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../**/templates/**/*.html',
  ],
  theme: {
    extend: {
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic':
          'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
      },
      fontFamily: {
        'kadwa-bold': ['kadwabold', 'serif'],
        'kadwa': ['kadwaregular', 'serif'],
      },
    },
  },
  plugins: [],
}

