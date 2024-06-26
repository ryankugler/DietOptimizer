# Diet Optimization for Canadian University Students

## Overview

This project focuses on developing an optimization model for diet planning tailored to the needs of Canadian university students. The primary objective is to minimize food costs while satisfying nutritional requirements—calories, protein, carbohydrates, and fats—essential for a healthy diet. The target audience for this project includes first-year university students who often face dietary challenges due to budget constraints and a busy academic schedule.

## Introduction to Linear Programming (LP) and Mixed-Integer Programming (MIP)

### Linear Programming (LP)

Linear Programming (LP) is a method to achieve the best outcome in a mathematical model whose requirements are represented by linear relationships. It is a technique used to optimize a linear objective function, subject to linear equality and inequality constraints. The solution space for LP problems is convex, making it easier to find the global optimum.

#### Mathematical Formulation of LP:

Given a vector of variables \( \mathbf{x} \), the standard form of an LP model is:

- **Objective Function**: Minimize or maximize ![Objective Function](https://latex.codecogs.com/png.latex?\min%20\sum_{i=1}^{24}%20y_i%20x_i)

- **Constraints**:
  - Linear equality constraints: \( A\mathbf{x} = b \)
  - Linear inequality constraints: \( A\mathbf{x} \leq b \)
  - Non-negativity constraints: \( \mathbf{x} \geq 0 \)

Where \( c, \mathbf{x} \), and \( b \) are vectors and \( A \) is a matrix of coefficients.

### Mixed-Integer Programming (MIP)

Mixed-Integer Programming (MIP) extends LP by including integer constraints to some or all decision variables. This inclusion makes MIPs significantly harder to solve, as the solution space becomes non-convex, leading to multiple local optima.

#### Mathematical Formulation of MIP:

Similar to LP, but with the addition that some or all variables are constrained to be integers:

- **Objective Function**: Minimize or maximize \( c^T \mathbf{x} \)
- **Constraints**:
  - Linear constraints: \( A\mathbf{x} \leq b \)
  - Integer constraints: Some or all \( x_i \) must satisfy \( x_i \in \mathbb{Z} \)

## Project Description

### Objective

The goal is to create a daily diet plan from a specified list of cafeteria foods that meets the minimum daily nutritional requirements at the lowest possible cost.

### Decision Variables

For the MIP model:
- \( x_i \): Binary variable indicating whether item \( i \) is included (1) or not (0).
- \( y_i \): Cost for item \( i \).
- \( p_i \): Protein content in food item \( i \).
- \( c_i \): Caloric content in food item \( i \).
- \( q_i \): Carbohydrates content in food item \( i \).
- \( f_i \): Fat content in food item \( i \).

For the LP model:
- The variables remain the same, but \( x_i \) can take any non-negative rational value representing the amount (in servings) of item \( i \) included in the diet.

### Constraints

1. **Nutritional intake**:
   - Total Calories: ![Calorie Constraint](https://latex.codecogs.com/png.latex?\sum_{i=1}^{24}%20c_i%20x_i%20\geq%202200)
   - Total Protein: ![Protein Constraint](https://latex.codecogs.com/png.latex?\sum_{i=1}^{24}%20p_i%20x_i%20\geq%2055)
   - Total Carbohydrates: ![Carbohydrates Constraint](https://latex.codecogs.com/png.latex?\sum_{i=1}^{24}%20q_i%20x_i%20\geq%20130)
   - Total Fat: ![Fat Constraint](https://latex.codecogs.com/png.latex?\sum_{i=1}^{24}%20f_i%20x_i%20\geq%2050)

2. **Budget constraint**:
   - ![Budget Constraint](https://latex.codecogs.com/png.latex?\sum_{i=1}^{24}%20y_i%20x_i%20\leq%2020)

3. **Variety and food selection rules**:
   - At least 5 different foods per day: ![Variety Constraint](https://latex.codecogs.com/png.latex?\sum_{i=1}^{24}%20x_i%20\geq%205)
   - If chicken breast is selected, then steamed vegetables must be selected: ![Linkage Constraint](https://latex.codecogs.com/png.latex?x_1%20\leq%20x_4)
   - Protein powder is selected only if milk, peanut butter, and bananas are all selected: ![Protein Powder Constraint](https://latex.codecogs.com/png.latex?(x_5-x_7)%2B(x_5-x_8)%2B(x_5-x_3)%20\leq%200)
   - Milk must be selected if frosted flakes are selected: ![Milk and Flakes Constraint](https://latex.codecogs.com/png.latex?x_14%20\leq%20x_3)
   - Exactly one beverage (milk, Coca-Cola, or orange juice): ![Beverage Constraint](https://latex.codecogs.com/png.latex?x_3%20+%20x_23%20+%20x_24%20=%201)

### Optimization

- **MIP Model**: Aimed at finding a binary solution (food items are either selected or not).
- **LP Model**: Allows for partial servings, providing a more granular optimization that can reflect more realistic consumption patterns.

### Sensitivity Analysis and Shadow Pricing

Sensitivity analysis and shadow pricing are integral components of LP and MIP solutions, providing insights into how changes in the constraints or objective function coefficients affect the optimal solution.

- **Shadow Prices**: These values represent the rate at which the objective function's value would increase or decrease with a one-unit change in the right-hand side of a constraint, holding all else constant. For instance, if the shadow price for the calorie constraint is $0.04, then increasing the minimum required calories by one unit would increase the minimal cost by $0.04.

- **Reduced Costs**: For decision variables, the reduced cost indicates how much the objective function's coefficient would need to improve (increase for maximization problems, decrease for minimization problems) before that variable would change from its current solution value.

- **Objective Coefficient Sensitivity**: This indicates how much you can increase or decrease a coefficient of the objective function before the current optimal basis changes.

- **Constraint RHS Sensitivity**: This reveals the range over which the right-hand side of a constraint can vary before the current basis of the optimal solution becomes invalid.

## Implementation

This project utilizes Python with libraries such as `PuLP` or `Gurobi` for defining and solving the optimization models. The source code includes data management, model formulation, constraint setting, execution of the solver, and results interpretation.

## Conclusion

The project showcases how LP and MIP can be effectively utilized in practical scenarios like diet planning for budget-constrained university students, balancing nutritional needs with financial limitations. The results provide a foundational strategy that students can adapt to maintain a healthy diet during their academic pursuits.
