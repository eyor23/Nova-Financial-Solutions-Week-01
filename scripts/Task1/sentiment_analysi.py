import pandas as pd
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_analysis(data, column, sample_size=None):
    """
    Perform sentiment analysis on the specified column, optionally using a random sample of the dataset.
    :param data: pandas DataFrame containing textual data
    :param column: Name of the column with text for analysis
    :param sample_size: Number of random samples to process (default is None to process all)
    """
    if sample_size is not None:
        data = data.sample(n=sample_size, random_state=1)  # Random sampling

    data['sentiment'] = data[column].apply(lambda x: TextBlob(x).sentiment.polarity)
    print("Sentiment analysis completed.")
    print(data[['headline', 'sentiment']].head())


def keyword_extraction(data, column, n=10, sample_size=None):
    """
    Extract common keywords using CountVectorizer, optionally using a random sample.
    :param data: pandas DataFrame
    :param column: Name of the column with text for analysis
    :param n: Number of top keywords to extract
    :param sample_size: Number of random samples to process (default is None to process all)
    """
    if sample_size is not None:
        data = data.sample(n=sample_size, random_state=1)  # Random sampling

    vectorizer = CountVectorizer(max_features=n, stop_words='english')
    keywords = vectorizer.fit_transform(data[column])
    print("Top keywords:\n", vectorizer.get_feature_names_out())


def pfm_sentiment_analysis(df, column_name, sample_size=None):
    """
    Perform sentiment analysis on a specific column in a DataFrame, optionally using a random sample.
    :param df: pandas DataFrame containing textual data
    :param column_name: Name of the column with text for analysis
    :param sample_size: Number of random samples to process (default is None to process all)
    :return: DataFrame with added 'sentiment_score' and 'sentiment_category' columns
    """
    if sample_size is not None:
        df = df.sample(n=sample_size, random_state=1)  # Random sampling

    sentiment_scores = []
    sentiment_categories = []

    for text in df[column_name]:
        # Skip empty or null values
        if isinstance(text, str) and text.strip():
            score = TextBlob(text).sentiment.polarity
            sentiment_scores.append(score)

            # Categorize based on polarity
            if score > 0:
                sentiment_categories.append('positive')
            elif score < 0:
                sentiment_categories.append('negative')
            else:
                sentiment_categories.append('neutral')
        else:
            sentiment_scores.append(0.0)  # Default neutral for non-text
            sentiment_categories.append('neutral')

    df['sentiment_score'] = sentiment_scores
    df['sentiment_category'] = sentiment_categories
    return df


def vader_sentiment_analysis(df, column_name, sample_size=None):
    """
    Perform sentiment analysis using VADER, optionally using a random sample.
    :param df: pandas DataFrame containing textual data
    :param column_name: Name of the column with text for analysis
    :param sample_size: Number of random samples to process (default is None to process all)
    :return: DataFrame with added 'sentiment_score' and 'sentiment_category' columns
    """
    if sample_size is not None:
        df = df.sample(n=sample_size, random_state=1)  # Random sampling

    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = []
    sentiment_categories = []

    for text in df[column_name]:
        if isinstance(text, str) and text.strip():
            scores = analyzer.polarity_scores(text)
            sentiment_scores.append(scores['compound'])

            # Categorize based on compound score
            if scores['compound'] > 0.05:
                sentiment_categories.append('positive')
            elif scores['compound'] < -0.05:
                sentiment_categories.append('negative')
            else:
                sentiment_categories.append('neutral')
        else:
            sentiment_scores.append(0.0)
            sentiment_categories.append('neutral')

    df['sentiment_score'] = sentiment_scores
    df['sentiment_category'] = sentiment_categories
    return df