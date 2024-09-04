module.exports = {
  env: {
    browser: true,
    es2021: true,
  },
  extends: [
    'eslint:recommended',
    'plugin:vue/vue3-essential',
    'airbnb-base',
  ],
  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'module',
  },
  rules: {
    semi: ['error', 'always'], // Enforce semicolons
    'max-len': ['error', { code: 120 }], // Increased max line length to 120 characters
    'vue/multi-word-component-names': 'off', // Disabled multi-word component names rule
    'no-new': 'off', // Disabled no-new rule
    'no-multi-spaces': 'off',
  },
};
