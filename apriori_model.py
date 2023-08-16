import pandas as pd
from apyori import apriori

def load_data():
    dataset = pd.read_csv('data/dataset.csv', header=None)
    transactions = []
    for i in range(len(dataset)):
        transactions.append([str(item) for item in dataset.loc[i] if not pd.isna(item)])
    return transactions

def get_recommendations(transactions, input_product):
    rules = apriori(transactions, min_support=0.003, min_confidence=0.2, min_lift=3, min_length=2, max_length=2)
    
    recommendations = []
    for rule in rules:
        items = rule.items
        if input_product in items:
            other_item = next(item for item in items if item != input_product)
            confidence = rule.ordered_statistics[0].confidence
            recommendations.append((other_item, confidence))
    
    return recommendations
