# time_series.py
import matplotlib.pyplot as plt

def publication_frequency(data):
    """
    Plot publication frequency over time
    """
    freq = data['date'].value_counts().sort_index()

    # Plot the data
    plt.figure(figsize=(24, 12))
    freq.plot(kind='line', title='Publication Frequency Over Time')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(100))

    plt.show()

