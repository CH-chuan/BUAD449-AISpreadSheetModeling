# Worked example: product mix with tiered prices and overtime labor

Use as a template when a product-mix problem has **two unit prices** (first \(K\) units vs rest) and/or **two labor rates** (regular vs overtime machine time with separate hour caps).

---

## Problem statement (data)

Four products A, B, C, D; machine times in **minutes per unit**:

| Product | Machine 1 | Machine 2 | Machine 3 |
| ------- | --------- | --------- | --------- |
| A       | 12        | 8         | 5         |
| B       | 7         | 9         | 10        |
| C       | 8         | 4         | 7         |
| D       | 10        | 0         | 3         |

- Machine **regular** availability: 20, 40, and 10 hours per week (machines 1–3).
- Up to **10 additional hours** per machine (overtime), with higher labor rates.
- Material cost: \$2/unit for A and B; \$1/unit for C and D.
- **Prices:** first **20 units** of each product at high price; additional units at low price: A \((5,4)\), B \((4,3)\), C \((5,4)\), D \((5,4)\) (dollars/unit).
- **Labor:** regular \$4/h on machines 1–2, \$3/h on machine 3; overtime \$5/h on 1–2, \$4/h on machine 3.

**Decide** weekly production quantities to **maximize profit** (revenue − material − labor).

---

## (a) Problem understanding and LP type

Choose how much of each product to make. Tiered selling prices and tiered labor are **piecewise linear** in totals but linear in **split** variables, so the model is a **continuous LP** (product mix with variable splitting).

---

## (b) Verbal formulation

**Objective:** Maximize total revenue minus material cost minus machine labor cost, where revenue applies the high unit price only to the portion of each product up to 20 units and the low price to any remainder, and labor charges the regular rate only on minutes assigned to the regular-time bucket (up to each machine’s regular weekly limit) and the overtime rate on minutes assigned to the overtime bucket (up to 10 extra hours per machine).

**Constraints:**

1. Each product’s total units equal “high-price” units (at most 20) plus “low-price” units (nonnegative).
2. Required processing minutes on each machine equal regular-time minutes plus overtime minutes for that machine.
3. Regular-time minutes per machine do not exceed regular weekly capacity; overtime minutes do not exceed 10 hours per machine (in minutes).
4. All quantities are nonnegative; high-price segment quantities are at most 20 per product.

---

## (c) Decision variables

**Pricing splits** (units, \(\geq 0\); \(y_j \leq 20\)):

- \(y_A,y_B,y_C,y_D\): units sold at the **high** price.
- \(z_A,z_B,z_C,z_D\): additional units at the **low** price.

Totals: \(x_j = y_j + z_j\) for \(j \in \{A,B,C,D\}\).

**Labor splits** (minutes, \(\geq 0\)):

- \(m_{i,r}\): minutes on machine \(i\) at **regular** labor rate, \(i \in \{1,2,3\}\).
- \(m_{i,o}\): minutes on machine \(i\) at **overtime** rate.

**Capacities (minutes):** \(R_1=1200\), \(R_2=2400\), \(R_3=600\); \(O=600\) overtime cap each.

**Coefficients \(a_{ij}\):** use the table above (e.g. \(a_{1A}=12\), \(a_{2D}=0\), \(a_{3D}=3\)).

---

## (d) Algebraic formulation

**Links and balances**

\[
x_j = y_j + z_j,\quad j \in \{A,B,C,D\}.
\]

\[
\sum_{j \in \{A,B,C,D\}} a_{ij}\, x_j = m_{i,r} + m_{i,o},\quad i=1,2,3.
\]

**Bounds**

\[
\begin{aligned}
0 &\leq m_{i,r} \leq R_i,\quad 0 \leq m_{i,o} \leq O,\quad i=1,2,3,\\
0 &\leq y_j \leq 20,\quad z_j \geq 0,\quad j \in \{A,B,C,D\}.
\end{aligned}
\]

**Objective (maximize \(Z\))**

Revenue minus material minus labor (labor: dollars per minute = hourly rate \(/\ 60\)):

\[
\begin{aligned}
Z =\;& \bigl(5y_A + 4z_A\bigr) + \bigl(4y_B + 3z_B\bigr) + \bigl(5y_C + 4z_C\bigr) + \bigl(5y_D + 4z_D\bigr) \\
&- 2(x_A + x_B) - (x_C + x_D) \\
&- \frac{4}{60}\bigl(m_{1,r}+m_{2,r}\bigr) - \frac{3}{60}m_{3,r}
 - \frac{5}{60}\bigl(m_{1,o}+m_{2,o}\bigr) - \frac{4}{60}m_{3,o}.
\end{aligned}
\]

**Why splits work:** Maximizing \(Z\) makes cheap regular minutes and high-price segments preferable at the margin, matching “fill regular time before overtime” and “value first 20 units at the high price” without binary variables.

**Equivalent hours formulation (optional):** Divide all \(a_{ij}\), \(R_i\), and \(O\) by 60; use \(h_{i,r},h_{i,o}\) in hours with the same bounds in hours; labor terms become \(4h_{1,r}+4h_{2,r}+3h_{3,r}+5h_{1,o}+5h_{2,o}+4h_{3,o}\).
