# LP Formulator Skill Example

This file is a **worked example** of the general skill-building process from `part02-cursor-agent-skills/guide.md`.

The example skill is **`linear-program-formulator`**, a project skill for writing a **continuous linear program** in a consistent BUAD449-style format.

The actual skill files live in:

- `.cursor/skills/linear-program-formulator/SKILL.md`
- `.cursor/skills/linear-program-formulator/reference.md`
- `.cursor/skills/linear-program-formulator/examples.md`

---

## What This Skill Is For

This skill is for the case where the user wants to **formulate** an LP, not solve it numerically.

Its job is to help Cursor:

1. identify the LP type,
2. restate the problem clearly,
3. write the verbal objective and constraints,
4. define decision variables,
5. write the algebraic model.

This is a good example of a skill where the **reasoning sequence** matters a lot. The point is not just to get an algebraic answer, but to follow a teaching-friendly structure that reduces modeling mistakes.

---

## Why This Skill Should Stay Separate From the Solver

The solver skill and formulator skill are related, but they should not be merged.

The formulator skill is narrower:

- it does **not** write code,
- it does **not** run a solver,
- it does **not** focus on numerical sensitivity analysis.

Instead, it focuses on getting the model structure right before any implementation begins.

This separation helps students because it makes the workflow clearer:

1. first formulate correctly,
2. then solve if needed.

---

## How the Skill Is Organized

### `SKILL.md`

This main file tells the agent:

- when to use the skill,
- what is in scope,
- what sequence to follow,
- and what answer structure to produce.

For `linear-program-formulator`, the main file requires the agent to present:

- **(a) problem understanding and LP type**,
- **(b) verbal formulation**,
- **(c) decision variables**,
- **(d) algebraic formulation**.

It also makes the scope explicit:

- **continuous LP only**,
- stop if the natural model is integer, binary, or nonlinear.

### `reference.md`

This support file stores pattern templates such as:

- product mix,
- blending / diet,
- transportation.

That makes it easier for the agent to map a new problem into a known LP pattern.

### `examples.md`

This file stores a worked example for a more advanced formulation pattern: a product-mix problem with:

- tiered prices,
- regular and overtime labor,
- split variables to keep the model linear.

This is especially useful for students because it shows how a more complicated story can still be turned into a continuous LP without jumping straight to code.

---

## What Students Should Learn From This Example

This example shows a different skill design pattern from the solver.

Here, the most important thing to control is the **sequence of reasoning**:

1. identify the structure,
2. state the model in words,
3. define variables carefully,
4. write the algebra.

That ordering improves reproducibility because students can follow the same checklist every time instead of jumping directly to equations.

---

## Reproducible Prompt Pattern

If a student wanted to reproduce this kind of skill from scratch, a good starting prompt would be:

> `/create-skill I want to build a project skill for formulating continuous linear programs in a consistent step-by-step format. Let's discuss scope, standard sections, and what examples should be included.`

That prompt works well because it highlights:

- the task,
- the desired structure,
- the need for scope control,
- and the value of worked examples.

---

## Design Takeaway

The formulator example is a case where the main value of the skill is **teaching a disciplined modeling process**.

That is why this skill emphasizes:

- classification,
- verbal modeling,
- clean variable definitions,
- and a standard final structure.

If you want to compare this with a more implementation-heavy skill, read `part02-cursor-agent-skills/solver.md`.
