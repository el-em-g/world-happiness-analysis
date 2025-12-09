#!/usr/bin/env python3
"""
Convert world_happiness_combined.csv to R-friendly format
- Changes semicolon delimiter to comma
- Changes comma decimal separator to period
"""

import pandas as pd
from pathlib import Path

# File paths
project_dir = Path(__file__).parent.parent.parent
input_file = project_dir / "world_happiness_combined.csv"
output_file = project_dir / "world_happiness_combined_r.csv"

print(f"Reading {input_file}...")
# Read with European format
df = pd.read_csv(input_file, sep=';', decimal=',')

print(f"Dataset shape: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"\nWriting R-friendly format to {output_file}...")

# Write with standard format (comma delimiter, period decimal)
df.to_csv(output_file, index=False)

print("✓ Conversion complete!")
print("\nYou can now read this in R with:")
print(f'  df <- read.csv("{output_file.name}")')
print("or")
print(f'  library(readr)')
print(f'  df <- read_csv("{output_file.name}")')
