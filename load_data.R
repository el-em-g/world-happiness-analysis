# Load World Happiness Data in R/RStudio
# ========================================

# Option 1: Using base R
df <- read.csv("world_happiness_combined_r.csv")

# Option 2: Using readr (recommended - faster and better defaults)
# install.packages("readr")  # Run once if not installed
library(readr)
df <- read_csv("world_happiness_combined_r.csv")

# Option 3: Using data.table (fastest for large datasets)
# install.packages("data.table")  # Run once if not installed
library(data.table)
df <- fread("world_happiness_combined_r.csv")

# View the data
head(df)
str(df)
summary(df)

# Quick check
cat(sprintf("Loaded %d rows and %d columns\n", nrow(df), ncol(df)))
cat(sprintf("Years covered: %d to %d\n", min(df$Year), max(df$Year)))
