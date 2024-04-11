from gurobipy import Model, GRB, quicksum

# --- Food Data --- #
foods = [
    {
        "name": "Chicken Breast",
        "calories": 165,
        "protein": 31,
        "carbs": 0,
        "fat": 3.6,
        "cost": 2.00,
    },
    {
        "name": "Whole Wheat Bread",
        "calories": 81,
        "protein": 4,
        "carbs": 13,
        "fat": 1.5,
        "cost": 0.25,
    },
    {
        "name": "Milk",
        "calories": 103,
        "protein": 8,
        "carbs": 12,
        "fat": 2.4,
        "cost": 1.00,
    },
    {
        "name": "Steamed Vegetables",
        "calories": 50,
        "protein": 2,
        "carbs": 10,
        "fat": 0.5,
        "cost": 0.50,
    },
    {
        "name": "Protein Powder",
        "calories": 120,
        "protein": 24,
        "carbs": 3,
        "fat": 1,
        "cost": 0.50,
    },
    {
        "name": "Eggs",
        "calories": 78,
        "protein": 6,
        "carbs": 0.6,
        "fat": 5,
        "cost": 0.32,
    },
    {
        "name": "Banana",
        "calories": 89,
        "protein": 1.1,
        "carbs": 22.8,
        "fat": 0.3,
        "cost": 0.20,
    },
    {
        "name": "Peanut Butter",
        "calories": 188,
        "protein": 8,
        "carbs": 6,
        "fat": 16,
        "cost": 0.50,
    },
    {
        "name": "Oatmeal",
        "calories": 68,
        "protein": 2.4,
        "carbs": 12,
        "fat": 1.5,
        "cost": 0.30,
    },
    {
        "name": "Salmon",
        "calories": 206,
        "protein": 22,
        "carbs": 0,
        "fat": 12,
        "cost": 3.00,
    },
    {
        "name": "Greek Yogurt",
        "calories": 59,
        "protein": 10,
        "carbs": 3.6,
        "fat": 0.4,
        "cost": 0.75,
    },
    {
        "name": "Avacado",
        "calories": 240,
        "protein": 3,
        "carbs": 13,
        "fat": 22,
        "cost": 0.70,
    },
    {
        "name": "Rice",
        "calories": 205,
        "protein": 4,
        "carbs": 45,
        "fat": 0.4,
        "cost": 0.30,
    },
    {
        "name": "Frosted Flakes",
        "calories": 130,
        "protein": 2,
        "carbs": 37.3,
        "fat": 0,
        "cost": 1.00,
    },
    {
        "name": "Vanilla Cupcake",
        "calories": 293,
        "protein": 2.2,
        "carbs": 42,
        "fat": 13,
        "cost": 2.50,
    },
    {
        "name": "Peanuts",
        "calories": 567,
        "protein": 26,
        "carbs": 16,
        "fat": 49,
        "cost": 2.50,
    },
    {
        "name": "Pasta",
        "calories": 220,
        "protein": 8,
        "carbs": 43,
        "fat": 1.3,
        "cost": 1.20,
    },
    {
        "name": "Quinoa",
        "calories": 120,
        "protein": 4,
        "carbs": 21,
        "fat": 1.9,
        "cost": 0.70,
    },
    {
        "name": "Potato",
        "calories": 160,
        "protein": 4,
        "carbs": 37,
        "fat": 0.2,
        "cost": 0.25,
    },
    {
        "name": "Cheese",
        "calories": 81,
        "protein": 11,
        "carbs": 3.4,
        "fat": 2.3,
        "cost": 1.50,
    },
    {
        "name": "Chocolate bar",
        "calories": 230,
        "protein": 2,
        "carbs": 25,
        "fat": 13,
        "cost": 1.80,
    },
    {
        "name": "Tofu",
        "calories": 70,
        "protein": 8,
        "carbs": 1.9,
        "fat": 4.2,
        "cost": 1.50,
    },
    {
        "name": "Orange Juice",
        "calories": 112,
        "protein": 1.7,
        "carbs": 25.8,
        "fat": 0.5,
        "cost": 0.75,
    },
    {
        "name": "Coca-Cola",
        "calories": 140,
        "protein": 0,
        "carbs": 39,
        "fat": 0,
        "cost": 1.50,
    },
]

m = Model()
x = m.addVars(len(foods), vtype=GRB.BINARY, name="x")
# --- Objective Function ---- #
m.setObjective(
    quicksum(x[i] * foods[i]["cost"] for i in range(len(foods))), GRB.MINIMIZE
)
# --- Constraints --- #
m.addConstr(
    quicksum(x[i] * foods[i]["calories"] for i in range(len(foods))) >= 2200,
    "MinCalories",
)
m.addConstr(
    quicksum(x[i] * foods[i]["protein"] for i in range(len(foods))) >= 55, "MinProtein"
)
m.addConstr(
    quicksum(x[i] * foods[i]["carbs"] for i in range(len(foods))) >= 130, "MinCarbs"
)
m.addConstr(quicksum(x[i] * foods[i]["fat"] for i in range(len(foods))) >= 50, "MinFat")
m.addConstr(
    quicksum(x[i] * foods[i]["cost"] for i in range(len(foods))) <= 20, "MaxCost"
)
m.addConstr(quicksum(x[i] for i in range(len(foods))) >= 5, "Variety Constraint")
m.addConstr(x[0] - x[3] <= 0, "Chicken with Vegetables Constraint")
m.addConstr(x[4] <= x[7], "Protein Powder only selected if Peanut Butter is selected")
m.addConstr(x[4] <= x[2], "Protein Powder only selected if Milk is selected")
m.addConstr(x[4] <= x[6], "Protein Powder only selected if Bananas are selected")
m.addConstr(x[14] + x[20] <= 1, "cupcake and chocolate are mutually exclusive")
m.addConstr(x[13] <= x[2], "Milk must be selected if frosted flakes are selected")
m.addConstr(x[2] + x[len(foods) - 2] + x[len(foods) - 1] == 1, "Exactly 1 Beverage")

m.optimize()
if m.status == GRB.OPTIMAL:
    print("Optimal solution:\n")
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0
    for i, v in enumerate(m.getVars()):
        if v.x > 0:
            print(f'{foods[i]["name"]} selected')
            total_calories += foods[i]["calories"] * v.x
            total_protein += foods[i]["protein"] * v.x
            total_carbs += foods[i]["carbs"] * v.x
            total_fat += foods[i]["fat"] * v.x

    print(f"\nTotal Cost: ${m.objVal:.2f}")
    print(f"Total Calories: {total_calories}")
    print(f"Total Protein: {total_protein}g")
    print(f"Total Carbs: {total_carbs}g")
    print(f"Total Fat: {total_fat}g")
else:
    print("No convergence")
