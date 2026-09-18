"""
Datasets registry for electronicspy.
"""

DATASETS = {
    "electronics_dataset": {
        "filename": "electronics_dataset.csv",
        "source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/elvinrustam/electronics-dataset", 
        "license": "CC0: Public Domain",
        "description": "Electronics product data scraped from Costco's online marketplace."
    },

    "electronic_sales": {
        "filename": "electronic_sales.csv",
        "source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/cameronseamons/electronic-sales-sep2023-sep2024",
        "license": "MIT",
        "description": "One year of electronics sales transactions, including customer demographics, products, and purchase behavior."
    },

    "samsung_electronics_stocks": {
        "filename": "samsung_electronics_stocks.csv",
        "source": "Kaggle",
        "url": "hhttps://www.kaggle.com/datasets/sameerramzan/samsung-electronics-historical-stock-prices",
        "license": "CC0: Public Domain",
        "description": "Historical Samsung Electronics stock data, including prices, highs, lows, and trading volume."
    }

}

__all__ = ["DATASETS"]
