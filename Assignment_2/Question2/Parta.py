import json
import random
import matplotlib.pyplot as plt
import pandas as pd

# Load the original recipe data
with open("recipe_data.json", "r") as file:
    original_recipes = json.load(file)

# Calculate the size (number of ingredients) for each recipe in the original cuisine
original_recipe_sizes = [len(ingredients) for ingredients in original_recipes.values()]

# Calculate the counts and percentages for the original recipe sizes
original_counts = pd.Series(original_recipe_sizes).value_counts().sort_index()
total_original_recipes = original_counts.sum()
original_percentages = (original_counts / total_original_recipes) * 100

# a) Create a size-controlled replica for each recipe with a random ingredient count
replicated_recipes_sizes = []
for _ in range(10):  # 10 sets of random sizes
    for size in original_recipe_sizes:
        random_size = max(1, int(size * random.uniform(0.5, 1.5)))  # Random size between 50% and 150% of original size
        replicated_recipes_sizes.append(random_size)

# Calculate the counts and percentages for the replicated recipe sizes
replicated_counts = pd.Series(replicated_recipes_sizes).value_counts().sort_index()
total_replicated_recipes = replicated_counts.sum()
replicated_percentages = (replicated_counts / total_replicated_recipes) * 100

# Plot 1: Original Recipe Size Distribution with dots connected by lines (percentages)
plt.figure(figsize=(10, 6))
plt.plot(original_percentages.index, original_percentages.values, marker='o', linestyle='-', color='b', markersize=8)
plt.title("Original Cuisine Recipe Size Distribution (Percentage)")
plt.xlabel("Recipe Size (Number of Ingredients)")
plt.ylabel("Percentage of Recipes (%)")
plt.xticks(original_percentages.index)
plt.grid(True)
plt.savefig("original_recipe_size_distribution_percentage.png")
plt.show()

# Plot 2: Randomly Created Recipe Size Distribution with dots connected by lines (percentages)
plt.figure(figsize=(10, 6))
plt.plot(replicated_percentages.index, replicated_percentages.values, marker='o', linestyle='-', color='r', markersize=8)
plt.title("Randomly Created Recipe Size Distribution (Percentage)")
plt.xlabel("Recipe Size (Number of Ingredients)")
plt.ylabel("Percentage of Recipes (%)")
plt.xticks(replicated_percentages.index)
plt.grid(True)
plt.savefig("randomly_created_recipe_size_distribution_percentage.png")
plt.show()

# Calculate and print the average size of the recipes (rounded to the nearest integer)
average_original_size = round(pd.Series(original_recipe_sizes).mean())
average_replicated_size = round(pd.Series(replicated_recipes_sizes).mean())
print(f"Average size of the original recipes (rounded to the nearest integer): {average_original_size}")
print(f"Average size of the replicated recipes (rounded to the nearest integer): {average_replicated_size}")
