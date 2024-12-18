import csv
import json
from collections import defaultdict

# Create a dictionary where each key is an int and each value is a list of strings
recipe_map = defaultdict(list)

# Open and read the CSV file
with open("Question1_B.csv", mode="r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row if there is one

    # Process each row
    for row in csv_reader:
        recipe_id = int(row[0])  # Convert Recipe ID to an integer
        ingredient = row[1].strip()  # Strip any extra whitespace around the ingredient name
        
        # Append the ingredient to the list for this Recipe ID
        recipe_map[recipe_id].append(ingredient)

# Convert to regular dict to save as JSON
recipe_map = dict(recipe_map)

# Write the dictionary to a JSON file
with open("recipe_data.json", "w") as json_file:
    json.dump(recipe_map, json_file, indent=4)

print("Recipe data has been saved to 'recipe_data.json'")
