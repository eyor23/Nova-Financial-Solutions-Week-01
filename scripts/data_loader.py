import pandas as pd
import yaml

def load_config(config_file='../config.yaml'):
    """
    Load configuration from a YAML file.
    """
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

def load_data(file_path):
    """
    Load dataset from a CSV file.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Dataset loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def inspect_data(data):
    """
    Display dataset structure and basic information.
    """
    print(data.info())
    print(data.head())

def handle_missing_values(data):
    """
    Handle missing values in the dataset.
    """
    missing_counts = data.isnull().sum()
    print("Missing values per column:\n", missing_counts)
    # Drop rows with missing values for simplicity
    data_cleaned = data.dropna()
    print(f"Dataset after dropping missing values: {data_cleaned.shape[0]} rows.")
    return data_cleaned