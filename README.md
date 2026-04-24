# BUAD449 — AI-Assisted Spreadsheet Modeling

Course repository for BUAD449 Module 3, Spring 2026.

## Setup

See [part01-setup/setup.md](part01-setup/setup.md) for installation instructions.

## Quick Start

```bash
git clone https://github.com/CH-chuan/BUAD449-AISpreadSheetModeling.git
cd BUAD449-AISpreadSheetModeling
pip install -r requirements.txt
python part01-setup/test_setup.py
```

## API key (`.env`)

Any notebook that calls the OpenAI API expects the **same setup**: a `.env` file at the **project root** (next to `requirements.txt`) with `OPENAI_API_KEY`, loaded with `python-dotenv` before creating the client.

**One-time setup**

1. The repo includes **`.env.local`** as a template. **Copy** it to `.env` in the repo root:

   ```bash
   cp .env.local .env
   ```

2. **Edit `.env`** and set your real key after `OPENAI_API_KEY=` (no quotes). Use a key supplied for the course, or create your own at [OpenAI API keys](https://platform.openai.com/api-keys).

3. **`.env`** is gitignored so it is never committed. **`.env.local`** stays in the repo as the shared template.

**Use API-Key in your Code**

Use the **Section 0 / first code cell** in [`part03-agent-with-structured-output/01_lp_formulation.ipynb`](part03-agent-with-structured-output/01_lp_formulation.ipynb) as the canonical example: project root path, `load_dotenv(dotenv_path=PROJECT_ROOT / ".env")`, assert `OPENAI_API_KEY`, then build the client. Other notebooks (for example Part 4) follow the same idea—copy or match that setup when you add API calls elsewhere.

If you see `OPENAI_API_KEY not found` with `.env` already at the repo root, Jupyter’s **current working directory** may not match what that cell assumes (`Path.cwd().parent` vs the repo root). Adjust `PROJECT_ROOT` in that cell to match your kernel’s cwd, or start Jupyter from the notebook’s folder so `..` resolves to the project root.
