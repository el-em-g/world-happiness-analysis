#!/usr/bin/env python3
"""
Quick Exploratory Data Analysis for World Happiness Dataset
"""

import sys
from pathlib import Path

try:
    import pandas as pd
    import numpy as np
except ImportError:
    print("Error: Required packages not installed.")
    print("Please install: pip install pandas numpy")
    sys.exit(1)


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80 + "\n")


def quick_eda():
    """Perform quick exploratory data analysis on World Happiness dataset"""

    # Load data
    data_file = Path(__file__).parent.parent.parent / "world_happiness_combined.csv"

    if not data_file.exists():
        print(f"Error: Data file not found at {data_file}")
        return

    print_section("WORLD HAPPINESS DATASET - QUICK EDA")

    try:
        # Try reading with semicolon delimiter and comma as decimal
        df = pd.read_csv(data_file, sep=';', decimal=',')
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # 1. Basic Information
    print_section("1. DATASET OVERVIEW")
    print(f"Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
    print(f"\nColumns: {', '.join(df.columns.tolist())}")

    # 2. Data Types and Missing Values
    print_section("2. DATA QUALITY")
    print("\nColumn Information:")
    info_df = pd.DataFrame({
        'Column': df.columns,
        'Type': df.dtypes.values,
        'Non-Null': df.count().values,
        'Missing': df.isnull().sum().values,
        'Missing %': (df.isnull().sum() / len(df) * 100).round(2).values
    })
    print(info_df.to_string(index=False))

    # Check for duplicates
    duplicates = df.duplicated().sum()
    print(f"\nDuplicate rows: {duplicates}")

    # 3. Summary Statistics
    print_section("3. SUMMARY STATISTICS")
    print(df.describe().round(3).to_string())

    # 4. Top Insights
    print_section("4. KEY INSIGHTS")

    # Identify year column (might be 'year' or 'Year')
    year_col = None
    for col in ['year', 'Year', 'YEAR']:
        if col in df.columns:
            year_col = col
            break

    if year_col:
        years = sorted(df[year_col].unique())
        print(f"Years covered: {min(years)} - {max(years)}")

    # Determine happiness score column name
    happiness_col = None
    for col in ['Ladder score', 'Happiness score', 'Score']:
        if col in df.columns:
            happiness_col = col
            break

    # Top 10 happiest countries (overall average)
    if 'Country' in df.columns and happiness_col:
        print(f"\n📊 Top 10 Happiest Countries (Average):")
        top_happy = df.groupby('Country')[happiness_col].mean().sort_values(ascending=False).head(10)
        for i, (country, score) in enumerate(top_happy.items(), 1):
            print(f"  {i:2d}. {country:<30} {score:.3f}")

        print(f"\n📉 Bottom 10 Countries (Average):")
        bottom_happy = df.groupby('Country')[happiness_col].mean().sort_values().head(10)
        for i, (country, score) in enumerate(bottom_happy.items(), 1):
            print(f"  {i:2d}. {country:<30} {score:.3f}")

    # Regional comparison
    if 'Regional indicator' in df.columns and happiness_col:
        print("\n🌍 Regional Happiness Averages:")
        regional = df.groupby('Regional indicator')[happiness_col].mean().sort_values(ascending=False)
        for region, score in regional.items():
            print(f"  {region:<50} {score:.3f}")

    # Biggest changes over time
    if year_col and 'Country' in df.columns and happiness_col:
        print("\n📈 Countries with Biggest Happiness Improvements:")
        pivot = df.pivot_table(values=happiness_col, index='Country', columns=year_col)
        if len(pivot.columns) >= 2:
            first_year = pivot.columns.min()
            last_year = pivot.columns.max()
            changes = (pivot[last_year] - pivot[first_year]).dropna().sort_values(ascending=False)

            print(f"\n  Top 5 Improvers ({first_year} to {last_year}):")
            for country, change in changes.head(5).items():
                print(f"    {country:<30} +{change:.3f}")

            print(f"\n  Top 5 Decliners ({first_year} to {last_year}):")
            for country, change in changes.tail(5).items():
                print(f"    {country:<30} {change:.3f}")

    # 5. Correlations
    print_section("5. CORRELATION ANALYSIS")

    # Key factors to examine (using flexible happiness column)
    factor_cols = [
        happiness_col, 'GDP per capita', 'Social support',
        'Healthy life expectancy', 'Freedom to make life choices',
        'Generosity', 'Perceptions of corruption'
    ]

    # Filter to columns that exist (and remove None values)
    available_cols = [col for col in factor_cols if col and col in df.columns]

    if len(available_cols) >= 2 and happiness_col:
        corr_matrix = df[available_cols].corr()[happiness_col].sort_values(ascending=False)

        print(f"Correlation with Happiness Score ({happiness_col}):\n")
        for factor, corr in corr_matrix.items():
            if factor != happiness_col:
                bar = '█' * int(abs(corr) * 20)
                sign = '+' if corr > 0 else '-'
                print(f"  {factor:<35} {sign}{abs(corr):.3f}  {bar}")

    print("\n" + "=" * 80)
    print("  EDA Complete!")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    quick_eda()
