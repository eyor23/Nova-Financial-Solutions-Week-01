import pandas as pd

def analyze_text_length(data, column):
    """
    Analyze text lengths of the specified column.
    """
    data['text_length'] = data[column].apply(len)
    print("Basic statistics for text lengths:\n", data['text_length'].describe())

def articles_per_publisher(data):
    """
    Count articles per publisher.
    """
    publisher_counts = data['publisher'].value_counts()
    print("Articles per publisher:\n", publisher_counts)

def analyze_publication_dates(data):
    """
    Analyze publication trends over time.
    """
    data['date'] = pd.to_datetime(data['date'])
    date_counts = data['date'].value_counts().sort_index()
    print("Publication trends:\n", date_counts)
