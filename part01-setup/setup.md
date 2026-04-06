# Part 1 — Setup

We'll set up your environment **using AI from the very first step**. You'll install Cursor (an AI-powered code editor), then hand it this file and let it walk you through the rest.

---

## Step 1: Install Cursor

This is the only step you do manually.

1. Go to [cursor.com](https://cursor.com) and download the installer for your OS (Mac or Windows)
2. Install and open Cursor
3. Apply for the free student pro plan: [cursor.com/students](https://cursor.com/students)
   - Use your university email
   - Approval may take a day or two — the free tier works fine for today

---

## Step 2: Let Cursor Do the Rest

1. Open Cursor
2. Press **Cmd+L** (Mac) or **Ctrl+L** (Windows) to open the AI chat panel
3. Paste the following prompt:

> I'm setting up my environment for a university course (BUAD449 Module 3). Walk me through each step below **one at a time** — check what's already installed, install what's missing, and verify each step before moving on. Ask me before running anything. Here are the steps:
>
> 1. **Python** — Check if Python 3.10+ is installed. If not, install it (Homebrew on Mac, or guide me to python.org on Windows). Verify with `python3 --version` (Mac) or `python --version` (Windows).
>
> 2. **Git** — Check if Git is installed. If not, help me install it (Xcode CLI tools on Mac, git-scm.com on Windows). Verify with `git --version`.
>
> 3. **Clone the course repo** — Run: `cd ~/Desktop && git clone https://github.com/CH-chuan/BUAD449-AISpreadSheetModeling.git` (adjust the path for Windows: `cd %USERPROFILE%\Desktop`). Then open the cloned folder in Cursor (File → Open Folder).
>
> 4. **Create a virtual environment** — In the Cursor terminal, run `python3 -m venv .venv` (Mac) or `python -m venv .venv` (Windows), then activate it. Confirm I see `(.venv)` in my prompt.
>
> 5. **Install packages** — Run `pip install -r requirements.txt` inside the activated venv.
>
> 6. **Verify** — Run `python part01-setup/test_setup.py`. I should see all "OK" lines. If anything says MISSING, help me fix it.

4. Let Cursor guide you through each step. It will run commands in the built-in terminal and explain what's happening along the way.

---

## What You Just Did

- Installed an AI-powered code editor
- Used it to set up Python, Git, and your project — by describing what you needed in plain English
- This is exactly how we'll work for the rest of the course: **tell the AI what you want, review what it does, learn from the process**

---

## Quick Reference

**Three Cursor shortcuts to remember:**

| Action | Mac | Windows |
|---|---|---|
| Chat with AI | Cmd+L | Ctrl+L |
| Inline edit | Cmd+K | Ctrl+K |
| Composer (multi-file) | Cmd+I | Ctrl+I |

---

## Troubleshooting

If Cursor gets stuck or something goes wrong, here are common fixes:

| Problem | Fix |
|---|---|
| `python: command not found` (Mac) | Use `python3` instead, or add alias to `~/.zshrc` |
| `python is not recognized` (Windows) | Reinstall Python, check "Add to PATH" |
| `pip: command not found` (Mac) | Make sure venv is activated first. Outside venv, use `pip3` |
| `git: command not found` (Mac) | Install Xcode Command Line Tools: `xcode-select --install` |
| No `(.venv)` in prompt | Mac: run `source .venv/bin/activate`. Windows: if PowerShell blocks it, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` first |
| Cursor can't find Python | Cmd/Ctrl+Shift+P → "Python: Select Interpreter" → pick the one inside `.venv/` |

> **Tip:** You can also paste any error message directly into the Cursor chat — it's usually good at diagnosing the problem.
