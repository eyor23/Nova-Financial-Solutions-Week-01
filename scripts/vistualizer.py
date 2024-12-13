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

def plot_time_series(data, date_column):
    """
    Plots a time series analysis of publication frequency over time.

    :param data: DataFrame containing the date data
    :param date_column: Name of the column with date values
    """
    plt.figure(figsize=(10, 6))
    data[date_column] = pd.to_datetime(data[date_column], errors='coerce')
    data.dropna(subset=[date_column], inplace=True)
    data.groupby(date_column).size().plot(kind='line')
    plt.title('Publication Frequency Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles')
    plt.show()

def plot_publisher_contribution(data, publisher_column, top_n=5):
    """
    Plots a bar chart for the top N publishers by article count.

    :param data: DataFrame containing the publisher data
    :param publisher_column: Name of the column with publisher names
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
    :param text_column: Name of the column with textual content
    """
    text = " ".join(data[text_column])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Frequent Keywords in Headlines')
    plt.show()
