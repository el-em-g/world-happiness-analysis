---
description: Perform a quick exploratory data analysis on the World Happiness dataset
---

# Quick EDA - World Happiness Dataset

Perform a comprehensive exploratory data analysis on the World Happiness dataset. Use the Python script at `.claude/scripts/quick_eda.py` if it exists, otherwise perform the analysis directly.

## Analysis Steps:

1. **Load the data**: Use the `world_happiness_combined.csv` file
2. **Basic info**:
   - Dataset shape (rows, columns)
   - Column names and data types
   - Missing values summary
   - Date range covered

3. **Summary statistics**:
   - Display descriptive statistics for numerical columns
   - Identify outliers in key metrics (Ladder score, GDP, etc.)

4. **Top insights**:
   - Top 10 happiest countries (overall and by year)
   - Bottom 10 happiest countries
   - Countries with biggest happiness score changes over time
   - Regional happiness comparison

5. **Data quality**:
   - Check for duplicates
   - Identify any data quality issues
   - Report on completeness

6. **Key correlations**:
   - Show correlation between happiness score and key factors (GDP, social support, etc.)
   - Highlight strongest relationships

Present the results in a clear, readable format with markdown tables and brief commentary.
