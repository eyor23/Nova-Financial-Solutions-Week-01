import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import re
import pynance
import talib

def plot_sentiment_analysis(data, sentiment_column, sample_size=None):
    """
    Plots a bar chart for sentiment analysis distribution.

    :param data: DataFrame containing the sentiment data
    :param sentiment_column: Name of the column with sentiment values
    :param sample_size: Number of random samples to process (default is None to process all)
    """
    if sample_size is not None:
        data = data.sample(n=sample_size, random_state=1)  # Random sampling

    plt.figure(figsize=(8, 6))
    data[sentiment_column].value_counts().plot(kind='bar', color=['green', 'gray', 'red'])
    plt.title('Sentiment Analysis Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Frequency')
    plt.show()

def plot_word_cloud(data, text_column, sample_size=None):
    """
    Plots a word cloud for the most frequent keywords in a text column.

    :param data: DataFrame containing the text data
    :param text_column: Name of the column containing text
    :param sample_size: Number of random samples to process (default is None to process all)
    """
    if sample_size is not None:
        data = data.sample(n=sample_size, random_state=1)  # Random sampling

    if text_column not in data.columns:
        raise ValueError(f"Column '{text_column}' does not exist in the DataFrame.")

    if data[text_column].empty:
        raise ValueError("The provided text column is empty.")

    text = " ".join(data[text_column].dropna())  # Handle NaN values
    cleaned_text = re.sub(r'[^A-Za-z0-9\s]', '', text).lower()

    # Count the frequency of each word
    word_counts = Counter(cleaned_text.split())

    # Get the top 5 words
    top_5_words = dict(word_counts.most_common(5))
    print(f"Top 5 words: {top_5_words}")

    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(top_5_words)

    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Top 5 Frequent Keywords in Headlines')
    plt.show()

def plot_time_series(data, date_col, sample_size=None):
    """
    Plots a time series analysis of publication frequency over time.

    :param data: DataFrame containing the date data
    :param date_column: Date
    :param sample_size: Number of random samples to process (default is None to process all)
    """
    if sample_size is not None:
        data = data.sample(n=sample_size, random_state=1)  # Random sampling

    plt.figure(figsize=(10, 6))
    data[date_col] = pd.to_datetime(data[date_col], errors='coerce')
    data.dropna(subset=[date_col], inplace=True)
    data['month'] = data[date_col].dt.to_period('M')
    monthly_counts = data.groupby('month').size()
    monthly_counts.plot(kind='line')
    plt.title('Publication Frequency Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles')
    plt.grid()
    plt.show()

def plot_publisher_contribution(data, publisher_column, top_n=5, sample_size=None):
    """
    Plots a bar chart for the top N publishers by article count.

    :param data: DataFrame containing the publisher data
    :param publisher_column: Publisher column name
    :param top_n: Number of top publishers to display
    :param sample_size: Number of random samples to process (default is None to process all)
    """
    if sample_size is not None:
        data = data.sample(n=sample_size, random_state=1)  # Random sampling

    plt.figure(figsize=(10, 6))
    top_publishers = data[publisher_column].value_counts().head(top_n)
    top_publishers.plot(kind='bar', color='skyblue')
    plt.title(f'Top {top_n} Publishers by Article Count')
    plt.xlabel('Publisher')
    plt.ylabel('Number of Articles')
    plt.show()

def plot_stock_article_count(data, stock_column, sample_size=None):
    """
    Plots the number of articles for each stock.

    :param data: DataFrame containing the stock data
    :param stock_column: Name of the column with stock names
    :param sample_size: Number of random samples to process (default is None to process all)
    """
    if sample_size is not None:
        data = data.sample(n=sample_size, random_state=1)  # Random sampling

    plt.figure(figsize=(10, 6))
    stock_counts = data[stock_column].value_counts()
    stock_counts.plot(kind='bar', color='lightblue')
    plt.title('Number of Articles per Stock')
    plt.xlabel('Stock')
    plt.ylabel('Number of Articles')
    plt.show()

def plot_word_cloud_top_stocks(data, text_column, stock_column, top_n=5, sample_size=None):
    """
    Plots word clouds for the top N stocks by article count.

    :param data: DataFrame containing the text and stock data
    :param text_column: Name of the column with text data
    :param stock_column: Name of the column with stock names
    :param top_n: Number of top stocks to visualize
    :param sample_size: Number of random samples to process (default is None to process all)
    """
    if sample_size is not None:
        data = data.sample(n=sample_size, random_state=1)  # Random sampling

    top_stocks = data[stock_column].value_counts().head(top_n).index
    for stock in top_stocks:
        stock_data = data[data[stock_column] == stock]
        text = " ".join(stock_data[text_column])
        cleaned_text = re.sub(r'[^A-Za-z0-9\s]', '', text)
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(cleaned_text)
        plt.figure(figsize=(12, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'Frequent Keywords in Headlines for {stock}')
        plt.show()

import matplotlib.pyplot as plt

def plot_technical_indicators(df, stock_name):
    """
    Plot stock data with technical indicators.

    :param df: DataFrame containing stock data with indicators
    :param stock_name: Name of the stock
    """
    plt.figure(figsize=(14, 8))
    plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
    plt.plot(df['Date'], df['SMA_20'], label='SMA 20', color='orange')
    plt.title(f'{stock_name} - Technical Indicators')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def plot_financial_metrics(metrics, stock_name):
    """
    Plot financial metrics such as daily and cumulative returns.

    :param metrics: Dictionary of financial metrics
    :param stock_name: Name of the stock
    """
    plt.figure(figsize=(14, 8))
    plt.plot(metrics['daily_return'], label='Daily Returns', color='green')
    plt.plot(metrics['cumulative_return'], label='Cumulative Returns', color='red')
    plt.title(f'{stock_name} - Financial Metrics')
    plt.xlabel('Date')
    plt.ylabel('Return')
    plt.legend()
    plt.show()

import matplotlib.pyplot as plt

def plot_ta_indicators(df):
    """
    Plot technical indicators: SMA, RSI, MACD.
    
    :param df: DataFrame containing stock data with technical indicators
    """
    # Plot SMA and Close Price
    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
    plt.plot(df['Date'], df['SMA_20'], label='20-Day SMA', color='orange')
    plt.title("Close Price and 20-Day SMA")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

    # Plot RSI
    plt.figure(figsize=(14, 5))
    plt.plot(df['Date'], df['RSI'], label='RSI', color='purple')
    plt.axhline(70, linestyle='--', color='red', label='Overbought')
    plt.axhline(30, linestyle='--', color='green', label='Oversold')
    plt.title("RSI (Relative Strength Index)")
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.legend()
    plt.show()

    # Plot MACD
    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], df['MACD'], label='MACD', color='blue')
    plt.plot(df['Date'], df['MACD_signal'], label='MACD Signal', color='red')
    plt.title("MACD and Signal Line")
    plt.xlabel("Date")
    plt.ylabel("MACD")
    plt.legend()
    plt.show()
