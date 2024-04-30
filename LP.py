from gurobipy import Model, GRB, quicksum

want_sensitivity_report = False

# ---- Food Data ---- #
foods = [
    {"name": "Chicken Breast", "calories": 165, "protein": 31, "carbs": 0, "fat": 3.6, "cost": 2.00, "group": "protein"},
    {"name": "Whole Wheat Bread", "calories": 81, "protein": 4, "carbs": 13, "fat": 1.5, "cost": 0.25, "group": "grain"},
    {"name": "Milk", "calories": 103, "protein": 8, "carbs": 12, "fat": 2.4, "cost": 1.00, "group": "dairy"},
    {"name": "Steamed Vegetables", "calories": 50, "protein": 2, "carbs": 10, "fat": 0.5, "cost": 0.50, "group": "vegetable"},
    {"name": "Protein Powder", "calories": 120, "protein": 24, "carbs": 3, "fat": 1, "cost": 0.50, "group": "protein"},
    {"name": "Eggs", "calories": 78, "protein": 6, "carbs": 0.6, "fat": 5, "cost": 0.32, "group": "protein"},
    {"name": "Banana", "calories": 89, "protein": 1.1, "carbs": 22.8, "fat": 0.3, "cost": 1.60, "group": "fruit"},
    {"name": "Peanut Butter", "calories": 188, "protein": 8, "carbs": 6, "fat": 16, "cost": 0.50, "group": "protein"},
    {"name": "Oatmeal", "calories": 68, "protein": 2.4, "carbs": 12, "fat": 1.5, "cost": 0.30, "group": "grain"},
    {"name": "Salmon", "calories": 206, "protein": 22, "carbs": 0, "fat": 12, "cost": 3.00, "group": "protein"},
    {"name": "Greek Yogurt", "calories": 59, "protein": 10, "carbs": 3.6, "fat": 0.4, "cost": 0.75, "group": "dairy"},
    {"name": "Avocado", "calories": 240, "protein": 3, "carbs": 13, "fat": 22, "cost": 0.70, "group": "fruit"},
    {"name": "Rice", "calories": 205, "protein": 4, "carbs": 45, "fat": 0.4, "cost": 0.30, "group": "grain"},
    {"name": "Frosted Flakes", "calories": 130, "protein": 2, "carbs": 37.3, "fat": 0, "cost": 1.00, "group": "junk"},
    {"name": "Vanilla Cupcake", "calories": 293, "protein": 2.2, "carbs": 42, "fat": 13, "cost": 2.50, "group": "junk"},
    {"name": "Peanuts", "calories": 567, "protein": 26, "carbs": 16, "fat": 49, "cost": 2.50, "group": "protein"},
    {"name": "Pasta", "calories": 220, "protein": 8, "carbs": 43, "fat": 1.3, "cost": 1.20, "group": "grain"},
    {"name": "Quinoa", "calories": 120, "protein": 4, "carbs": 21, "fat": 1.9, "cost": 0.70, "group": "grain"},
    {"name": "Potato", "calories": 160, "protein": 4, "carbs": 37, "fat": 0.2, "cost": 0.25, "group": "vegetable"},
    {"name": "Cheese", "calories": 81, "protein": 11, "carbs": 3.4, "fat": 2.3, "cost": 1.50, "group": "dairy"},
    {"name": "Chocolate bar", "calories": 230, "protein": 2, "carbs": 25, "fat": 13, "cost": 1.80, "group": "junk"},
    {"name": "Tofu", "calories": 70, "protein": 8, "carbs": 1.9, "fat": 4.2, "cost": 1.50, "group": "protein"},
    {"name": "Orange Juice", "calories": 112, "protein": 1.7, "carbs": 25.8, "fat": 0.5, "cost": 0.75, "group": "fruit"},
    {"name": "Coca-Cola", "calories": 140, "protein": 0, "carbs": 39, "fat": 0, "cost": 1.50, "group": "junk"},
    {"name": "Apple", "calories": 52, "protein": 0, "carbs": 14, "fat": 0.2, "cost": 0.3, "group": "fruit"},
    {"name": "Orange", "calories": 62, "protein": 1, "carbs": 15, "fat": 0.2, "cost": 0.5, "group": "fruit"},
    {"name": "Pineapple", "calories": 82, "protein": 1, "carbs": 22, "fat": 0.2, "cost": 1, "group": "fruit"},
]

m = Model()
x = m.addVars(len(foods), lb=0, vtype=GRB.CONTINUOUS, name="x")

# ---- Objective Function ---- #
m.setObjective(quicksum(x[i] * foods[i]['cost'] for i in range(len(foods))), GRB.MINIMIZE)


# ---- Variables ---- #
max_cost = 20 # default 20
max_calories = 2500 # default 2500
max_protein = 150 # default 150
max_carbs = 300 # default 300
max_fat = 70 # default 70

min_calories = 2200 # default 2200
min_protein = 55 # default 55
min_carbs = 130 # default 130
min_fat = 50 # default 50

# ---- Constraints ---- #
m.addConstr(quicksum(x[i] * foods[i]["calories"] for i in range(len(foods))) >= min_calories, "MinCalories")
m.addConstr(quicksum(x[i] * foods[i]["protein"] for i in range(len(foods))) >= min_protein, "MinProtein")
m.addConstr(quicksum(x[i] * foods[i]["carbs"] for i in range(len(foods))) >= min_carbs, "MinCarbs")
m.addConstr(quicksum(x[i] * foods[i]["fat"] for i in range(len(foods))) >= min_fat, "MinFat")
m.addConstr(quicksum(x[i] * foods[i]["cost"] for i in range(len(foods))) <= max_cost, "MaxCost")
m.addConstr(quicksum(x[i] * foods[i]["calories"] for i in range(len(foods))) <= max_calories, "MaxCalories")
m.addConstr(quicksum(x[i] * foods[i]["protein"] for i in range(len(foods))) <= max_protein, "MaxProtein")
m.addConstr(quicksum(x[i] * foods[i]["carbs"] for i in range(len(foods))) <= max_carbs, "MaxCarbs")
m.addConstr(quicksum(x[i] * foods[i]["fat"] for i in range(len(foods))) <= max_fat, "MaxFat")

fruits_vegetables_indices = [i for i, food in enumerate(foods) if food["group"] in ["fruit", "vegetable"]]
other_food_indices = [i for i, food in enumerate(foods) if food["group"] not in ["fruit", "vegetable", "junk"]]
grains_indices = [i for i, food in enumerate(foods) if food["group"] == "grain"]
proteins_indices = [i for i, food in enumerate(foods) if food["group"] == "protein"]
junk_indices = [i for i, food in enumerate(foods) if food["group"] == "junk"]

m.addConstr(2 * quicksum(x[i] for i in other_food_indices) == quicksum(x[i] for i in fruits_vegetables_indices), "FruitsVegToOtherRatio")
m.addConstr(1 * quicksum(x[i] for i in grains_indices) == 1 * quicksum(x[i] for i in proteins_indices), "GrainsToProteinsRatio")
m.addConstr(quicksum(x[i] for i in junk_indices) <= 1, "MaxOneServingJunkFood")

for i in range(len(foods)):
    m.addConstr(x[i] <= 2, f"MaxServings_{i}")


m.optimize()

if m.status == GRB.OPTIMAL:
    print("\n ---Optimal solution:---")
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0
    total_cost = 0
    
    for var in m.getVars():
        if var.x > 0:
            # Extract the index from the variable name, which is formatted as "x[i]"
            index = int(var.varName.split('[')[-1].split(']')[0])
            food = foods[index]
            print(f'{food["name"]}: {var.x:.2f} servings')
            total_calories += food["calories"] * var.x
            total_protein += food["protein"] * var.x
            total_carbs += food["carbs"] * var.x
            total_fat += food["fat"] * var.x
            total_cost += food["cost"] * var.x

    print("\nNutritional summary:")
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Total Calories: {total_calories:.2f}")
    print(f"Total Protein: {total_protein:.2f}g")
    print(f"Total Carbohydrates: {total_carbs:.2f}g")
    print(f"Total Fat: {total_fat:.2f}g")

    
else:
    print("No convergence")


# ---- Sensitivity Analysis ---- 
    
if want_sensitivity_report:
    print("Reduced Costs:")
    for var in m.getVars():
        if var.X > 0:  # Only print non-zero allocations (basic variables)
            print(f"{var.VarName}: Reduced Cost = {var.RC}")

    print("\nShadow Prices:")
    for constr in m.getConstrs():
        print(f"{constr.ConstrName}: Shadow Price = {constr.Pi}")

    print("\nObjective Coefficient Sensitivity:")
    for var in m.getVars():
        print(f"{var.VarName}: Coefficient can increase by {var.SAObjUp} and decrease by {var.SAObjLow}")

    print("\nConstraint RHS Sensitivity:")
    for constr in m.getConstrs():
        print(f"{constr.ConstrName}: RHS can increase by {constr.SARHSUp} and decrease by {constr.SARHSLow}")