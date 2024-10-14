import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the original recipe data
with open("recipe_data.json", "r") as file:
    original_recipes = json.load(file)

# Calculate the size (number of ingredients) for each recipe in the original cuisine
original_recipe_sizes = [len(ingredients) for ingredients in original_recipes.values()]

# Calculate the frequency of each recipe size
size_counts = pd.Series(original_recipe_sizes).value_counts().sort_index()

# Calculate percentages for original recipe sizes
total_original_recipes = size_counts.sum()
original_percentages = (size_counts / total_original_recipes) * 100

# Create a cumulative distribution function (CDF)
cdf = size_counts.cumsum() / size_counts.sum()

# Function to create random cuisines based on the ingredient frequency
def create_random_cuisines(num_sets=10, num_recipes_per_set=1000):
    random_cuisines = []
    for _ in range(num_sets):
        # Generate random sizes using the inverse transformation method
        random_samples = np.random.uniform(0, 1, num_recipes_per_set)  # Uniform random numbers
        new_sizes = np.searchsorted(cdf, random_samples)  # Inverse transform sampling
        random_cuisines.append(new_sizes)
    return random_cuisines

# Create 10 sets of random cuisines
random_cuisines = create_random_cuisines()

# Calculate percentages for random cuisines
random_percentages_list = []
for random_cuisine in random_cuisines:
    random_counts = pd.Series(random_cuisine).value_counts().sort_index()
    total_random_recipes = random_counts.sum()
    random_percentages = (random_counts / total_random_recipes) * 100
    random_percentages_list.append(random_percentages)

# Plotting the recipe size distribution
plt.figure(figsize=(12, 6))

# Plot Original Recipe Size Distribution with dots connected by lines
plt.plot(original_percentages.index, original_percentages.values, marker='o', linestyle='-', color='skyblue', markersize=8, label='Original Cuisine')

# Plot Random Recipe Size Distributions with dots connected by lines
for i, random_percentages in enumerate(random_percentages_list):
    plt.plot(random_percentages.index, random_percentages.values, marker='o', linestyle='-', markersize=5, label=f'Random Cuisine Set {i+1}')

# Customize the plot
plt.title('Recipe Size Distribution of Original and Random Cuisines')
plt.xlabel('Number of Ingredients')
plt.ylabel('Percentage of Recipes (%)')
plt.xticks(np.arange(0, max(original_recipe_sizes) + 1, 1))  # Adjust x-ticks
plt.grid(True)
plt.legend()
plt.savefig('Q3A.png')
plt.show()
