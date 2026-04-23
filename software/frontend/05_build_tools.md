---
tags:
  - software
  - frontend
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T15:20:41
recent_editor: CLAUDE
---

↑ [Frontend Overview](./00_frontend_overview.md)

# Build Tools

## What It Is

Programs that transform your source code (TypeScript, JSX, multiple files, modern syntax) into files browsers can actually run (plain JavaScript, one or a few bundled files). The two main jobs: **bundling** (combining files) and **transpiling** (converting syntax).

## Analogy

A factory assembly line. Raw materials come in (`.ts`, `.jsx`, `node_modules`) and finished products come out (optimized `.js` files ready for the browser). The factory also minifies code (removes whitespace), resolves imports, and tree-shakes (removes unused code).

## How It Works

**Transpiling** — converts unsupported syntax to older JavaScript:

```
TypeScript / JSX  →  transpiler (esbuild, Babel)  →  plain ES5 JavaScript
```

**Bundling** — follows all `import` statements and combines everything into one (or a few) files so the browser makes fewer network requests.

**Tree shaking** — removes code that is imported but never called. Only what's used ships to the browser.

**Current tools:**

| Tool | Speed | Use case |
|------|-------|---------|
| **Vite** | Very fast (esbuild + native ESM) | Modern default for React, Vue, Svelte |
| **Webpack** | Slower, more configurable | Legacy projects, complex setups |
| **esbuild** | Fastest (written in Go) | Used inside Vite; also standalone |
| **Turbopack** | Fast (Rust) | Next.js default (replacing Webpack) |

## Example

You write:
```ts
// src/utils.ts
export const add = (a: number, b: number) => a + b
```

Vite builds it to:
```js
// dist/assets/index-abc123.js  (minified, hashed filename for cache busting)
const n=(a,b)=>a+b;
```

## Why It Matters

You never interact with the browser directly — the build tool is the bridge between what you write and what ships. Knowing what Vite or Webpack does explains why builds take time, why filenames have hashes, and why `import` works in the browser despite it being a Node.js concept.

---
↑ [Frontend Overview](./00_frontend_overview.md)

**Related:** [JavaScript Core](./02_javascript_core.md), [TypeScript](./04_typescript.md), [React](./03_react.md)
**Tags:** #software #frontend
