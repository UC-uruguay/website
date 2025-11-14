# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Create React App (CRA) based application using React 19.2.0 and JavaScript (ES6+).

## Development Commands

```bash
# Start development server at http://localhost:3000
npm start

# Run all tests in watch mode
npm test

# Run tests without watch mode (CI)
npm test -- --watchAll=false

# Run specific test file
npm test -- ComponentName.test.js

# Build for production (outputs to /build)
npm run build
```

## Architecture

### Application Entry Point
- `src/index.js`: Application root using `ReactDOM.createRoot()` with `<React.StrictMode>`
- `public/index.html`: HTML template with `<div id="root">` mount point

### Component Structure
- Single-page application with `App.js` as the main component
- Components use function declarations (not arrow functions)
- Each component can have co-located `.css` file and `.test.js` file

### Testing Setup
- Uses @testing-library/react (v16.3.0) with Jest
- `src/setupTests.js`: Configures `@testing-library/jest-dom` matchers
- Tests use `render()` and `screen` queries from Testing Library
- Example pattern:
  ```javascript
  import { render, screen } from '@testing-library/react';
  import Component from './Component';

  test('description', () => {
    render(<Component />);
    const element = screen.getByText(/text/i);
    expect(element).toBeInTheDocument();
  });
  ```

## Code Conventions

### Component Files
- Function components using `function ComponentName() { ... }`
- Default export at bottom: `export default ComponentName;`
- Import order: external libraries first, then local imports (assets, styles)

### Naming
- Components: `ComponentName.js` (PascalCase)
- Tests: `ComponentName.test.js`
- Styles: `ComponentName.css` or `index.css` for global styles
- Utilities: `utilityName.js` (camelCase)

### JSX/CSS
- CSS class names: `className="Component-element"` (kebab-case or PascalCase)
- External links must include `rel="noopener noreferrer"`
- Multi-line JSX attributes should be indented

### ESLint
- Uses `react-app` and `react-app/jest` extends
- Configured in `package.json` under `eslintConfig`

## Environment Variables

- Prefix all custom environment variables with `REACT_APP_`
- Use `.env.local` for local overrides (not committed)

## Build Output

- Production build creates optimized bundle in `/build`
- Static files from `/public` are copied to build root
- Assets include content hashes for cache busting
