import random
import matplotlib.pyplot as plt
import pandas as pd

def monte_carlo_dice_simulation(num_rolls=100000):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        sums_count[roll_sum] += 1

    probabilities = {sum_: (count / num_rolls) * 100 for sum_, count in sums_count.items()}
    
    return probabilities

num_rolls = 100000
probabilities = monte_carlo_dice_simulation(num_rolls)

results_df = pd.DataFrame(list(probabilities.items()), columns=['Sum', 'Probability (%)'])
print(results_df)

plt.figure(figsize=(10, 6))
plt.bar(results_df['Sum'], results_df['Probability (%)'], color='skyblue')
plt.xlabel('Sum of Two Dice')
plt.ylabel('Probability (%)')
plt.title(f'Probability Distribution of Dice Sums (Monte Carlo - {num_rolls} rolls)')
plt.xticks(range(2, 13))
plt.show()
