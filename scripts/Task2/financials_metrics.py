import pandas as pd
import yfinance as yf

def calculate_financial_metrics(tickers):
    """
    Calculate financial metrics using yfinance.

    :param tickers: List of stock ticker symbols
    :return: Dictionary of financial metrics
    """
    metrics = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1y")
        daily_return = hist['Close'].pct_change()
        cumulative_return = (1 + daily_return).cumprod() - 1
        volatility = daily_return.std()

        metrics[ticker] = {
            'daily_return': daily_return,
            'cumulative_return': cumulative_return,
            'volatility': volatility
        }
    return metrics

