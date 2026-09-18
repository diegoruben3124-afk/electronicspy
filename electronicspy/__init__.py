"""
electronicspy
A Python package providing electronics and consumer-technology datasets in CSV format from curated Kaggle datasets.
"""

__version__ = "0.1.0"

from .core import load_dataset, list_datasets, describe
from .datasets import DATASETS

__all__ = [
    "load_dataset",
    "list_datasets",
    "describe",
    "DATASETS",
    "__version__",
]