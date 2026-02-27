"""
Exercise 8: Basic String Operations
Before Regex, you need to master simple string methods.

Goal:
1. Strip whitespace from 'Name' column.
2. Convert 'City' to Title Case (e.g., "new york" -> "New York").
3. Replace "St." with "Street" in 'Address'.

Execution mode: python 08_string_ops.py
"""

import pandas as pd
import os

def setup_data():
    data = {
        'Name': ['  John  ', 'Alice ', 'Bob', '  Eve'],
        'City': ['new york', 'LOS ANGELES', 'chicago', 'houston'],
        'Address': ['123 Main St.', '456 Oak St.', '789 Pine Rd.', '101 Maple St.']
    }
    df = pd.DataFrame(data)
    df.to_csv('strings.csv', index=False)
    print("✅ Test data strings.csv generated")

def cleanup_data():
    if os.path.exists('strings.csv'):
        os.remove('strings.csv')
        print("🧹 Cleaning up test data")

def process_data():
    df = pd.read_csv('strings.csv')
    print("--- Raw Data ---")
    print(df)

    # TODO: 1. Strip whitespace
    df['Name'] = df['Name'].str.strip()

    # TODO: 2. Title Case
    df['City'] = df['City'].str.title()

    # TODO: 3. Replace substring
    df['Address'] = df['Address'].str.replace('St.', 'Street', regex=False)

    print("\n--- Cleaned Data ---")
    print(df)

    # --- Verification ---
    if df.iloc[0]['Name'] == 'John' and df.iloc[0]['City'] == 'New York' and 'Street' in df.iloc[0]['Address']:
        print("\n🎉 Congratulations! Exercise 8 completed!")
    else:
        print("\n❌ Incorrect result.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
