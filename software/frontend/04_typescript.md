---
tags:
  - software
  - frontend
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

↑ [Overview](./00_frontend_overview.md)

# TypeScript

## What It Is

A superset of JavaScript that adds a static type system. TypeScript code compiles down to plain JavaScript — browsers never see TypeScript directly. The type checker catches errors at write time, before the code runs.

## Analogy

Spell-check for code. JavaScript lets you pass anything anywhere and only crashes at runtime. TypeScript highlights the mistake immediately in your editor — like spell-check flagging a typo before you send the email.

## How It Works

You annotate variables, function parameters, and return values with types:

```ts
function add(a: number, b: number): number {
  return a + b
}

add(1, '2')  // ✗ Error: Argument of type 'string' is not assignable to 'number'
```

**Interface** — describes the shape of an object:

```ts
interface User {
  id: number
  name: string
  email?: string  // optional
}
```

**Generics** — write logic that works across types:

```ts
function first<T>(arr: T[]): T {
  return arr[0]
}
first([1, 2, 3])    // returns number
first(['a', 'b'])   // returns string
```

TypeScript is erased at compile time — the output is plain `.js`.

## Example

Without TypeScript, this bug only appears at runtime:

```js
const user = { name: 'Alice' }
console.log(user.email.toLowerCase())  // TypeError at runtime
```

With TypeScript, the error appears in the editor before you run anything:

```ts
const user: User = { name: 'Alice' }  // email is optional
console.log(user.email.toLowerCase())  // ✗ Error: user.email is possibly undefined
```

## Why It Matters

TypeScript eliminates an entire class of runtime bugs in large codebases. It's now the default for React, Node.js, and most modern frontend projects — understanding it is a prerequisite for reading most open-source JavaScript.

---
↑ [Overview](./00_frontend_overview.md)

**Related:** [JavaScript Core](./02_javascript_core.md), [React](./03_react.md)
**Tags:** #software #frontend
