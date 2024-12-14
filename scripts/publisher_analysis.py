import pandas as pd

def publisher_contributions(data):
    """
    Analyze the contributions of each publisher.
    """
    if 'publisher' in data.columns:
        contributions = data['publisher'].value_counts()
        print("Publisher contributions:\n", contributions)
    else:
        print("Error: 'publisher' column not found in the data.")

def domain_analysis(data):
    """
    Analyze unique email domains if applicable.
    """
    if 'publisher' in data.columns:
        data['domain'] = data['publisher'].str.extract(r'@([\w\.]+)')
        domain_counts = data['domain'].value_counts()
        print("Unique domains:\n", domain_counts)
    else:
        print("Error: 'publisher' column not found in the data.")

# Example usage
# Assuming data_cleaned is your DataFrame
data_cleaned = pd.DataFrame({
    'publisher': ['pub1@example.com', 'pub2@example.com', 'pub3@example.com', 'pub1@example.com']
})

# Check the structure of your data
print(data_cleaned.columns)
print(data_cleaned.head())

# Run the analysis functions
publisher_contributions(data_cleaned)
domain_analysis(data_cleaned)
