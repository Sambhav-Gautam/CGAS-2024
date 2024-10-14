import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the original recipe data
with open("recipe_data.json", "r") as file:
    original_recipes = json.load(file)

# Calculate the size (number of ingredients) for each recipe in the original cuisine
original_recipe_sizes = [len(ingredients) for ingredients in original_recipes.values()]

# Calculate the frequency of each recipe size for the original cuisine
original_size_counts = pd.Series(original_recipe_sizes).value_counts()

# Normalize frequencies to get proportions
total_count = original_size_counts.sum()
normalized_frequencies = original_size_counts / total_count

# Assign ranks based on frequency
ranks = range(1, len(normalized_frequencies) + 1)

# Plotting Frequency-Rank Distribution for Original Cuisine
plt.figure(figsize=(10, 6))
plt.plot(ranks, normalized_frequencies.sort_values(ascending=False), marker='o', linestyle='-', color='skyblue', markersize=8)
plt.title('Frequency-Rank Distribution of Original Cuisine')
plt.xlabel('Rank')
plt.ylabel('Normalized Frequency')
plt.xscale('log')  # Log scale for rank
plt.yscale('log')  # Log scale for frequency
plt.grid(True, which='both', linestyle='--', linewidth=0.7)

# Save the plot as PNG file
plt.savefig('frequency_rank_distribution_original_cuisine.png')
plt.show()

# Create 10 sets of random cuisines based on the original sizes
def create_random_cuisines(num_sets=10, num_recipes_per_set=1000):
    random_cuisines = []
    # Calculate the cumulative distribution function (CDF)
    cdf = original_size_counts.cumsum() / original_size_counts.sum()
    for _ in range(num_sets):
        # Generate random sizes using the inverse transformation method
        random_samples = np.random.uniform(0, 1, num_recipes_per_set)  # Uniform random numbers
        new_sizes = np.searchsorted(cdf, random_samples)  # Inverse transform sampling
        random_cuisines.append(new_sizes)
    return random_cuisines

# Create 10 sets of random cuisines
random_cuisines = create_random_cuisines()

# Frequency-rank distribution for random cuisines
random_freq_counts_list = []
random_rank_list = []
for random_cuisine in random_cuisines:
    random_freq_counts = pd.Series(random_cuisine).value_counts()
    total_count = random_freq_counts.sum()
    normalized_random_frequencies = random_freq_counts / total_count
    random_freq_counts_list.append(normalized_random_frequencies)
    random_rank_list.append(range(1, len(normalized_random_frequencies) + 1))

# Plotting Frequency-Rank Distribution for Random Cuisines
plt.figure(figsize=(12, 6))
for i, random_freq_counts in enumerate(random_freq_counts_list):
    plt.plot(random_rank_list[i], random_freq_counts.sort_values(ascending=False).values, marker='o', linestyle='-', markersize=5, label=f'Random Cuisine Set {i+1}')

# Customize the plot for random cuisines
plt.title('Frequency-Rank Distribution of Random Cuisines')
plt.xlabel('Rank')
plt.ylabel('Normalized Frequency')
plt.xscale('log')  # Log scale for rank
plt.yscale('log')  # Log scale for frequency
plt.grid(True, which='both', linestyle='--', linewidth=0.7)
plt.legend()
plt.savefig('frequency_rank_distribution_random_cuisines.png')
plt.show()
