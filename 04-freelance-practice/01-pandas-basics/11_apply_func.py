"""
Exercise 11: Apply Functions (Custom Logic)
When built-in functions aren't enough, apply your own python function to every row.

Goal:
1. Create a function `classify_score(score)` that returns 'Pass' or 'Fail'.
2. Apply this function to the 'Score' column to create a new 'Status' column.

Execution mode: python 11_apply_func.py
"""

import pandas as pd
import os

def setup_data():
    data = {
        'Student': ['Alice', 'Bob', 'Charlie', 'David'],
        'Score': [85, 40, 59, 90]
    }
    df = pd.DataFrame(data)
    df.to_csv('apply.csv', index=False)
    print("✅ Test data apply.csv generated")

def cleanup_data():
    if os.path.exists('apply.csv'):
        os.remove('apply.csv')
        print("🧹 Cleaning up test data")

def classify_score(score):
    if score >= 60:
        return 'Pass'
    else:
        return 'Fail'

def process_data():
    df = pd.read_csv('apply.csv')
    print("--- Raw Data ---")
    print(df)

    # TODO: 1. Apply function
    df['Status'] = df['Score'].apply(classify_score)

    print("\n--- Classified Data ---")
    print(df)

    # --- Verification ---
    if df.iloc[1]['Status'] == 'Fail' and df.iloc[0]['Status'] == 'Pass':
        print("\n🎉 Congratulations! Exercise 11 completed!")
    else:
        print("\n❌ Incorrect result.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
