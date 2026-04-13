---
name: linear-program-formulator
description: Builds continuous linear programming models using a fixed sequence—classify problem type, verbal objective and constraints, decision variables, then algebraic objective and constraints. Skips formulation when the problem is integer programming, binary, or nonlinear. Use when the user asks to formulate, model, or set up an LP, linear program, or linear optimization (e.g., product mix, blending, diet, transportation, piecewise unit pricing, regular and overtime machine labor).
---

# Linear Program Formulator

## Goal

Produce a **correct, complete continuous LP** (real-valued decision variables, linear objective and constraints). This skill does **not** cover solvers or implementation.

## Scope: continuous LP only

Before continuing past **(a)**:

- If the natural model needs **integer** or **binary** variables (indivisible counts, yes/no decisions, “how many whole units,” fixed charges that require binary logic, etc.), **stop**: briefly explain that it is an integer/binary program, not a pure LP, and **do not** complete steps **(b)–(d)** unless the user explicitly reframes the problem as a continuous relaxation.
- If the model is **nonlinear**, **stop** and say so; do not force a linear formulation.

When the problem is a valid continuous LP, assume **non-negative continuous** variables unless the statement allows negative values.

## Workflow

Follow these steps **in order**. Do not skip the verbal steps **(b)** when formulating; they catch wrong inequality direction and missing limits before algebra.

### (a) Understand the problem and identify the LP type

- Restate what is being decided and what is fixed (data).
- Apply **Scope** above first; if out of scope, output only the short “stop” response (see **Output format**).
- Classify using problem structure, e.g.:
  - **Product / production mix** — multiple activities or products, shared scarce resources (capacity, labor, materials), per-unit contributions (profit or cost). **Piecewise linear** tiered prices (e.g., first \(K\) units at a higher price) or tiered machine labor (regular vs overtime minutes) stay in scope: introduce **split variables** with bounds so the objective and constraints stay linear; see [examples.md](examples.md).
  - **Blending / diet** — choose amounts of inputs so output meets minimum or maximum standards (nutrients, octane, etc.); often minimize cost or maximize profit subject to quality bounds.
  - **Transportation** — ship from sources to destinations; supplies and demands; minimize (or sometimes maximize) linear shipping cost.
  - **Other** — staffing with coverage, multi-period inventory (still LP if linear), etc. Name the pattern honestly; if the natural model is nonlinear, say so.

### (b) Verbal objective and constraints

- **Objective (verbal):** One sentence: what is maximized or minimized, in plain language (e.g., “total weekly profit,” “total ingredient cost”).
- **Constraints (verbal):** List each limit or requirement as a full sentence (e.g., “Total machine hours used cannot exceed 400 hours per week,” “Protein from all foods must be at least 50 g”). Include non-negativity in words if it applies (“Quantities produced cannot be negative”).

### (c) Decision variables

- Define each variable with: **symbol**, **meaning**, **units**, and **sign** (typically \( \geq 0 \)).
- Use subscripts consistently with the LP type (e.g., \(x_j\) for product \(j\), \(x_{ij}\) for flow from \(i\) to \(j\)).

### (d) Objective function and constraints (algebraic)

- Write **maximize** or **minimize** \(Z =\) a **linear** sum (no products of variables, no nonlinear functions).
- Write each constraint in symbols with correct **\(\leq\) / \(\geq\) / \(=\)**. Add explicit variable bounds if not already included.

**After (d), briefly verify:** units balance on each constraint; count of constraints matches the story; objective and all constraints are linear.

Optional if asked: standard matrix form (\(c\), \(A\), \(b\)) with a fixed ordering of variables.

## Output format

**If the problem is not a continuous LP** (integer, binary, or nonlinear), use this and stop:

```markdown
## Out of scope
**Reason:** [integer program | binary program | nonlinear model — brief justification]

This skill only formulates **continuous linear programs**. Skipping steps (b)–(d). If you restate the problem as a continuous LP (or switch to an IP/MILP workflow), we can continue.
```

**If the problem is a continuous LP**, use this structure unless the user asks otherwise:

```markdown
## (a) Problem understanding and LP type
[Short restatement + named type, e.g., product mix]

## (b) Verbal formulation
**Objective:** [one sentence]

**Constraints:**
1. ...
2. ...

## (c) Decision variables
- ...

## (d) Algebraic formulation
**Objective:** [maximize|minimize] Z = ...

**Constraints:**
1. ...
2. ...
```

## Additional resources

- Pattern templates: [reference.md](reference.md)
- Worked example (product mix with tiered prices and overtime labor): [examples.md](examples.md)
