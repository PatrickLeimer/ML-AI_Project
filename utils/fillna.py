import pandas as pd
import os

def process_transactions(input_csv, is_fraud):
    """
    Reads a CSV of transactions, fills in missing Debit/Credit with 0,
    and labels them with isFraud = is_fraud.
    Returns the processed DataFrame (not written directly to disk).
    """
    df = pd.read_csv(input_csv)

    # Replace missing values in Debit or Credit with 0
    if 'Debit' in df.columns:
        df['Debit'] = df['Debit'].fillna(0)
    if 'Credit' in df.columns:
        df['Credit'] = df['Credit'].fillna(0)

    # Add/overwrite 'isFraud' column
    df['isFraud'] = 1 if is_fraud else 0

    return df


# Adjust these paths to match your folder structure
base_dir = os.path.dirname(os.path.abspath(__file__))

# CSV file containing known fraudulent transactions
fraud_file = os.path.join(base_dir, "../../data/raw/fraudulent_transactions.csv")
# CSV file containing latest bank statements (assumed non-fraudulent)
latest_file = os.path.join(base_dir, "../../data/raw/CP1Latest.csv")

# Output combined CSV
output_file = os.path.join(base_dir, "../../data/processed/combined_transactions.csv")

# Process the fraudulent CSV (label = 1)
df_fraud = process_transactions(fraud_file, is_fraud=True)

# Process the latest CSV (label = 0)
df_latest = process_transactions(latest_file, is_fraud=False)

# Combine the two DataFrames
df_combined = pd.concat([df_fraud, df_latest], ignore_index=True)

# Write out the combined CSV
df_combined.to_csv(output_file, index=False)
print(f"Combined CSV saved as {output_file}")
