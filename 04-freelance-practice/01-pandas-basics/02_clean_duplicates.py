"""
Exercise 2: Data Cleaning - Removing Duplicate Rows

Goal:
1. Identify duplicate rows in the data
2. Remove duplicate rows, keeping only the first occurrence
3. Print the number of rows after deduplication

Execution mode: python 02_clean_duplicates.py
"""

import pandas as pd
import os

# --- Automatically generate test data (Do not modify) ---
def setup_data():
    data = {
        'ID': [1, 2, 2, 3, 4, 4, 5],
        'Product': ['Apple', 'Banana', 'Banana', 'Orange', 'Grape', 'Grape', 'Mango'],
        'Price': [1.2, 0.5, 0.5, 0.8, 2.0, 2.0, 1.5]
    }
    df = pd.DataFrame(data)
    df.to_csv('duplicates.csv', index=False)
    print("✅ Test data duplicates.csv generated (contains duplicates)")

def cleanup_data():
    if os.path.exists('duplicates.csv'):
        os.remove('duplicates.csv')
        print("🧹 Cleaning up test data")

# --- Your code here ---
def process_data():
    # Read data
    df = pd.read_csv('duplicates.csv')
    print(f"Original rows: {len(df)}")
    
    # TODO: Remove duplicate rows and save to df_clean variable
    # Hint: Use drop_duplicates()
    df_clean = df.drop_duplicates() # Modify here
    
    print(f"Rows after deduplication: {len(df_clean)}")
    
    # --- Verification ---
    expected_rows = 5
    if len(df_clean) == expected_rows:
        print(f"\n🎉 Congratulations! Successfully removed {len(df) - len(df_clean)} duplicate rows!")
        print("Exercise 2 completed!")
    else:
        print(f"\n❌ Error: Expected {expected_rows} rows, but got {len(df_clean)} rows")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
