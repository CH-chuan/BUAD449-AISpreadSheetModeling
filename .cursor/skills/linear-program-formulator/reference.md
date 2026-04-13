# LP types and pattern templates (reference)

Use to support step **(a)**; adapt symbols and coefficients to the user’s problem.

## Product mix

**Signals:** Several products or activities; limited resources; contribution margin or profit per unit.

**Typical variables:** \(x_j\) = units of product \(j\) (\(x_j \geq 0\)).

**Typical objective:** Maximize \(\sum_j p_j x_j\).

**Typical constraints:** \(\sum_j a_{ij} x_j \leq b_i\) for each resource \(i\); optional \(x_j \leq d_j\).

**Piecewise linear tiers (still LP):** Split each product quantity \(x_j = y_j + z_j\) with \(0 \leq y_j \leq K\) (high price on \(y_j\)) and \(z_j \geq 0\) (low price on \(z_j\)). Split machine time into regular and overtime minutes with separate caps and rates, linked by \(\sum_j a_{ij}x_j = m_{i,r}+m_{i,o}\). Full numeric walkthrough: [examples.md](examples.md).

## Blending / diet

**Signals:** Mix inputs; output must meet minimum (or maximum) levels of attributes; minimize cost or maximize profit.

**Typical variables:** \(x_j\) = amount of input \(j\) (\(x_j \geq 0\)).

**Typical objective:** Minimize \(\sum_j c_j x_j\) (or maximize profit if selling a blend with linear revenue).

**Typical constraints:** \(\sum_j a_{ij} x_j \geq r_i\) for minimum standard \(i\); use \(\leq\) for caps.

## Transportation

**Signals:** Ship from origins to destinations; supply and demand; unit costs.

**Typical variables:** \(x_{ij}\) = amount shipped from \(i\) to \(j\) (\(x_{ij} \geq 0\)).

**Typical objective:** Minimize \(\sum_{i,j} c_{ij} x_{ij}\).

**Typical constraints:** \(\sum_j x_{ij} \leq s_i\); \(\sum_i x_{ij} \geq d_j\) (or \(=\) when appropriate and balanced).

## Out of scope for this skill

- **Integer or binary models** — Tell the user and skip formulation (steps **(b)–(d)**); this skill is continuous LP only.
- **Nonlinear** — Ratio objectives, products of variables, nonlinear rates, etc.; do not force a linear model.
