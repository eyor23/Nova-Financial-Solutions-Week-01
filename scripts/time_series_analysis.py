import matplotlib.pyplot as plt
import pandas as pd

def publication_frequency(data):
    """
    Plot publication frequency over time, aggregated by month
    """
    # Convert 'date' column to datetime with format inference
    data['date'] = pd.to_datetime(data['date'], infer_datetime_format=True, errors='coerce')

    # Drop rows where the date conversion failed
    data = data.dropna(subset=['date'])

    # Aggregate by month
    freq = data['date'].dt.to_period('M').value_counts().sort_index()

    # Plot the data
    plt.figure(figsize=(24, 12))
    freq.plot(kind='line', title='Publication Frequency Over Time (Aggregated by Month)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(20))  # Adjust the number of ticks on the x-axis

    plt.show()

# Example usage with corrected date range

