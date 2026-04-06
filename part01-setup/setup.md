# Part 1 — Setup

Follow these steps to set up your environment for the course. We'll do this together in class.

---

## Step 1: Install Python

### Mac

Open **Terminal** (search "Terminal" in Spotlight).

Option A — Homebrew (recommended if you already have Homebrew):
```bash
brew install python
```

Option B — Download from python.org:
1. Go to https://www.python.org/downloads/
2. Download the latest 3.10+ installer for macOS
3. Run the installer with default settings

Verify:
```bash
python3 --version
```
You should see something like `Python 3.12.x`.

> **Mac note:** On macOS, the command is `python3` and `pip3`, not `python` and `pip`. If you want to type just `python`, you can add `alias python=python3` to your `~/.zshrc` file — but `python3` always works.

### Windows

1. Go to https://www.python.org/downloads/
2. Download the latest 3.10+ installer for Windows
3. **Important: check the box "Add python.exe to PATH"** before clicking Install
4. Click "Install Now"

Verify — open **Command Prompt** (search "cmd") or **PowerShell**:
```
python --version
```
You should see something like `Python 3.12.x`.

> **Windows note:** If `python --version` says "not found" after installing, you missed the PATH checkbox. Uninstall, reinstall, and check the box this time.

---

## Step 2: Install Git

### Mac

Git is usually pre-installed. Verify:
```bash
git --version
```

If not installed, macOS will prompt you to install Xcode Command Line Tools. Click "Install" and wait.

### Windows

1. Go to https://git-scm.com/download/win
2. Download and run the installer
3. Use default settings (click Next through everything)

Verify:
```
git --version
```

---

## Step 3: Install Cursor

1. Go to https://cursor.com and download the installer for your OS
2. Install and open Cursor
3. Apply for the free student pro plan: https://cursor.com/students
   - Use your university email
   - Approval may take a day or two — the free tier works fine for today

---

## Step 4: Clone the Course Repo

### Mac (Terminal)
```bash
cd ~/Desktop
git clone https://github.com/CH-chuan/BUAD449-AISpreadSheetModeling.git
```

### Windows (Command Prompt or PowerShell)
```
cd %USERPROFILE%\Desktop
git clone https://github.com/CH-chuan/BUAD449-AISpreadSheetModeling.git
```

Then open the folder in Cursor:
1. Open Cursor
2. File → Open Folder
3. Select the `BUAD449-AISpreadSheetModeling` folder on your Desktop

---

## Step 5: Install Python Packages

Open the **terminal inside Cursor** (`` Ctrl+` `` or View → Terminal).

### Mac
```bash
pip3 install -r requirements.txt
```

### Windows
```
pip install -r requirements.txt
```

---

## Step 6: Verify Everything Works

In the Cursor terminal, run:

### Mac
```bash
python3 part01-setup/test_setup.py
```

### Windows
```
python part01-setup/test_setup.py
```

You should see:
```
Python ............ OK
cvxpy ............. OK
openpyxl .......... OK

All good! You're ready for BUAD449 Module 3.
```

If any line says MISSING, raise your hand — a TA will help.

---

## Step 7: Try Cursor

1. Open any file in Cursor (try this `setup.md`)
2. Press **Cmd+L** (Mac) or **Ctrl+L** (Windows) to open the chat panel
3. Ask: *"What does this file do?"*
4. If you get an answer, Cursor is working.

**Three shortcuts to remember:**

| Action | Mac | Windows |
|---|---|---|
| Chat with AI | Cmd+L | Ctrl+L |
| Inline edit | Cmd+K | Ctrl+K |
| Composer (multi-file) | Cmd+I | Ctrl+I |

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `python: command not found` (Mac) | Use `python3` instead, or add alias to `~/.zshrc` |
| `python is not recognized` (Windows) | Reinstall Python, check "Add to PATH" |
| `pip: command not found` (Mac) | Use `pip3` instead |
| `git: command not found` (Mac) | Install Xcode Command Line Tools: `xcode-select --install` |
| Cursor can't find Python | In Cursor, Cmd/Ctrl+Shift+P → "Python: Select Interpreter" → pick your Python 3.10+ |
| `pip install` permission error | Try `pip install --user -r requirements.txt` |
