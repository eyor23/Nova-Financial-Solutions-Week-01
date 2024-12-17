# stock_data.py
import pandas as pd

def load_stock_data(file_path):
    """
    Load stock price data into a DataFrame and ensure necessary columns are present.

    :param file_path: Path to the CSV file containing stock price data
    :return: DataFrame with stock price data
    :raises ValueError: If the data does not include the required columns
    """
    # Load the stock price data into a DataFrame
    data = pd.read_csv(file_path)  # Use the provided file_path argument
    # Ensure necessary columns are present
    required_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    if all(column in data.columns for column in required_columns):
        return data
    else:
        raise ValueError("Data must include Open, High, Low, Close, and Volume columns.")
