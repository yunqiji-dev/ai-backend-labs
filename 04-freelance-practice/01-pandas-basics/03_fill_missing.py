"""
Exercise 3: Data Cleaning - Handling Missing Values

Goal:
1. Identify missing values (NaN) in the data
2. Fill missing values in 'Name' column with "Unknown"
3. Fill missing values in 'Score' column with 0

Execution mode: python 03_fill_missing.py
"""

import pandas as pd
import numpy as np
import os

# --- Automatically generate test data (Do not modify) ---
def setup_data():
    data = {
        'Name': ['Alice', np.nan, 'Charlie', 'David', np.nan],
        'Score': [90, 85, np.nan, 95, 60],
        'City': ['NY', 'LA', 'SF', np.nan, 'DC']
    }
    df = pd.DataFrame(data)
    df.to_csv('missing.csv', index=False)
    print("✅ Test data missing.csv generated (contains missing values)")

def cleanup_data():
    if os.path.exists('missing.csv'):
        os.remove('missing.csv')
        print("🧹 Cleaning up test data")

# --- Your code here ---
def process_data():
    df = pd.read_csv('missing.csv')
    print("--- Original Data ---")
    print(df)
    
    # TODO: 1. Fill missing values in 'Name' column with "Unknown"
    # Hint: df['Name'] = df['Name'].fillna(...)
    df['Name'] = df['Name'].fillna('Unknown')
    
    
    # TODO: 2. Fill missing values in 'Score' column with 0
    df['Score'] =df['Score'].fillna(0)
    
    print("\n--- Processed Data ---")
    print(df)
    
    # --- Verification ---
    if df['Name'].isnull().sum() == 0 and df['Score'].isnull().sum() == 0:
        if 'Unknown' in df['Name'].values and 0 in df['Score'].values:
            print("\n🎉 Congratulations! All missing values handled correctly!")
            print("Exercise 3 completed!")
        else:
            print("\n❌ Error: Incorrect fill values, please check")
    else:
        print("\n❌ Error: Missing values still exist")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
