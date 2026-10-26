def budget_remaining (budget, food, transport):
    budgets = budget - food - transport
    return budgets

def message (name, remaining):
    return f"{name} has {remaining} naira remaining."

budget_final = budget_remaining(2000, 500, 300)
print(budget_final)

final_message = message ("Viyon", budget_final)
print (final_message)