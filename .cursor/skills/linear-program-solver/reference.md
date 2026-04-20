# Dual prices (shadow prices) from CVXPY

## Slack (binding vs non-binding)

For a row \(a_i^{\mathsf T} x \le b_i\), **slack** at optimum \(x^*\) is \(b_i - a_i^{\mathsf T} x^*\).

- **Binding:** slack \(\approx 0\) (within tolerance).
- **Non-binding:** slack \(> 0\); at optimum the **dual price** for that \(\le\) row is typically **0**.

## What to report as “dual price”

After `problem.solve()`, use each scalar row constraint’s **`constraint.dual_value`**.

**Interpretation for the user’s story:**

- **Maximize** profit: report how **profit** moves per **+1 unit** on that constraint’s RHS (e.g. +1 minute of capacity, +1 kg of raw material), for **small** changes.
- **Minimize** cost: report how **optimal cost** moves per **+1 unit** RHS relaxation (same “small change” caveat).

State **units** every time (e.g. $/minute, $/hour after converting RHS consistently).

## If the number looks wrong

Do **not** explain primal–dual pairs. Optionally **re-solve** once with \(b_i \leftarrow b_i + \varepsilon\) (tiny \(\varepsilon\) relative to scale), compare \(\Delta Z / \varepsilon\), and use that **empirical shadow price** in the write-up if it disagrees with `dual_value` (solver/convention quirks). Mention that you used a numerical check—still no dual-problem derivation.

## CVXPY pattern (one dual per structural row)

```python
import numpy as np
import cvxpy as cp

c = ...  # (n,)
A = ...  # (m, n)
b = ...  # (m,)

x = cp.Variable(A.shape[1], nonneg=True)
row_cons = [A[i] @ x <= b[i] for i in range(A.shape[0])]
prob = cp.Problem(cp.Maximize(c @ x), row_cons)
prob.solve(solver=cp.HIGHS)

x_star = np.asarray(x.value).ravel()
slack = b - A @ x_star
dual_prices = [float(row_cons[i].dual_value) for i in range(len(row_cons))]
```

Label each `dual_prices[i]` with the same name as the corresponding constraint in the problem statement.
