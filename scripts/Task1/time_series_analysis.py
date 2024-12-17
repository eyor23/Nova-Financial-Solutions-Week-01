import matplotlib.pyplot as plt
import pandas as pd

def publication_frequency(data):
    """
    Plot publication frequency over time, aggregated by year
    """
    # Convert 'date' column to datetime with format inference
    data['date'] = pd.to_datetime(data['date'], infer_datetime_format=True, errors='coerce')

    # Drop rows where the date conversion failed
    data = data.dropna(subset=['date'])

    # Aggregate by year
    freq = data['date'].dt.year.value_counts().sort_index()

    # Plot the data as a histogram
    plt.figure(figsize=(24, 12))
    freq.plot(kind='bar', title='Publication Frequency Over Time (Aggregated by Year)', color='skyblue')
    plt.xlabel('Year')
    plt.ylabel('Number of Publications')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.show()