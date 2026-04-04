# WSL Terminal and VS Code Workflow

## What It Is

WSL is a Linux terminal environment on Windows, and VS Code is the editor you use to browse and edit repo files visually. The usual workflow is to run navigation and Git commands in WSL, then open the same folder in VS Code.

## How It Works

### Shell, Command, and Argument

The **shell** is the program that reads what you type in the terminal and runs it. In WSL that shell is usually `bash`.

A **command** is the program or shell built-in you ask `bash` to run, and an **argument** is extra input you pass to that command.

```bash
ls git
```

In that example, `ls` is the command and `git` is the argument. Because the current folder is `/home/ys2357/study`, `git` refers to `/home/ys2357/study/git`.

### Commands You Use Most Often

| Command | What it does | When to use |
|---------|--------------|-------------|
| `pwd` | Prints your current folder path | When you need to confirm where you are |
| `ls` | Lists files and folders in the current folder | When you want to see what is here |
| `ls -la` | Lists all files, including hidden ones like `.gitignore` | When a file starts with `.` or you need permissions/timestamps |
| `cd <folder>` | Moves into a folder | When you want to open a subdirectory |
| `cd ..` | Moves up one folder | When you want to go back to the parent directory |
| `code .` | Opens the current folder in VS Code | When you want to inspect or edit files in the VS Code UI |
| `cat <file>` | Prints the whole file | When the file is short and you want to read all of it |
| `head -n 5 <file>` | Prints the first 5 lines of a file | When you only want the top of a file |
| `tail -n 5 <file>` | Prints the last 5 lines of a file | When you only want the bottom of a file |
| `sed -n '1,120p' <file>` | Prints the first 120 lines of a text file | When you want to read a Markdown note safely in terminal |
| `rg "text" .` | Searches for text under the current folder | When you want to find where a concept or command is documented |
| `rg --files` | Lists files quickly | When you want a fast file inventory |
| `ls -l <file>` | Shows one file's permissions, owner, size, and modified time | When you want to inspect file metadata |
| `file <file>` | Shows the file type and text encoding | When you want to confirm whether a file is UTF-8 text, PNG, etc. |
| `wc -l <file>` | Counts how many lines a file has | When you want a quick file length check |
| `clear` | Clears terminal output | When the screen is crowded |

### Practical Workflow

1. Run `pwd` to confirm you are in `/home/ys2357/study`.
2. Run `ls` or `ls -la` to inspect the current folder.
3. Use `cd computing`, `cd git`, or `cd ..` to move around the repo.
4. Run `code .` from the folder you want to inspect in VS Code.
5. Use `cat README.md` for a short file, `head -n 5 README.md` for the first lines, `tail -n 5 README.md` for the last lines, `sed -n '1,120p' README.md` for a line range, or `rg "command" .` to search across notes.

### WSL and Windows Path Tip

Inside WSL, use Linux paths like `/home/ys2357/study`. If you need to access a Windows file, it usually appears under `/mnt/c/...`, but for this repo you should stay in the WSL copy under `/home/ys2357/study` so terminal commands and Git operate on the same files VS Code opens.

### Reading `ls -la` Permissions

`ls -la` prints a permission string like `drwxr-xr-x` or `-rw-r--r--`.

The first character is the file type:

| Head character | Meaning |
|----------------|---------|
| `-` | Regular file |
| `d` | Directory |
| `l` | Symbolic link |
| `c` | Character device |
| `b` | Block device |
| `p` | Named pipe |
| `s` | Socket |

The next nine characters are three `rwx` groups:

```bash
rwx rwx rwx
```

- First group = owner permissions
- Second group = group permissions
- Third group = others permissions

`r` means read, `w` means write, and `x` means execute. For a file, execute means "run this file as a program/script." For a directory, execute means "enter or traverse this folder with `cd`."

Examples:

| Permission string | Meaning |
|-------------------|---------|
| `drwxrwxrwx` | Directory, everyone can read/write/enter |
| `-rwxrwxrwx` | File, everyone can read/write/execute |
| `-rw-r--r--` | File, owner can read/write, group and others can read only |
| `-rwxr-x---` | File, owner can read/write/execute, group can read/execute, others have no access |

### Text Encoding

`file README.md` may print `Unicode text, UTF-8 text`.

Unicode is the character set that includes English, Korean, and many other scripts. UTF-8 is one encoding format for storing Unicode text as bytes, so UTF-8 text can store Korean correctly.

### `cat` vs `head` vs `tail` vs `sed`

| Command | Meaning |
|---------|---------|
| `cat git/README.md` | Print the whole file |
| `head -n 5 git/README.md` | Print the first 5 lines |
| `tail -n 5 git/README.md` | Print the last 5 lines |
| `sed -n '1,40p' git/README.md` | Print lines 1 through 40 only |

Use `cat` for short files. Use `head`, `tail`, or `sed -n` when the file may be long or you only need part of it.

### Why Errors Happen

| Error example | What caused it | Fix |
|---------------|----------------|-----|
| `psd` → `command not found` | Typo in the command name | Use `pwd` |
| `cd git ** ls` → `cd: too many arguments` | Wrong connector; `**` is not the shell operator for "then run next command" | Use `cd git && ls` |
| `ls -l REAMDE.md` → `No such file or directory` | Filename typo or wrong path | Use `ls -l README.md` |
| `wc -l READM.md` → `No such file or directory` | Filename typo or wrong path | Use `wc -l README.md` |
| `git diff ...` prints nothing | No matching changes to show | Not always an error; check `git status` |

## Example

Open this repo in VS Code from WSL and inspect the Git notes:

```bash
cd /home/ys2357/study
pwd
ls
code .
cd git
ls
cat README.md
head -n 5 README.md
tail -n 5 README.md
sed -n '1,120p' 01_tracking_and_status.md
ls -l README.md
file README.md
wc -l README.md
```

## Why It Matters

If you can reliably answer "where am I?", "what files are here?", and "how do I open this folder in VS Code?", then WSL stops feeling confusing and repo navigation becomes routine. That also makes the [Git workflow](../git/02_daily_git_workflow.md) much easier because you are always running commands from the correct folder.

> **Tip:** Start every terminal session with `cd /home/ys2357/study && pwd` before running Git commands.

---
← Previous: [Endpoints](08_endpoints.md) | [Overview](00_overview.md) | Next: [Vim and Neovim](10_vim_and_neovim.md) →
