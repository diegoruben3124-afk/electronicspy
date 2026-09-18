"""
Basic usage example for electronicspy
Run:
    python basic_usage.py
"""
import electronicspy as spd
print("=== electronicspy: Basic Usage Example ===\n")

# Load a dataset

print("Loading 'electronics_dataset' dataset...")
electronics = ep.load_dataset("electronics_dataset")

# Show basic information

print("\nFirst 5 rows:")
print(electronics.head())
print("\nDataset shape:")
print(electronics.shape)
print("\nColumn names:")
print(list(electronics.columns))

# Load another dataset

print("\nLoading 'electronic_sales' dataset...")
electronicssale = ep.load_dataset("electronic_sales")
print("\nFirst 5 rows:")
print(electronicssale.head())
print("\nDone.")