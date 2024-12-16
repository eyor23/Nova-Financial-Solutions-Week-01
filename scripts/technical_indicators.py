import talib

def calculate_indicators(df):
    """
    Calculate basic technical indicators using TA-Lib.

    :param df: DataFrame containing stock data
    :return: DataFrame with new technical indicators
    """
    df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)  # Simple Moving Average
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)     # Relative Strength Index
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(df['Close'],
                                                                fastperiod=12,
                                                                slowperiod=26,
                                                                signalperiod=9)
    return df
