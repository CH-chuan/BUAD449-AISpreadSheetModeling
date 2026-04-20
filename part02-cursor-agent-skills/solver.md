# LP Solver Skill Example

This file is a **worked example** of the general skill-building process from `part02-cursor-agent-skills/guide.md`.

The example skill is **`linear-program-solver`**, a project skill for solving a **continuous linear program** with Python and **CVXPY**.

The actual skill files live in:

- `.cursor/skills/linear-program-solver/SKILL.md`
- `.cursor/skills/linear-program-solver/reference.md`

---

## What This Skill Is For

This skill is for the case where the LP is already formulated clearly enough to solve.

Its job is to help Cursor:

1. read the LP,
2. write a Python script with **CVXPY**,
3. run the script in the project environment,
4. report results in a useful business format.

This is a good example of a skill where the **workflow** is fairly standard, but the **output** must be tightly controlled.

---

## Why This Skill Needs Specific Instructions

Without a skill, the agent might still solve the LP, but the output may vary too much.

For this solver example, we wanted the output to consistently include:

1. the **optimal solution**,
2. the **optimal objective value**,
3. **binding** and **non-binding** constraints,
4. **dual-price sensitivity**,
5. **business recommendations**.

That makes the skill useful for teaching because students can compare answers across problems using the same structure.

---

## How the Skill Is Organized

### `SKILL.md`

This main file tells the agent:

- when to use the skill,
- what is in scope,
- what implementation workflow to follow,
- and what report format to use.

For `linear-program-solver`, the main file specifies:

- **continuous LP only**,
- use **CVXPY**,
- use the project **`.venv`**,
- report optimal solution and value,
- classify constraints as binding or non-binding,
- report **dual prices** in plain language,
- end with **business recommendations**.

### `reference.md`

This support file contains extra details the agent may need while solving, including:

- how to interpret slacks,
- how to read dual prices from CVXPY,
- a code pattern for extracting dual values.

This keeps the main skill short while preserving technical detail when needed.

---

## What Students Should Learn From This Example

This example shows a useful pattern:

- keep the **scope narrow**,
- standardize the **output structure**,
- move technical details into a support file,
- and test the skill on a real problem.

It also shows that a good skill does not need to control everything. In this case, the internal coding details can stay somewhat flexible, but the **final report structure** should be consistent.

---

## Reproducible Prompt Pattern

If a student wanted to reproduce this kind of skill from scratch, a good starting prompt would be:

> `/create-skill I want to build a project skill for solving continuous linear programs with CVXPY. Let's first discuss scope, environment, and the exact results format I want.`

That prompt works well because it names:

- the task,
- the tool choice,
- the scope,
- and the need for a controlled output format.

---

## Design Takeaway

The solver example is a case where the agent must both **do computation** and **communicate results well**.

That is why this skill emphasizes:

- environment setup,
- implementation workflow,
- numerical output,
- and interpretation for decision-making.

If you want to compare this with a narrower, formulation-only skill, read `part02-cursor-agent-skills/formulator.md`.
