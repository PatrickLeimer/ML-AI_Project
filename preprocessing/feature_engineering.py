import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "../raw/CP1Latest.csv")

df = pd.read_csv(csv_path)

df.drop(columns=['Transaction Date', 'Posted Date', 'Card No.', 'Description', 'Credit', 'Debit'], inplace=True)

print(df['Category'].unique())

# print(df['Description'].unique())