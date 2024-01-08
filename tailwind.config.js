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
        'kadwa-bold': ['Kadwa', 'serif'],
        'kadwa': ['kadwaregular', 'serif'],
      },
      boxShadow: {
        'signature': '14px 14px blue',
      },
      colors: {
        'blue': '#032DC2',
      },
      borderRadius: {
        'default': '4px',
      },
    },
  },
  plugins: [],
}

