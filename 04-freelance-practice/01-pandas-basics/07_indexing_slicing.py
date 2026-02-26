"""
Exercise 7: Indexing & Slicing (The Scalpel)
Filtering (Ex 05) selects rows. But how do you select specific cells?
e.g. "Change the Price of Apple to 2.00".

Goal:
1. Use `.loc` to select rows by Label/Condition.
2. Use `.iloc` to select rows by Position (Index).
3. Modify a specific value using `.loc`.

Execution mode: python 07_indexing_slicing.py
"""

import pandas as pd
import os

def setup_data():
    data = {
        'Product': ['Apple', 'Banana', 'Orange', 'Grape'],
        'Price': [1.5, 0.8, 1.2, 2.5],
        'Stock': [100, 200, 150, 50]
    }
    df = pd.DataFrame(data)
    # Set Product as Index to make .loc more intuitive
    df.set_index('Product', inplace=True)
    df.to_csv('inventory.csv')
    print("✅ Test data inventory.csv generated")

def cleanup_data():
    if os.path.exists('inventory.csv'):
        os.remove('inventory.csv')
        print("🧹 Cleaning up test data")

def process_data():
    df = pd.read_csv('inventory.csv', index_col='Product')
    print("--- Raw Data ---")
    print(df)

    # TODO: 1. Select 'Apple' using .loc (Label)
    apple_row = df.loc['Apple']
    print("\n--- Apple Row (.loc) ---")
    print(apple_row)

    # TODO: 2. Select first row using .iloc (Position)
    first_row = df.iloc[0]
    print("\n--- First Row (.iloc) ---")
    print(first_row)

    # TODO: 3. Modify value: Set Banana Price to 0.99
    # Format: df.loc[Row, Column] = NewValue
    df.loc['Banana', 'Price'] = 0.99

    print("\n--- Modified Data ---")
    print(df)

    # --- Verification ---
    if df.loc['Banana', 'Price'] == 0.99:
        print("\n🎉 Congratulations! Exercise 7 completed!")
    else:
        print("\n❌ Incorrect result. Banana price should be 0.99.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
