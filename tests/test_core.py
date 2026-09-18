import pandas as pd
import pytest
from electronicspy.core import list_datasets, load_dataset


def test_list_datasets_returns_list():
    datasets = list_datasets()
    assert isinstance(datasets, list)


def test_list_datasets_not_empty():
    datasets = list_datasets()
    assert len(datasets) > 0


def test_list_datasets_sorted():
    datasets = list_datasets()
    assert datasets == sorted(datasets)


def test_load_dataset_returns_dataframe():
    name = list_datasets()[0]
    df = load_dataset(name)
    assert isinstance(df, pd.DataFrame)


def test_load_dataset_invalid_name():
    with pytest.raises(ValueError):
        load_dataset("this_dataset_does_not_exist")


def test_load_dataset_file_not_found(monkeypatch):
    """
    Test that FileNotFoundError is raised when the CSV file doesn't exist.
    """
    from pathlib import Path
    from electronicspy.datasets import DATASETS
    
    # Get a valid dataset name that exists in DATASETS
    valid_dataset = list_datasets()[0]
    
    # Mock Path.exists to return False (simulating missing file)
    def mock_exists(self):
        return False
    
    monkeypatch.setattr(Path, "exists", mock_exists)
    
    with pytest.raises(FileNotFoundError, match="Dataset file not found"):
        load_dataset(valid_dataset)