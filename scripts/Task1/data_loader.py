import pandas as pd
import yaml
import os


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

def load_stock_data(file_paths):
    """
    Load multiple stock data files from a list of file paths.
    """
    stock_data = {}

    for file_path in file_paths:
        try:
            data = pd.read_csv(file_path)
            stock_name = file_path.split('/')[-1].split('_')[0]  # Extract stock name from the file path
            stock_data[stock_name] = data
            print(f"Loaded data for {stock_name} from {file_path} with {data.shape[0]} rows and {data.shape[1]} columns.")
        except Exception as e:
            print(f"Error loading {file_path}: {e}")

    return stock_data

import yfinance as yf
import pandas as pd

def load_stock_data(ticker, start_date, end_date):
    """
    Load historical stock data for a specific ticker.
    :param ticker: Stock ticker symbol (e.g., 'AAPL' for Apple)
    :param start_date: Start date in 'YYYY-MM-DD' format
    :param end_date: End date in 'YYYY-MM-DD' format
    :return: DataFrame containing stock price data
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    data.reset_index(inplace=True)
    return data
