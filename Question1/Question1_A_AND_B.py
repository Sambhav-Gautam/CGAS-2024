import json
import csv
from itertools import combinations
from collections import Counter

# Load the JSON data
with open("recipe_data.json", "r") as file:
    data = json.load(file)

# Convert data to a list of lists (one list per recipe's ingredients)
transactions = list(data.values())

# Function to generate itemsets and count frequencies
def get_frequent_itemsets(transactions, size):
    itemsets = []
    for transaction in transactions:
        # Generate itemsets of the specified size
        itemsets.extend(combinations(sorted(set(transaction)), size))
    # Count occurrences of each itemset
    itemset_counts = Counter(itemsets)
    return itemset_counts

# Generate itemsets of size one, two, and three
size_1_itemsets = get_frequent_itemsets(transactions, 1)
size_2_itemsets = get_frequent_itemsets(transactions, 2)
size_3_itemsets = get_frequent_itemsets(transactions, 3)

# Function to save itemsets to CSV
def save_itemsets_to_csv(itemsets, filename):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Itemset", "Frequency"])
        for itemset, count in itemsets.items():
            writer.writerow([", ".join(itemset), count])

# (a) Save complete lists of itemsets of size one, two, and three
save_itemsets_to_csv(size_1_itemsets, "itemsets_size_1.csv")
save_itemsets_to_csv(size_2_itemsets, "itemsets_size_2.csv")
save_itemsets_to_csv(size_3_itemsets, "itemsets_size_3.csv")

# (b) Get the top 20 itemsets for each size
top_20_size_1 = size_1_itemsets.most_common(20)
top_20_size_2 = size_2_itemsets.most_common(20)
top_20_size_3 = size_3_itemsets.most_common(20)

# Function to save top 20 itemsets to CSV
def save_top_itemsets_to_csv(top_itemsets, filename):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Itemset", "Frequency"])
        for itemset, count in top_itemsets:
            writer.writerow([", ".join(itemset), count])

# Save top 20 itemsets for each size to CSV
save_top_itemsets_to_csv(top_20_size_1, "top_20_itemsets_size_1.csv")
save_top_itemsets_to_csv(top_20_size_2, "top_20_itemsets_size_2.csv")
save_top_itemsets_to_csv(top_20_size_3, "top_20_itemsets_size_3.csv")

# Print the top 20 itemsets
print("\nTop 20 item sets of size 1:")
for itemset, count in top_20_size_1:
    print(f"{itemset}: {count}")

print("\nTop 20 item sets of size 2:")
for itemset, count in top_20_size_2:
    print(f"{itemset}: {count}")

print("\nTop 20 item sets of size 3:")
for itemset, count in top_20_size_3:
    print(f"{itemset}: {count}")
