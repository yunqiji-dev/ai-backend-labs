"""
Exercise 13: Handling Duplicates (Advanced)
Simple `drop_duplicates` is often not enough.
What if you need to keep the *newest* record? Or find *which* records are dupes?

Goal:
1. Identify duplicates using `df.duplicated(keep=False)`.
2. Sort by Date and keep the *last* occurrence (newest).
3. Drop duplicates based on a subset of columns (Email only).

Execution mode: python 13_advanced_duplicates.py
"""

import pandas as pd
import os

def setup_data():
    data = {
        'ID': [1, 2, 3, 4],
        'Email': ['a@test.com', 'b@test.com', 'a@test.com', 'c@test.com'],
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'], # ID 3 is newer update of ID 1
        'Value': [100, 200, 150, 300]
    }
    df = pd.DataFrame(data)
    df.to_csv('dupes_adv.csv', index=False)
    print("✅ Test data dupes_adv.csv generated")

def cleanup_data():
    if os.path.exists('dupes_adv.csv'):
        os.remove('dupes_adv.csv')
        print("🧹 Cleaning up test data")

def process_data():
    df = pd.read_csv('dupes_adv.csv')
    print("--- Raw Data ---")
    print(df)

    # TODO: 1. See all duplicates
    dupes = df[df.duplicated(subset=['Email'], keep=False)]
    print("\n--- All Duplicates ---")
    print(dupes)

    # TODO: 2. Sort by Date (ensure newest is last)
    df = df.sort_values('Date')

    # TODO: 3. Keep Last (Newest)
    df_clean = df.drop_duplicates(subset=['Email'], keep='last')

    print("\n--- Cleaned (Kept Newest) ---")
    print(df_clean)

    # --- Verification ---
    # Should keep ID 3 (Date 01-03) and drop ID 1 (Date 01-01)
    if 3 in df_clean['ID'].values and 1 not in df_clean['ID'].values:
        print("\n🎉 Congratulations! Exercise 13 completed!")
    else:
        print("\n❌ Incorrect result.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
