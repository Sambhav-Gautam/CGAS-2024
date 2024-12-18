# CGAS Assignment-1 Rubric

## Submission Guidelines:
- Name each Jupyter notebook according to the corresponding question number.
- Submit a zip folder containing:
  - Jupyter notebooks, PDFs, CSV files, and PNG images.
  - Handwritten answers for Questions 4-8 in a single scanned PDF.
- Filename convention: `Name_RollNo_Assignment1.zip` (2 marks deduction for non-compliance).
- **Plagiarism Policy:** 50% marks deduction for plagiarized content.

---

## Assignment Tasks:

### **1. Recipe Data Analysis**
1. **Data Scraping (5 Marks):**
   - Scrape 10,000 recipes from sources like allrecipes.com, tasteatlas.com, bbc.com.
   - Save data in CSV format with columns:
     - Recipe Name (0.5)
     - Recipe URL (0.5)
     - Ingredients (1.5)
     - Instructions (1.5)
     - Region/Cuisine, Servings, Preparation Time (Optional: 1)

2. **Ingredient Extraction (8 Marks):**
   - Assign random Recipe IDs.
   - Extract unique ingredients using Named Entity Recognition (SpaCy, Stanford NER).
   - Save results in CSV format.

3. **Recipe-Ingredient Storage (2 Marks):**
   - Save 100 randomly chosen recipes in `Recipe ID – Ingredient Name` format.

---

### **2. Data Analysis Tasks**
1. **Unique Ingredients (2 Marks):**
   - Count and list unique ingredients with frequencies.
   - Save results in a data frame.

2. **Recipe Size Distribution (3 Marks):**
   - Plot recipe size distribution and calculate average size.
   - Properly label axes and save plots as PNG.

3. **Cumulative Distribution Plot (5 Marks):**
   - Plot CDF of recipe size with properly labeled axes.
   - Save plots as PNG.

4. **Frequency-Rank Distribution (5 Marks):**
   - Plot normalized Freq-Rank Distribution.
   - Save plots as SVG and PNG.

---

### **3. Comparative & Descriptive Tasks**
1. **Nutritional Profile Comparison (2 Marks):**
   - Compare ‘Boiled Egg’ vs. ‘Boiled Rice and Daal’ on at least 2 points.

2. **Uncommon Ingredients (5 Marks):**
   - List 5 uncommon ingredients with:
     - Local/Common Name
     - English Name (if available)
     - Seasonal Use (if known)
     - Nutritional Value (if available)

3. **Scientific Arguments (3 Marks):**
   - Evaluate the following statements:
     - Does cooking in a microwave destroy nutritional value?
     - Does refrigeration destroy nutritional value?
     - Are genetic modifications in plants/animals harmful?

4. **Calorific Content Analysis (2 Marks):**
   - Summarize techniques for calculating food calorific content in 5-8 lines.

5. **Future Technologies (8 Marks):**
   - List 8 potential computational gastronomy-based technologies with 1-3 lines of description each.

---

**Ensure all files are properly labeled and saved as required. Follow the naming conventions strictly. Good luck!**