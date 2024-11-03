def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []

    for item, details in sorted_items:
        if details['cost'] <= budget:
            selected_items.append(item)
            total_calories += details['calories']
            budget -= details['cost']

    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]

    for i in range(n):
        item, details = list(items.items())[i]
        cost = details['cost']
        calories = details['calories']
        for j in range(budget, cost - 1, -1):
            if dp[j] < dp[j - cost] + calories:
                dp[j] = dp[j - cost] + calories
                selected_items[j] = selected_items[j - cost] + [item]

    max_calories = dp[budget]
    best_combination = selected_items[budget]

    return best_combination, max_calories

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 200},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

selected_items, total_calories = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected items:", selected_items)
print("Total calories:", total_calories)

selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("\nDynamic Programming:")
print("Selected items (DP):", selected_items_dp)
print("Total calories (DP):", total_calories_dp)
