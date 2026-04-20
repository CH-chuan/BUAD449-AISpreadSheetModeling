---
name: linear-program-solver
description: Solves continuous linear programs in Python with CVXPY using the project .venv, then reports optimal solution/value, binding vs non-binding constraints, dual-price sensitivity, and business recommendations. Use when the user wants to implement, solve, or numerically analyze an LP (not formulation-only—pair with linear-program-formulator when needed).
---

# Linear Program Solver (CVXPY)

## Goal

Turn a **given continuous LP** into a **runnable CVXPY script**, execute it (prefer **`.venv/bin/python`** after `pip install -r requirements.txt`), and present results in the **output format** below.

## Scope

- **In scope:** Continuous LP (real variables, linear objective, linear constraints, typically \(x \ge 0\)).
- **Out of scope:** Integer/binary programs, nonlinear models, full **allowable-range** sensitivity tables unless the user explicitly asks. Do **not** walk through dual-problem construction or primal–dual theory—only report **numerical sensitivity** (dual prices / shadow prices) and what they mean for the decision.

Formulation-only work belongs in **linear-program-formulator**; this skill assumes the model (or equivalent numeric \(c, A, b\)) is already clear.

## Workflow

1. **Parse the LP** — Objective direction, \(c\), constraint matrix/rows, RHS, variable bounds. **Keep units consistent** (e.g. hours vs minutes) across constraints and objective.
2. **Implement in CVXPY** — Split structural constraints into **named per-row constraints** (e.g. each \(A_{i,:} x \le b_i\)) so each row has its own `.dual_value` after solving. Use `cp.Variable(..., nonneg=True)` unless explicit bounds are needed for other reasons.
3. **Solve** — Prefer `solver=cp.HIGHS` for pure LP; fall back if unavailable. Require `status` in `{OPTIMAL, OPTIMAL_INACCURATE}` before interpreting duals.
4. **Post-process** — Compute slacks; classify binding vs non-binding; read **dual prices** from CVXPY for each structural row (see [reference.md](reference.md) for empirical check only if sign or magnitude looks wrong).
5. **Report** — Use the **Output format** section in order, ending with **Business recommendations**.

## Output format

Use this structure unless the user asks otherwise.

```markdown
## Optimal solution
- **Decision variables:** [name or index] = [value] (with units)
- **Optimal objective value:** [value] ([maximize|minimize] Z)

## Binding and non-binding constraints
For each structural constraint (in story order), report **slack** (for \(a^T x \le b\), slack \(= b - a^T x^*\)):
- **Binding:** [constraint label] — slack ≈ 0
- **Non-binding:** [constraint label] — slack = [value] ([units])

Use a clear numerical tolerance (e.g. \(10^{-5}\) times a typical scale, or absolute \(10^{-6}\) on slack).

## Sensitivity: dual prices (shadow prices)
For each **structural** constraint row, report:
- **Dual price** — numeric value from CVXPY (`constraint.dual_value`) after solve.
- **Units** — e.g. “$ per extra minute of machine 1 capacity” so the rate matches the objective and RHS units.
- **Plain-language meaning** — one sentence: how optimal **profit** (or **cost**, if minimizing) would change for a **small** increase of 1 unit in that constraint’s RHS, **ceteris paribus**. Note that this is a **local** linear rate; it can change if enough capacity is added that the optimal basis changes.

Do **not** derive or state the dual linear program; stay on **results and interpretation** only. If the reported dual conflicts with a quick **re-solve** with a tiny RHS bump, report the **empirical** rate \(\Delta Z / \Delta b\) for that constraint instead and use that in the narrative.

## Business recommendations
After the numbers, add a short **action-oriented** section (bullet list, 3–7 bullets) tied to the **optimal mix**, **binding constraints**, and **dual prices**:
- What to **produce** or **prioritize** operationally given the optimum.
- Where **scarce resources** bind and what that implies (bottlenecks).
- Whether **investing** in more of a binding resource (capacity, hours, material limit) is directionally attractive, using shadow prices **qualitatively** (highest marginal value first), without claiming a specific ROI unless the user supplied investment costs.
- Products or activities at **zero** in the LP optimum: interpret as “not currently attractive at the margin” unless economics change.
- Caveats: **continuous** LP (fractional units), static one-period model, shadow prices only **local**—keep language honest.

Keep tone **managerial**: clear, concise, no matrix algebra in this section.
```

## Implementation notes

- **Project environment:** `python3 -m venv .venv` → `.venv/bin/pip install -r requirements.txt` → `.venv/bin/python script.py`.
- **Do not** silently change the LP; if data is ambiguous, ask one clarifying question before solving.
- After solving, **sanity-check**: non-binding \(\le\) constraints at optimum usually have dual price \(\approx 0\); binding constraints often have nonzero duals.

## Additional resources

- Reading dual prices from CVXPY and optional empirical check: [reference.md](reference.md)
