# electronicspy – Examples

This page provides practical examples of using `electronicspy` for data analysis and exploration.

## Basic Examples

### Example 1: Loading and Exploring a Dataset

Learn how to load a dataset and perform basic exploration.

```python
import electronicspy as ep

# Load product and pricing data scraped from an online electronics marketplace.
electronics_001 = ep.load_dataset("electronics_dataset")

# Display first few rows
print(electronics_001.head())

# Check dataset shape
print(f"\nDataset shape: {electronics_001.shape}")

# View column names
print(f"\nColumns: {list(electronics_001.columns)}")

# Get summary statistics
print("\nSummary statistics:")
print(electronics_001.describe())

# Check for missing values
print("\nMissing values:")
print(electronics_001.isnull().sum())

```

### Example 2: Exploring Customer purchase behavior - Electronic Sales Data

```python

import electronicspy as ep

sales_001 = ep.load_dataset("electronic_sales")
print(sales_001.head())
print(f"\nDataset shape: {sales_001.shape}")
print(f"\nColumns: {list(sales_001.columns)}")

```

### Example 3: Exploring Samsung Electronics Historical Stock Prices

```python

import electronicspy as ep

stocks_001 = ep.load_dataset("samsung_electronics_stocks")
print(stocks_001.head())
print(f"\nDataset shape: {stocks_001.shape}")
print(f"\nColumns: {list(stocks_001.columns)}")

```

### Example 4: Listing all available datasets

```python

import electronicspy as ep

datasets = ep.list_datasets()
print(datasets)

```