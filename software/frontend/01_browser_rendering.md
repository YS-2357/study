---
tags:
  - software
  - frontend
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

↑ [Overview](./00_frontend_overview.md)

# Browser Rendering

## What It Is

The pipeline a browser runs every time it turns HTML, CSS, and JavaScript into pixels on screen. It has five sequential stages: parse → style → layout → paint → composite. ([MDN](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Critical_rendering_path))

## Analogy

Building a house from blueprints. The HTML is the blueprint (structure), CSS is the interior design spec (style), and the browser is the construction crew that builds the house (layout), paints the walls (paint), and furnishes each room independently (composite).

## How It Works

```
HTML → DOM
CSS  → CSSOM
         ↓
    Render Tree (DOM + CSSOM combined)
         ↓
    Layout  — calculates size and position of every element
         ↓
    Paint   — fills pixels: colors, borders, shadows
         ↓
    Composite — layers drawn in correct order on screen
```

**CSS is render-blocking** — the browser stops rendering until all CSS is downloaded and parsed. JavaScript is also render-blocking unless marked `async` or `defer`.

**Not all changes cost the same:**

| Change | Triggers |
|--------|---------|
| `width`, `margin` | Layout + Paint + Composite (most expensive) |
| `color`, `background` | Paint + Composite |
| `transform`, `opacity` | Composite only (cheapest — GPU-accelerated) |

## Example

You change `left: 100px` on a moving element. The browser re-runs layout for that element and everything affected by it, repaints, then composites — every frame, 60 times per second.

Replace with `transform: translateX(100px)` — now only composite runs. Same visual result, no layout or paint cost.

## Why It Matters

Understanding the pipeline tells you why some CSS animations are smooth (composite-only) and others cause jank (trigger layout). The rule: animate `transform` and `opacity`, never `width` or `top`.

---
↑ [Overview](./00_frontend_overview.md)

**Related:** [JavaScript Core](./02_javascript_core.md), [Build Tools](./05_build_tools.md)
**Tags:** #software #frontend
