"""
Exercise 17: Merging Datasets - The VLOOKUP of Python
Real world data is often split across multiple files (e.g. Users and Orders).

Goal:
1. Merge 'users.csv' and 'orders.csv' on 'UserID'.
2. Perform a 'Left Join' (keep all orders, attach user info).
3. Fill missing user names with 'Unknown'.

Execution mode: python 17_merge_datasets.py
"""

import pandas as pd
import os

def setup_data():
    users = {
        'UserID': [1, 2, 3],
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Email': ['alice@test.com', 'bob@test.com', 'charlie@test.com']
    }
    orders = {
        'OrderID': [101, 102, 103, 104],
        'UserID': [1, 2, 1, 99], # User 99 does not exist in users table
        'Amount': [250, 150, 300, 50]
    }
    pd.DataFrame(users).to_csv('users.csv', index=False)
    pd.DataFrame(orders).to_csv('orders.csv', index=False)
    print("✅ Test data users.csv and orders.csv generated")

def cleanup_data():
    for f in ['users.csv', 'orders.csv']:
        if os.path.exists(f):
            os.remove(f)
    print("🧹 Cleaning up test data")

def process_data():
    users = pd.read_csv('users.csv')
    orders = pd.read_csv('orders.csv')
    
    # TODO: 1. Merge Orders with Users (Left Join)
    merged_df = pd.merge(orders, users, on='UserID', how='left')

    # TODO: 2. Fill missing names
    merged_df['Name'] = merged_df['Name'].fillna('Unknown')

    print("\n--- Merged Data ---")
    print(merged_df)

    # --- Verification ---
    if len(merged_df) == 4 and merged_df.iloc[3]['Name'] == 'Unknown':
        print("\n🎉 Congratulations! Exercise 17 completed!")
    else:
        print("\n❌ Incorrect result.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
