# text_analysis.py
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer

def sentiment_analysis(data, column):
    """
    Perform sentiment analysis on the specified column.
    """
    data['sentiment'] = data[column].apply(lambda x: TextBlob(x).sentiment.polarity)
    print("Sentiment analysis completed.")
    print(data[['headline', 'sentiment']].head())

def keyword_extraction(data, column, n=10):
    """
    Extract common keywords using CountVectorizer.
    """
    vectorizer = CountVectorizer(max_features=n, stop_words='english')
    keywords = vectorizer.fit_transform(data[column])
    print("Top keywords:\n", vectorizer.get_feature_names_out())


def pfm_sentiment_analysis(df, column_name):
    """
    Perform sentiment analysis on a specific column in a DataFrame.
    :param df: pandas DataFrame containing textual data
    :param column_name: Name of the column with text for analysis
    :return: DataFrame with added 'sentiment_score' and 'sentiment_category' columns
    """
    sentiment_scores = []
    sentiment_categories = []

    for text in df[column_name]:
        score = TextBlob(text).sentiment.polarity
        sentiment_scores.append(score)
        if score > 0:
            sentiment_categories.append('positive')
        elif score < 0:
            sentiment_categories.append('negative')
        else:
            sentiment_categories.append('neutral')

    df['sentiment_score'] = sentiment_scores
    df['sentiment_category'] = sentiment_categories
    return df