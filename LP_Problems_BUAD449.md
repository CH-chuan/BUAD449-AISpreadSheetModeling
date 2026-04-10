# BUAD449 — LP Application Problems

## Problem 1: Product Manufacturing (Part 1)

A certain plant can manufacture four products A, B, C, and D in any combination. Each product requires time on each of three machines as follows (in minutes/unit):


| Product | Machine 1 | Machine 2 | Machine 3 |
| ------- | --------- | --------- | --------- |
| A       | 12        | 8         | 5         |
| B       | 7         | 9         | 10        |
| C       | 8         | 4         | 7         |
| D       | 10        | 0         | 3         |


Machine 1, 2, and 3 are available 20, 40, and 10 hours per week, respectively. Material costs are $2 each for products A and B and $1 each for C and D.

Assume all products are competitive and any amounts made may be sold at respective prices of $5, $4, $5, and $5. Variable labor costs are $4/hour for machines 1 and 2 and $3/hour for machine 3. Find the best product mix to maximize total weekly profit.

### Formulation

**Decision Variables:**

- X_A, X_B, X_C, X_D = units of each product to produce

**Objective:**

Max (5−2)X_A + (4−2)X_B + (5−1)X_C + (5−1)X_D − 4·(12X_A+7X_B+8X_C+10X_D)/60 − 4·(8X_A+9X_B+4X_C+0X_D)/60 − 3·(5X_A+10X_B+7X_C+3X_D)/60

**Subject to:**

- (12X_A + 7X_B + 8X_C + 10X_D) / 60 ≤ 20
- (8X_A + 9X_B + 4X_C + 0X_D) / 60 ≤ 40
- (5X_A + 10X_B + 7X_C + 3X_D) / 60 ≤ 10
- X_A, X_B, X_C, X_D ≥ 0

---

## Problem 2: Product Manufacturing — Extended (Part 1)

A certain plant can manufacture four products A, B, C, and D in any combination. Each product requires time on each of three machines as follows (in minutes/unit):


| Product | Machine 1 | Machine 2 | Machine 3 |
| ------- | --------- | --------- | --------- |
| A       | 12        | 8         | 5         |
| B       | 7         | 9         | 10        |
| C       | 8         | 4         | 7         |
| D       | 10        | 0         | 3         |


Machine 1, 2, and 3 are available 20, 40, and 10 hours per week, respectively. Material costs are $2 each for products A and B and $1 each for C and D.

Products are **not purely competitive**: the prices of $5, $4, $5, and $5 only to the first 20 units for each product. The prices of additional products A, B, C, and D are $4, $3, $4, and $4 respectively. Regular hours labor costs are $4/hour for machines 1 and 2 and $3/hour for machine 3. Additional machine hours, up to 10 hours for each machine, are available for each machine with corresponding labor costs of $5/hour for machines 1 and 2, and $4/hour for machine 3.

### Formulation

**Decision Variables:**

- L_A, L_B, L_C, L_D = quantity of each product produced within 20 units
- H_A, H_B, H_C, H_D = quantity of each product produced beyond 20 units
- R1, R2, R3 = regular hours used for each machine
- O1, O2, O3 = overtime hours used for each machine

**Objective:**

Max (5−2)L_A + (4−2)H_A + (4−2)L_B + (3−2)H_B + (5−1)L_C + (4−1)H_C + (5−1)L_D + (4−1)H_D − (4R1 + 5O1) − (4R2 + 5O2) − (3R3 + 4O3)

**Subject to:**

- R1 ≤ 20; R2 ≤ 40; R3 ≤ 10
- O1, O2, O3 ≤ 10
- L_A, L_B, L_C, L_D ≤ 20
- R1 + O1 = [12(L_A+H_A) + 7(L_B+H_B) + 8(L_C+H_C) + 10(L_D+H_D)] / 60
- R2 + O2 = [8(L_A+H_A) + 9(L_B+H_B) + 4(L_C+H_C) + 0(L_D+H_D)] / 60
- R3 + O3 = [5(L_A+H_A) + 10(L_B+H_B) + 7(L_C+H_C) + 3(L_D+H_D)] / 60
- All variables ≥ 0

---

## Problem 3: Farm Planning (Part 1)

Buster Sod operates an 800-acre irrigated farm. His principal activities are raising wheat, alfalfa, and beef. He has been allotted 1000 acre-feet of water for next year.

- Beef price: $500/ton; Wheat price: $2/bushel
- Alfalfa can be sold at $22/ton; if he needs to buy more, it costs $28/ton
- Wheat yield: 70 bushels/acre; Alfalfa yield: 4 tons/acre


| Activity          | Labor/Machine Cost ($) | Water Req. (Acre-Ft) | Land Req. (Acres) | Alfalfa Req. (Tons) |
| ----------------- | ---------------------- | -------------------- | ----------------- | ------------------- |
| 1 acre of wheat   | 20                     | 2                    | 1                 | —                   |
| 1 acre of alfalfa | 28                     | 3                    | 1                 | —                   |
| 1 ton of beef     | 50                     | 0.05                 | 0.1               | 5                   |


### Formulation

**Decision Variables:**

- W = total acres of wheat
- B = total tons of beef
- AR = total tons of alfalfa raised (note: acres of alfalfa = AR/4)
- AS = total tons of alfalfa sold
- AB = total tons of alfalfa bought

**Objective:**

Max (2×70 − 20)W − (28/4)AR + (500 − 50)B − 28·AB + 22·AS

**Subject to:**

- W + (1/4)AR + 0.1B ≤ 800  *(Land)*
- 2W + (3/4)AR + 0.05B ≤ 1000  *(Water)*
- 5B + AS = AR + AB  *(Alfalfa balance)*
- All variables ≥ 0

---

## Problem 4: GreenBridge Portfolio — Blending (Part 3)

GreenBridge Pension Fund can purchase up to $5M in QQQ, up to $7M in VOO, and up to $6M in BND.

Two portfolio products are offered:

- **Growth Portfolio** (younger employees): avg beta ≤ 1.05, avg ESG ≥ 6.0
- **Income Portfolio** (near-retirement): avg beta ≤ 0.40, avg ESG ≥ 7.5, at least 30% in BND

ETF properties:


| ETF | Beta | ESG Rating | Expense Ratio |
| --- | ---- | ---------- | ------------- |
| QQQ | 1.15 | 5.2        | 0.20%         |
| VOO | 1.00 | 6.8        | 0.03%         |
| BND | 0.05 | 8.5        | 0.03%         |


Management fee: 1.2% on Growth, 0.8% on Income. Demand is unlimited.

### Formulation

**Decision Variables:**

- x₁G, x₂G, x₃G = dollars from QQQ, VOO, BND allocated to Growth Portfolio
- x₁I, x₂I, x₃I = dollars from QQQ, VOO, BND allocated to Income Portfolio

**Objective:**

Max 0.0100·x₁G + 0.0117·x₂G + 0.0117·x₃G + 0.0060·x₁I + 0.0077·x₂I + 0.0077·x₃I

*(Coefficients = management fee − expense ratio for each ETF-portfolio combination)*

**Subject to:**

- x₁G + x₁I ≤ 5,000,000  *(QQQ supply)*
- x₂G + x₂I ≤ 7,000,000  *(VOO supply)*
- x₃G + x₃I ≤ 6,000,000  *(BND supply)*
- 0.10x₁G − 0.05x₂G − 1.00x₃G ≤ 0  *(Growth beta ≤ 1.05, linearized)*
- 0.75x₁I + 0.60x₂I − 0.35x₃I ≤ 0  *(Income beta ≤ 0.40, linearized)*
- −0.8x₁G + 0.8x₂G + 2.5x₃G ≥ 0  *(Growth ESG ≥ 6.0, linearized)*
- −2.3x₁I − 0.7x₂I + 1.0x₃I ≥ 0  *(Income ESG ≥ 7.5, linearized)*
- −0.30x₁I − 0.30x₂I + 0.70x₃I ≥ 0  *(Income BND ≥ 30%)*
- All variables ≥ 0

---

## Problem 5: Heating Oil Blending (Part 3)

A heating-oil distributor blends two grades of heating oil (regular and nontoxic) from three distillates. Blend specifications are weighted averages.

**Table 1 — Heating Oils:**


|          | Max Sulfur (gms/bar) | Min Vapor Pressure | Max Distil. 3 % | Price ($/bar) | Max Monthly Sales (bar) |
| -------- | -------------------- | ------------------ | --------------- | ------------- | ----------------------- |
| Regular  | 14                   | 6                  | 80%             | 12.00         | 10,000                  |
| Nontoxic | 8                    | 12                 | 30%             | 16.00         | 4,000                   |


**Table 2 — Distillates:**


|           | Sulfur (gms/bar) | Vapor Pressure | Cost ($/bar) | Max Available (bar/month) |
| --------- | ---------------- | -------------- | ------------ | ------------------------- |
| Distil. 1 | 6                | 16             | 10.00        | 3,000                     |
| Distil. 2 | 10               | 8              | 14.00        | 2,000                     |
| Distil. 3 | 18               | 4              | 6.00         | 10,000                    |


### Formulation

**Decision Variables:**

- R1, R2, R3 = bars of Distil. 1, 2, 3 used for Regular
- N1, N2, N3 = bars of Distil. 1, 2, 3 used for Nontoxic

**Objective:**

Max 12(R1+R2+R3) + 16(N1+N2+N3) − 10(R1+N1) − 14(R2+N2) − 6(R3+N3)

**Subject to:**

- R1 + N1 ≤ 3000;  R2 + N2 ≤ 2000;  R3 + N3 ≤ 10000  *(Material availability)*
- R1 + R2 + R3 ≤ 10000;  N1 + N2 + N3 ≤ 4000  *(Max monthly sales)*
- 6R1 + 10R2 + 18R3 ≤ 14(R1+R2+R3)  *(Regular sulfur)*
- 6N1 + 10N2 + 18N3 ≤ 8(N1+N2+N3)  *(Nontoxic sulfur)*
- 16R1 + 8R2 + 4R3 ≥ 6(R1+R2+R3)  *(Regular vapor pressure)*
- 16N1 + 8N2 + 4N3 ≥ 12(N1+N2+N3)  *(Nontoxic vapor pressure)*
- R3 ≤ 0.8(R1+R2+R3)  *(Regular max Distil. 3 content)*
- N3 ≤ 0.3(N1+N2+N3)  *(Nontoxic max Distil. 3 content)*
- All variables ≥ 0

---

## Problem 6: Crop Planning — Process Selection (Part 4)

A farm owner has 2000 acres across three plots (500, 800, 700 acres). Three crops can be planted: corn, peas, and soybeans.


| Crop     | Max Acreage | Profit ($/acre) |
| -------- | ----------- | --------------- |
| Corn     | 900         | 600             |
| Peas     | 700         | 450             |
| Soybeans | 1000        | 300             |


**Restrictions:**

- At least 60% of each plot must be under cultivation.
- The same proportion of each plot must be cultivated.

### Formulation

**Decision Variables:**

- C1, C2, C3 = acres of corn on plots 1, 2, 3
- P1, P2, P3 = acres of peas on plots 1, 2, 3
- S1, S2, S3 = acres of soybeans on plots 1, 2, 3

**Objective:**

Max 600(C1+C2+C3) + 450(P1+P2+P3) + 300(S1+S2+S3)

**Subject to:**

- C1+C2+C3 ≤ 900;  P1+P2+P3 ≤ 700;  S1+S2+S3 ≤ 1000
- 300 ≤ C1+P1+S1 ≤ 500
- 480 ≤ C2+P2+S2 ≤ 800
- 420 ≤ C3+P3+S3 ≤ 700
- (C1+P1+S1)/500 = (C2+P2+S2)/800 = (C3+P3+S3)/700  *(Equal proportion)*
- All variables ≥ 0

---

## Problem 7: Cargo Balancing — Process Selection (Part 4)

A ship has three cargo holds:


| Hold    | Weight Capacity (tons) | Volume Capacity (cubic feet) |
| ------- | ---------------------- | ---------------------------- |
| Forward | 3,000                  | 155,000                      |
| Center  | 4,000                  | 185,000                      |
| Rear    | 2,500                  | 145,000                      |


**Balance constraints:**

- Forward weight must be within 5% of rear weight.
- Center weight ≥ 1.3 × forward weight.
- Center weight ≥ 1.3 × rear weight.
- Center weight ≤ 0.9 × (forward + rear weight).

Four commodities are offered:


| Commodity | Amount (tons) | Volume (cu ft/ton) | Profit ($/ton) |
| --------- | ------------- | ------------------ | -------------- |
| 1         | 5,000         | 60                 | 6              |
| 2         | 3,000         | 50                 | 8              |
| 3         | 1,000         | 25                 | 5              |
| 4         | 1,500         | 40                 | 7              |


The ship owner may accept all or any part of each commodity.

### Formulation

**Decision Variables:**

- F1, C1, R1 = tons of commodity 1 in Forward, Center, Rear
- F2, C2, R2 = tons of commodity 2 in Forward, Center, Rear
- F3, C3, R3 = tons of commodity 3 in Forward, Center, Rear
- F4, C4, R4 = tons of commodity 4 in Forward, Center, Rear

**Objective:**

Max 6(F1+C1+R1) + 8(F2+C2+R2) + 5(F3+C3+R3) + 7(F4+C4+R4)

**Subject to:**

- F1+C1+R1 ≤ 5000;  F2+C2+R2 ≤ 3000;  F3+C3+R3 ≤ 1000;  F4+C4+R4 ≤ 1500  *(Supply)*
- F1+F2+F3+F4 ≤ 3000  *(Forward weight)*
- C1+C2+C3+C4 ≤ 4000  *(Center weight)*
- R1+R2+R3+R4 ≤ 2500  *(Rear weight)*
- 60F1+50F2+25F3+40F4 ≤ 155,000  *(Forward volume)*
- 60C1+50C2+25C3+40C4 ≤ 185,000  *(Center volume)*
- 60R1+50R2+25R3+40R4 ≤ 145,000  *(Rear volume)*
- 0.95(R1+R2+R3+R4) ≤ F1+F2+F3+F4 ≤ 1.05(R1+R2+R3+R4)  *(Forward ≈ Rear)*
- C1+C2+C3+C4 ≥ 1.3(F1+F2+F3+F4)  *(Center ≥ 130% of Forward)*
- C1+C2+C3+C4 ≥ 1.3(R1+R2+R3+R4)  *(Center ≥ 130% of Rear)*
- C1+C2+C3+C4 ≤ 0.9(F1+F2+F3+F4 + R1+R2+R3+R4)  *(Center ≤ 90% of Forward+Rear)*
- All variables ≥ 0

---

## Problem 8: Multi-Period Investment (Financial Planning)

You have $1,000 on hand right now. Find the best investment strategy to maximize cash on hand by the beginning of year 6. Annual interest on uninvested cash balance is 10%.


| Investment | Start                  | End                    | Return Rate |
| ---------- | ---------------------- | ---------------------- | ----------- |
| A          | every year (years 1–4) | 2 years later          | 40%         |
| B          | every year (years 1–3) | 3 years later          | 70%         |
| C          | year 2 only            | 4 years later (year 6) | 90%         |
| D          | year 5 only            | 1 year later (year 6)  | 30%         |


**Cash Flow Table:**


| Period | Flow In                                | Flow Out       |
| ------ | -------------------------------------- | -------------- |
| 1      | $1,000                                 | A1, B1, S1     |
| 2      | 1.1·S1                                 | A2, B2, C2, S2 |
| 3      | 1.4·A1, 1.1·S2                         | A3, B3, S3     |
| 4      | 1.7·B1, 1.4·A2, 1.1·S3                 | A4, S4         |
| 5      | 1.4·A3, 1.7·B2, 1.1·S4                 | D5, S5         |
| 6      | 1.4·A4, 1.7·B3, 1.9·C2, 1.3·D5, 1.1·S5 | *(final cash)* |


### Formulation

**Decision Variables:**

- A1, A2, A3, A4 = amount invested in A at the beginning of year 1, 2, 3, 4
- B1, B2, B3 = amount invested in B at the beginning of year 1, 2, 3
- C2 = amount invested in C at the beginning of year 2
- D5 = amount invested in D at the beginning of year 5
- S1, S2, S3, S4, S5 = amount saved as cash balance at the beginning of year 1, 2, 3, 4, 5

**Objective:**

Max 1.4·A4 + 1.7·B3 + 1.9·C2 + 1.3·D5 + 1.1·S5

**Subject to:**

- 1000 = A1 + B1 + S1  *(Period 1 equilibrium)*
- 1.1·S1 = A2 + B2 + C2 + S2  *(Period 2 equilibrium)*
- 1.4·A1 + 1.1·S2 = A3 + B3 + S3  *(Period 3 equilibrium)*
- 1.7·B1 + 1.4·A2 + 1.1·S3 = A4 + S4  *(Period 4 equilibrium)*
- 1.4·A3 + 1.7·B2 + 1.1·S4 = D5 + S5  *(Period 5 equilibrium)*
- All variables ≥ 0

---

## Problem 9: Investment and Payment — Sinking Fund (Financial Planning)

Anne Alyze is the investment manager for an organization that has signed a contract to purchase equipment costing $750,000. Payments are due as follows: $150,000 at the beginning of month 3, and $600,000 at the beginning of month 7. Anne will set up a sinking fund immediately (beginning of month 1) and wants to minimize the initial amount placed in the fund.


| Investment   | Available at Beginning of | Months to Maturity | Yield at Maturity |
| ------------ | ------------------------- | ------------------ | ----------------- |
| A            | 1, 2, 3, 4, 5, 6          | 1                  | 1.5%              |
| B            | 1, 3, 5                   | 2                  | 3.5%              |
| C            | 1, 4                      | 3                  | 6.0%              |
| D            | 1                         | 6                  | 11.0%             |
| Cash Reserve | 1, 2, 3, 4, 5, 6          | 0                  | 0%                |


**Cash Flow Table:**


| Period | Flow In                                  | Flow Out             |
| ------ | ---------------------------------------- | -------------------- |
| 1      | INL                                      | A1, B1, C1, D1, S1   |
| 2      | 1.015·A1, S1                             | A2, S2               |
| 3      | 1.035·B1, 1.015·A2, S2                   | $150,000, A3, B3, S3 |
| 4      | 1.06·C1, 1.015·A3, S3                    | A4, C4, S4           |
| 5      | 1.035·B3, 1.015·A4, S4                   | A5, B5, S5           |
| 6      | 1.015·A5, S5                             | A6, S6               |
| 7      | 1.11·D1, 1.06·C4, 1.035·B5, 1.015·A6, S6 | $600,000             |


### Formulation

**Decision Variables:**

- A1, A2, A3, A4, A5, A6 = amount invested in A at the beginning of month 1–6
- B1, B3, B5 = amount invested in B at the beginning of month 1, 3, 5
- C1, C4 = amount invested in C at the beginning of month 1, 4
- D1 = amount invested in D at the beginning of month 1
- S1, S2, S3, S4, S5, S6 = cash reserved at the beginning of month 1–6
- INL = initial amount placed in the sinking fund

**Objective:**

Min INL

**Subject to:**

- INL = A1 + B1 + C1 + D1 + S1  *(Month 1 equilibrium)*
- 1.015·A1 + S1 = A2 + S2  *(Month 2 equilibrium)*
- 1.035·B1 + 1.015·A2 + S2 = 150,000 + A3 + B3 + S3  *(Month 3 equilibrium)*
- 1.06·C1 + 1.015·A3 + S3 = A4 + C4 + S4  *(Month 4 equilibrium)*
- 1.035·B3 + 1.015·A4 + S4 = A5 + B5 + S5  *(Month 5 equilibrium)*
- 1.015·A5 + S5 = A6 + S6  *(Month 6 equilibrium)*
- 1.11·D1 + 1.06·C4 + 1.035·B5 + 1.015·A6 + S6 = 600,000  *(Month 7 equilibrium)*
- All variables ≥ 0

