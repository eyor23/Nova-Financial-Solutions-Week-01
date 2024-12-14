import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_sentiment_analysis(data, sentiment_column):
    """
    Plots a bar chart for sentiment analysis distribution.

    :param data: DataFrame containing the sentiment data
    :param sentiment_column: Name of the column with sentiment values
    """
    plt.figure(figsize=(8, 6))
    data[sentiment_column].value_counts().plot(kind='bar', color=['green', 'gray', 'red'])
    plt.title('Sentiment Analysis Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Frequency')
    plt.show()

def plot_time_series(data, date_col):
    """
    Plots a time series analysis of publication frequency over time.

    :param data: DataFrame containing the date data
    :param date_column: Date
    """
    plt.figure(figsize=(10, 6))
    data[date_col] = pd.to_datetime(data[date_col], errors='coerce')
    data.dropna(subset=[date_col], inplace=True)
    #data.groupby(date_column).size().plot(kind='line')
    data['month'] = data[date_col].dt.to_period('M')
    monthly_counts = data.groupby('month').size()
    monthly_counts.plot(kind='line')
    plt.title('Publication Frequency Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles')
    plt.grid()
    plt.show()

def plot_publisher_contribution(data, publisher_column, top_n=5):
    """
    Plots a bar chart for the top N publishers by article count.

    :param data: DataFrame containing the publisher data
    :param publisher_column: publisher
    :param top_n: Number of top publishers to display
    """
    plt.figure(figsize=(10, 6))
    top_publishers = data[publisher_column].value_counts().head(top_n)
    top_publishers.plot(kind='bar', color='skyblue')
    plt.title(f'Top {top_n} Publishers by Article Count')
    plt.xlabel('Publisher')
    plt.ylabel('Number of Articles')
    plt.show()

def plot_word_cloud(data, text_column):
    """
    Plots a word cloud for the most frequent keywords in a text column.

    :param data: DataFrame containing the text data
    :param text_column: Headline
    """
    text = " ".join(data[text_column])
    cleaned_text = re.sub(r'[A-Za-z0-9\s]', '', text).lower()
    word_counts = Counter(cleaned_text.split())
    top_5_words = dict(word_counts.most_common(5))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Top 5 Frequent Keywords in Headlines')
    plt.show()

def plot_stock_article_count(data, stock_column):
    """
    Plots the number of articles for each stock.

    :param data: DataFrame containing the stock data
    :param stock_column: Name of the column with stock names
    """
    plt.figure(figsize=(10, 6))
    stock_counts = data[stock_column].value_counts()
    stock_counts.plot(kind='bar', color='lightblue')
    plt.title('Number of Articles per Stock')
    plt.xlabel('Stock')
    plt.ylabel('Number of Articles')
    plt.show()

def plot_word_cloud_top_stocks(data, text_column, stock_column, top_n=5):
    """
    Plots word clouds for the top N stocks by article count.

    :param data: DataFrame containing the text and stock data
    :param text_column: Name of the column with text data
    :param stock_column: Name of the column with stock names
    :param top_n: Number of top stocks to visualize
    """
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
