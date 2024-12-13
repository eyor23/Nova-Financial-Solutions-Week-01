# time_series_analysis.py
import matplotlib.pyplot as plt

def publication_frequency(data):
    """
    Plot publication frequency over time.
    """
    freq = data['date'].value_counts().sort_index()
    freq.plot(kind='line', title='Publication Frequency Over Time')
    plt.show()
