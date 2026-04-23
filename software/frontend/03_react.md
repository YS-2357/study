---
tags:
  - software
  - frontend
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T15:20:41
recent_editor: CLAUDE
---

↑ [Frontend Overview](./00_frontend_overview.md)

# React

## What It Is

A JavaScript library for building UIs out of **components** — reusable functions that take data (props) in and return HTML-like output (JSX). React keeps the UI in sync with data automatically via a **virtual DOM** diffing algorithm.

## Analogy

LEGO bricks. Each component is a brick with a specific shape (structure) and color (data). You snap bricks together to build complex UIs. When you change a brick's color (state), only that brick and anything connected to it updates — not the whole model.

## How It Works

**Component** — a function that returns JSX:

```jsx
function Button({ label, onClick }) {
  return <button onClick={onClick}>{label}</button>
}
```

**Props** — data passed in from parent, read-only.

**State** — data that lives inside a component. When state changes, React re-renders the component.

```jsx
function Counter() {
  const [count, setCount] = useState(0)
  return <button onClick={() => setCount(count + 1)}>{count}</button>
}
```

**Virtual DOM** — React keeps a lightweight copy of the DOM in memory. On state change, it diffs the new virtual DOM against the old one and applies only the minimal real DOM changes needed.

```
State change → new Virtual DOM → diff vs old → patch real DOM
```

## Example

A search input that filters a list:

```jsx
function Search({ items }) {
  const [query, setQuery] = useState('')
  const filtered = items.filter(i => i.includes(query))
  return (
    <>
      <input onChange={e => setQuery(e.target.value)} />
      {filtered.map(i => <div key={i}>{i}</div>)}
    </>
  )
}
```

Every keystroke updates `query` → React re-renders → filtered list updates.

## Why It Matters

React's component model makes large UIs maintainable — each piece is isolated, testable, and reusable. It dominates frontend hiring and is the default choice for SPAs, dashboards, and AI-facing UIs.

---
↑ [Frontend Overview](./00_frontend_overview.md)

**Related:** [JavaScript Core](./02_javascript_core.md), [TypeScript](./04_typescript.md), [Build Tools](./05_build_tools.md)
**Tags:** #software #frontend
