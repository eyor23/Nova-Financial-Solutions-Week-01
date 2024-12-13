# publisher_analysis.py
import pandas as pd
def publisher_contributions(data):
    """
    Analyze the contributions of each publisher.
    """
    contributions = data['publisher'].value_counts()
    print("Publisher contributions:\n", contributions)

def domain_analysis(data):
    """
    Analyze unique email domains if applicable.
    """
    data['domain'] = data['publisher'].str.extract(r'@([\w\.]+)')
    domain_counts = data['domain'].value_counts()
    print("Unique domains:\n", domain_counts)
