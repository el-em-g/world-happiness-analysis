# Claude Code Configuration

This directory contains Claude Code hooks and commands for the World Happiness Analysis project.

## Session Start Hook

**File:** `.claude/hooks/session-start.sh`

Automatically runs when you start a Claude Code session on the web. It:
- Sets up the Python environment (PYTHONPATH)
- Installs dependencies from `requirements.txt` if present

## Commands

### `/quick-eda` - Quick Exploratory Data Analysis

Performs a comprehensive exploratory data analysis on the World Happiness dataset.

**Usage:**
```
/quick-eda
```

**What it does:**
- Loads and analyzes the `world_happiness_combined.csv` dataset
- Shows dataset overview (shape, columns, data types)
- Reports data quality issues (missing values, duplicates)
- Displays summary statistics
- Identifies top 10 happiest and bottom 10 countries
- Compares happiness across regions
- Shows countries with biggest happiness changes over time
- Analyzes correlations between happiness and key factors

**Direct script usage:**
You can also run the EDA script directly:
```bash
python3 .claude/scripts/quick_eda.py
```

## Dependencies

Dependencies are defined in `requirements.txt`:
- pandas
- numpy
- matplotlib
- seaborn

These are automatically installed by the session start hook when using Claude Code on the web.
