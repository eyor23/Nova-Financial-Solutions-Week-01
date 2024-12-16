import pynance as pn

def calculate_financial_metrics(df):
    """
    Use PyNance to calculate financial metrics.

    :param df: DataFrame containing stock data
    :return: Dictionary of financial metrics
    """
    metrics = {
        'daily_return': pn.metrics.daily_returns(df['Close']),
        'cumulative_return': pn.metrics.cumulative_returns(df['Close']),
        'volatility': pn.metrics.volatility(df['Close']),
    }
    return metrics
