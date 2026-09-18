# electronicspy

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

The `electronicspy` package provides a curated collection of electronics and consumer-technology
datasets for data analysis, statistical modeling, and machine learning research. Includes retail
and marketplace product data, e-commerce sales transactions and customer purchase behavior, and
historical stock prices for major electronics companies, sourced from curated datasets on Kaggle.

## Installation

You can install the `electronicspy` package from PyPI:
```bash
pip install electronicspy
```

## Usage
```python

import electronicspy as ep

# List all available datasets

datasets = ep.list_datasets()
print(datasets)

# Load a specific dataset

df = ep.load_dataset('electronics_dataset')
print(df.head())

# Describe dataset

df_01 = ep.describe('electronic_sales')
print(df_01)

```

## 📊 Some Available Datasets

| Dataset | Description |
|---------|-------------|
| `electronics_dataset` | Product and pricing data scraped from an online electronics marketplace. |
| `electronic_sales` | Sales transaction records for an electronics company (Sep 2023–Sep 2024), including customer demographics, product types, and purchase behavior. |
| `samsung_electronics_stocks` | Historical stock price data for Samsung Electronics, including opening/closing prices, daily highs and lows, and trading volume. |

> Run `electronicspy.list_datasets()` or `ep.list_datasets()` (using `ep` as alias) to see the full list of available datasets.

## Disclaimer

The datasets included in `electronicspy` are provided strictly for educational,
research, and informational purposes. All datasets originate from curated sources
on Kaggle and retain their original licenses and attributions.

The author of `electronicspy` makes no warranties, express or implied, regarding
the accuracy, completeness, or suitability of any dataset for a particular purpose.
Users are solely responsible for ensuring that their use of these datasets complies
with applicable licenses, laws, and ethical guidelines.

Any findings, conclusions, or decisions derived from the use of these datasets
are the sole responsibility of the user. The author shall not be held liable for
any direct, indirect, incidental, or consequential damages arising from the use
or misuse of the datasets included in this library.

## License

The `electronicspy` library is released under the **MIT License**, which allows free use,
modification, and distribution, including in proprietary software, provided that the
original copyright notice and license are included. See the [LICENSE](LICENSE) file for details.