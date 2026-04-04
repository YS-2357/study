# Vim and Neovim

## What It Is

Vim and Neovim are terminal-based text editors that use modal editing: the same keys mean different things depending on whether you are inserting text or issuing edit/navigation commands. Vim is the long-established classic editor, and Neovim is a modern fork focused on better extensibility and development tooling.

## Analogy

VS Code is like editing with visible menus and buttons, while Vim/Neovim are like editing with keyboard shortcuts as the main control surface. That is slower to learn at first, but faster once the key motions become familiar.

## How It Works

### Core Editing Model

Vim and Neovim switch between modes instead of treating every keypress as plain text input.

| Mode | What it does | Common entry |
|------|--------------|--------------|
| Normal mode | Move, delete, copy, paste, search, and run editor commands | Press `Esc` |
| Insert mode | Type text into the file | Press `i` in Normal mode |
| Command-line mode | Save, quit, and run `:` commands | Type `:` in Normal mode |
| Visual mode | Select text ranges | Press `v` in Normal mode |

That means `j` may move the cursor down in Normal mode, but insert the letter `j` in Insert mode.

### Feasibility In WSL

Vim and Neovim are highly feasible in WSL because they run directly in the terminal where you already use `cd`, `git`, and `rg`. They also work naturally over SSH on remote Linux machines, which is useful for cloud and server work.

The main feasibility cost is learning and configuration:

- Vim is often already installed and works immediately with little setup.
- Neovim may need installation, and its plugin/LSP ecosystem is stronger but adds more config decisions.
- For a Markdown study repo, a minimal Vim or Neovim setup is usually enough; a heavy IDE-like Neovim setup is optional, not required.

### Vim vs Neovim

| Editor | Strengths | Tradeoffs |
|--------|-----------|-----------|
| Vim | Mature, stable, widely available by default, excellent for terminal and SSH editing | Older plugin/config ecosystem, less built-in modern IDE behavior |
| Neovim | Modern plugin architecture, Lua config, stronger built-in LSP/editor extensibility, better path to an IDE-like terminal editor | Not always preinstalled, faster-moving ecosystem, config can become complex |

If your priority is "edit files reliably anywhere," start with Vim basics. If your priority is "terminal-first editor that can grow into a coding environment," Neovim is usually the better long-term choice.

### Compared With Other Editors

| Tool | Best fit | Main difference from Vim/Neovim |
|------|----------|---------------------------------|
| nano | Quick beginner-friendly terminal edits | Easier to start, but far less powerful for navigation, bulk edits, and repeatable keyboard workflows |
| VS Code | Visual GUI editing, extensions, debugging, easier discoverability | Heavier and GUI-centered; less natural on bare servers and less keyboard-modal by default |
| Less / `cat` / `sed -n` | Reading files in terminal | Good for viewing text, but not designed as full interactive editors |

For this repo, Vim/Neovim sit between plain terminal viewers and VS Code: they keep you inside WSL, but give you a real editor instead of only printing file contents.

### Practical Adoption Path

If you are unsure whether to commit to Neovim, use this sequence:

1. Learn enough Vim to avoid getting stuck: `i`, `Esc`, `:w`, `:q`, `:wq`, `u`, `/text`, `n`, `dd`, `yy`, `p`.
2. Use Vim or Neovim for small Markdown edits inside this repo.
3. Keep VS Code available as a fallback while your muscle memory is still weak.
4. Only invest in Neovim plugins and LSP config after basic modal editing feels comfortable.

## Example

Open a study note in Neovim from WSL, make one edit, and save:

```bash
cd /home/ys2357/study
nvim computing/10_vim_and_neovim.md
```

Inside Neovim:

```text
/Neovim      # search for the word Neovim
n            # jump to the next match
i            # enter Insert mode and edit text
Esc          # return to Normal mode
:wq          # save and quit
```

If Neovim is not installed, `vim computing/10_vim_and_neovim.md` is the same basic workflow with classic Vim.

## Why It Matters

If you move your workflow into WSL, Vim or Neovim can become your in-terminal editor so you can navigate, inspect, edit, and commit without constantly switching back to a GUI. The tradeoff is that you only get this speed after learning modal editing, so for a Markdown-heavy study repo it is usually best to start with minimal Vim/Neovim usage and expand only if the workflow feels worthwhile.

> **Tip:** Do not begin by building a large Neovim configuration. First confirm that basic modal editing actually improves your WSL workflow for this repo.

---
← Previous: [WSL Terminal and VS Code Workflow](09_wsl_terminal_and_vscode.md) | [Overview](00_overview.md)
