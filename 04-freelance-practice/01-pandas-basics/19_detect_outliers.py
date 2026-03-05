"""
Exercise 19: Outlier Detection - Finding Anomalies
Bad data often hides as "extreme values" (e.g., Age = 200).

Goal:
1. Calculate the Z-Score for the 'Amount' column.
2. Filter out rows where Z-Score > 2 (Keep only normal data).

Execution mode: python 19_detect_outliers.py
"""

import pandas as pd
import numpy as np
import os

def setup_data():
    data = {
        'TransactionID': [1, 2, 3, 4, 5, 6],
        'Amount': [100, 105, 95, 110, 100, 10000] # 10000 is outlier
    }
    df = pd.DataFrame(data)
    df.to_csv('transactions.csv', index=False)
    print("✅ Test data transactions.csv generated")

def cleanup_data():
    if os.path.exists('transactions.csv'):
        os.remove('transactions.csv')
        print("🧹 Cleaning up test data")

def process_data():
    df = pd.read_csv('transactions.csv')
    print("--- Raw Transactions ---")
    print(df)

    # TODO: 1. Calculate Mean and Std Dev
    mean = df['Amount'].mean()
    std = df['Amount'].std()

    # TODO: 2. Calculate Z-Score
    df['Z_Score'] = (df['Amount'] - mean) / std

    # TODO: 3. Filter Outliers (Keep |Z| <= 1.5 for this small dataset)
    df_clean = df[df['Z_Score'].abs() <= 1.5]

    print("\n--- Cleaned Data (No Outliers) ---")
    print(df_clean)

    # --- Verification ---
    if len(df_clean) == 5 and 10000 not in df_clean['Amount'].values:
        print("\n🎉 Congratulations! Exercise 19 completed!")
    else:
        print("\n❌ Incorrect result.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
