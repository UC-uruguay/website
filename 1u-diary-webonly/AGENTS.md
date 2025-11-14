# Repository Guidelines

This project hosts the web-only Astro build of the 1U Diary experience. Use the practices below to keep the site maintainable and aligned with live production look and feel.

## Project Structure & Module Organization
Keep Astro source inside `src/`. Place routed pages in `src/pages/`, reusable UI in `src/components/`, long-form content or data in `src/content/`, and shared styling in `src/styles/`. Static assets (fonts, images, favicon) belong in `public/`; anything generated at build time goes to `dist/` and should never be committed. Add helper scripts (e.g., content sync, image processing) under `scripts/` with clear CLI usage in file headers.

## Architecture & Layout Rules
Mirror the WordPress production layout: hero banner without the "Home" title, the About Me split layout with logo-only social links, Travel & Culture paired with Inspirations, three-card Recent Posts with 120×120 thumbnails, four-tile Gallery & Interests grid, and the simplified footer quote. Treat these as non-negotiable sections—update copy and assets freely, but preserve order, spacing, and semantics.

## Build, Test, and Development Commands
Run `npm install` once per machine. Use `npm run dev` for the local server, `npm run build` for a production bundle, and `npm run preview` to verify the generated `dist/`. Execute `npm run astro check` before every PR to catch type and accessibility issues.

## Coding Style & Naming Conventions
Use TypeScript in frontmatter blocks and utility modules; prefer `PascalCase` filenames for Astro components and `kebab-case` for routes. Stick to two-space indentation in templates and scripts. Name CSS classes with `block__element--modifier` semantics and co-locate critical styles with components. Import shared colors, spacing, and gradients from `src/styles/tokens.css` to avoid hard-coded values.

## Testing Guidelines
Author component snapshots with Playwright or Storybook-driven tests under `src/tests/` and run them via `npm run test` (wire this to Playwright). For any data transformers, create Vitest suites in `src/tests/unit/` and enforce coverage thresholds of 80% statements/branches. Gate merges on a green CI run covering `npm run astro check`, `npm run lint`, and `npm run test`.

## Commit & Pull Request Guidelines
Follow a conventional commits style: `feat(home): add hero gradient animation`. Keep subject lines ≤72 characters and body paragraphs wrapped at 100 characters. Each PR should describe the user-facing change, list testing commands executed, and attach before/after screenshots for visual updates. Link to tracking issues or Notion tasks, and request review from both a designer and an implementer when layout shifts might affect the locked homepage structure.
