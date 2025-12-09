# World Happiness Analysis

Dataset and analysis tools for the World Happiness Report (2015-2024).

## Dataset Files

- **`world_happiness_combined.csv`** - Original dataset (European format: semicolon-delimited, comma decimals)
- **`world_happiness_combined_r.csv`** - R/RStudio-friendly format (comma-delimited, period decimals)
- Individual year files: `world_happiness_2015.csv` through `world_happiness_2024.csv`

## Using in RStudio

The `world_happiness_combined_r.csv` file is formatted for easy use in R:

```r
# Load the data
df <- read.csv("world_happiness_combined_r.csv")

# Or using readr for better performance
library(readr)
df <- read_csv("world_happiness_combined_r.csv")
```

See `load_data.R` for more examples.

## Using in Python

```python
import pandas as pd

# For the original file
df = pd.read_csv("world_happiness_combined.csv", sep=';', decimal=',')

# For the R-friendly file
df = pd.read_csv("world_happiness_combined_r.csv")
```

## Quick EDA

Run exploratory data analysis:

```bash
python3 .claude/scripts/quick_eda.py
```

Or use the `/quick-eda` command in Claude Code.

## Data Description

See `Readme.txt` for detailed information about the dataset structure, columns, and usage policies.
