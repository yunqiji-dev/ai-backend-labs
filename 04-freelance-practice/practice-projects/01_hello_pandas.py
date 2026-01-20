"""
Exercise 1: Pandas Getting Started - Reading and Viewing Data

Goal:
1. Read the 'data.csv' file in the current directory
2. Print the first 5 rows of the data
3. Print the shape of the data (number of rows, columns)

Execution mode: python 01_hello_pandas.py
"""

import pandas as pd
import os

# --- Automatically generate test data (Do not modify) ---
def setup_data():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
        'Age': [25, 30, 35, 40, 22, 28],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami']
    }
    df = pd.DataFrame(data)
    df.to_csv('data.csv', index=False)
    print("✅ Test data data.csv generated")

def cleanup_data():
    if os.path.exists('data.csv'):
        os.remove('data.csv')
        print("🧹 Cleaning up test data")

# --- Your code here ---
def process_data():
    # TODO: 1. Read 'data.csv' into variable df
    df = pd.read_csv('data.csv') # Modified here: df = pd.read_csv('data.csv')
    
    if df is None:
        print("❌ Error: Please implement data reading code first")
        return

    print("\n--- First 5 rows ---")
    # TODO: 2. Print first 5 rows
    print(df.head())
    
    print("\n--- Data Shape ---")
    # TODO: 3. Print shape
    print(df.shape)
    
    # --- Verification ---
    if len(df) == 6 and df.shape[1] == 3:
        print("\n🎉 Congratulations! Exercise 1 completed!")
    else:
        print("\n❌ Incorrect result, please check your code")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
