# electronicspy Documentation

## Welcome

The `electronicspy` package provides a curated collection of electronics and consumer-technology
datasets for data analysis, statistical modeling, and machine learning
research. It includes datasets related to **online marketplace product data,
e-commerce sales transactions, customer purchase behavior, and historical stock
prices for major electronics companies**.

The package contains datasets related to electronics product pricing and
specifications scraped from online marketplaces, customer purchase behavior and
sales transactions for an electronics company, and Samsung Electronics'
historical stock price data, all curated from Kaggle.

### Philosophy

The author's vision is to create **specialized dataset packages** focused on specific themes and topics. Instead of searching through multiple generic data packages to find relevant datasets, users can go directly to a thematic package where all datasets are carefully curated around a particular subject.

In the case of `electronicspy`, every dataset is **exclusively focused on
electronics and consumer-technology research**, making it the go-to resource for
researchers, data scientists, statisticians, retail analysts, and students working in
the fields of e-commerce, market analysis, financial analysis, and machine learning.


## Getting Started

### Installation

#### From PyPI (Recommended)

The easiest way to install `electronicspy` is directly from PyPI:
```bash
pip install electronicspy
```

#### From GitHub (Latest Development Version)

To get the latest development version with the newest features and bug fixes:
```bash
pip install git+https://github.com/diegoruben3124-afk/electronicspy
```

### Quick Start Tutorial

#### 1. Import the Package
```python
import electronicspy as ep
```

#### 2. List Available Datasets

See all datasets included in the package:
```python
# Get list of all datasets
datasets = ep.list_datasets()
print(datasets)
```

#### 3. Load a Dataset

Load any dataset as a pandas DataFrame:
```python
# Load electronics_dataset
df = ep.load_dataset('electronics_dataset')

# Display first rows
print(df.head())

# Check dataset dimensions
print(f"Shape: {df.shape}")
```

#### 4. Describe a dataset

```python

# Describe a dataset
print(ep.describe("electronics_dataset"))

```

### Basic Concepts

#### Dataset Naming Convention

All dataset names in `electronicspy` follow a consistent naming pattern:

- Lowercase with underscores: `electronic_sales`
- Descriptive names that reflect content


#### Some Datasets available at `electronicspy`

Every dataset is **exclusively focused on electronics and consumer-technology topics for
data analysis, statistical modeling, and machine learning**:

- **electronics_dataset**: Product and pricing data scraped from an online electronics marketplace.
- **electronic_sales**: Sales transaction records for an electronics company (Sep 2023–Sep 2024), including customer demographics, product types, and purchase behaviors.
- **samsung_electronics_stocks**: Historical stock price data for Samsung Electronics, including opening/closing prices, daily highs and lows, and trading volume.

> **Disclaimer:** The datasets included in `electronicspy` are provided strictly for
> educational, research, and informational purposes. For financial advice, investment
> decisions, or any data-driven business decision-making, always consult a qualified
> professional.


#### Data Licenses

All datasets are sourced from Kaggle and maintain their original open-source licenses:

- Most datasets use **CC0: Public Domain**
- Some use **MIT**
- The `electronicspy` package itself is licensed under **MIT**