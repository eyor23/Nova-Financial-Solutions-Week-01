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
