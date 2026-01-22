"""
Exercise 4: Data Transformation - Modifying Column Data

Goal:
1. Convert all names in 'Name' column to uppercase
2. Create a new column 'Price_CNY' which is 7 times 'Price' (USD)
3. Print first 5 rows to check results

Execution mode: python 04_transform_columns.py
"""

import pandas as pd
import os

# --- Automatically generate test data ---
def setup_data():
    data = {
        'Name': ['apple', 'banana', 'orange', 'grape'],
        'Price': [1.5, 0.8, 1.2, 2.5]
    }
    df = pd.DataFrame(data)
    df.to_csv('fruits.csv', index=False)
    print("✅ Test data fruits.csv generated")

def cleanup_data():
    if os.path.exists('fruits.csv'):
        os.remove('fruits.csv')

# --- Your code ---
def process_data():
    df = pd.read_csv('fruits.csv')
    print("--- Original Data ---")
    print(df)
    
    # TODO: 1. Convert 'Name' column to uppercase
    # Hint: df['Name'] = df['Name'].str.upper()
    df['Name'] = df['Name'].str.upper()
    
    # TODO: 2. Create new column 'Price_CNY' = Price * 7
    df['Price_CNY'] = df['Price'] * 7
    
    print("\n--- Transformed Data ---")
    print(df)
    
    # --- Verification ---
    if df['Name'][0] == 'APPLE' and df['Price_CNY'][0] == 10.5:
        print("\n🎉 Congratulations! Data transformation successful!")
    else:
        print("\n❌ Error: Incorrect data transformation")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
