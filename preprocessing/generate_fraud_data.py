import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate 150 fraudulent transactions
n_transactions = 150

# Generate random dates within the last 30 days
end_date = datetime.now()
start_date = end_date - timedelta(days=30)
transaction_dates = [start_date + timedelta(
    days=np.random.randint(0, 30),
    hours=np.random.randint(0, 24),
    minutes=np.random.randint(0, 60)
) for _ in range(n_transactions)]

# Common fraud categories and their descriptions
fraud_categories = {
    'Electronics': ['Apple Store', 'Best Buy', 'Amazon Electronics', 'NewEgg.com'],
    'Gas/Automotive': ['Shell', 'Exxon', 'BP', 'Chevron'],
    'Internet': ['Steam Games', 'PlayStation Network', 'Xbox Live', 'Nintendo eShop'],
    'Travel': ['Expedia.com', 'Hotels.com', 'Airbnb', 'United Airlines'],
    'ATM': ['ATM Withdrawal', 'Cash Advance'],
    'Retail': ['Walmart', 'Target', 'Amazon.com', 'eBay'],
}

# ['Merchandise' 'Dining' 'Other Travel' 'Payment/Credit' 'Utilities'
#  'Lodging' 'Other' 'Airfare' 'Gas/Automotive' 'Phone/Cable'
#  'Other Services' 'Health Care' 'Entertainment' 'Internet']

# Generate random card numbers (last 4 digits only for privacy)
card_numbers = ['8373']

# Create fraudulent transactions
data = {
    'Transaction Date': transaction_dates,
    'Posted Date': [d + timedelta(days=np.random.randint(1, 4)) for d in transaction_dates],
    'Card No.': card_numbers,
    'Description': [],
    'Category': [],
    'Debit': [],
    'Credit': []
}

for _ in range(n_transactions):
    # Select random category and description
    category = np.random.choice(list(fraud_categories.keys()))
    description = np.random.choice(fraud_categories[category])
    
    # Generate transaction amount based on category
    if category == 'Electronics':
        amount = np.random.uniform(300, 2000)
    elif category == 'Gas Station':
        amount = np.random.uniform(40, 150)
    elif category == 'Online Services':
        amount = np.random.uniform(10, 200)
    elif category == 'Travel':
        amount = np.random.uniform(200, 1500)
    elif category == 'ATM':
        amount = np.random.choice([100, 200, 300, 500, 1000])
    else:
        amount = np.random.uniform(50, 500)
    
    data['Description'].append(description)
    data['Category'].append(category)
    data['Debit'].append(round(amount, 2))
    data['Credit'].append(0.00)

# Create DataFrame
df = pd.DataFrame(data)

# Sort by Transaction Date
df = df.sort_values('Transaction Date')

# Format dates as strings
df['Transaction Date'] = df['Transaction Date'].dt.strftime('%Y-%m-%d %H:%M:%S')
df['Posted Date'] = df['Posted Date'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Save to CSV
df.to_csv('fraudulent_transactions.csv', index=False)
