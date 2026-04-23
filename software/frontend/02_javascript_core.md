---
tags:
  - software
  - frontend
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

↑ [Overview](./00_frontend_overview.md)

# JavaScript Core

## What It Is

JavaScript is single-threaded — it can only do one thing at a time. The **event loop** is the mechanism that lets it handle async operations (network calls, timers) without blocking, by queuing callbacks and running them when the main thread is free.

## Analogy

A restaurant with one chef (single thread). Orders (tasks) go on a ticket rail (call stack). When an order needs something from the supplier (async operation), the chef hands it off to the supplier and keeps cooking other tickets. When the supplier returns, the ticket goes to the pickup window (callback queue) and the chef grabs it when free.

## How It Works

```
Call Stack          Web APIs           Callback Queue
─────────────       ──────────────     ──────────────
main()          →   setTimeout(fn)  →  fn()  ← event loop picks up
fetch()         →   network call    →  callback()
```

**Promises** — represent a future value. Three states: pending → fulfilled / rejected.

```js
fetch('/api/data')
  .then(res => res.json())   // runs when fulfilled
  .catch(err => log(err))    // runs when rejected
```

**async/await** — syntactic sugar over promises. Makes async code look synchronous.

```js
async function getData() {
  const res = await fetch('/api/data')  // pauses here, doesn't block thread
  return res.json()
}
```

`await` suspends the function and yields control back to the event loop until the promise resolves.

## Example

```js
console.log('1')
setTimeout(() => console.log('3'), 0)  // queued, runs after stack is clear
console.log('2')
// Output: 1, 2, 3
```

Even with `0ms` delay, `3` logs last — the callback waits for the call stack to empty.

## Why It Matters

Misunderstanding the event loop causes bugs like "why is my data undefined?" (reading before the async call finishes). async/await makes the execution order explicit and the code readable.

---
↑ [Overview](./00_frontend_overview.md)

**Related:** [Browser Rendering](./01_browser_rendering.md), [React](./03_react.md)
**Tags:** #software #frontend
