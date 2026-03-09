"""
Exercise 26: The Final Capstone - Expert Data Pipeline
This challenge simulates a full-scale Experian data engineering task.

Scenario:
You have a 3-part dataset:
1. `users.json`: Nested user profiles (needs flattening).
2. `transactions.csv`: Large transaction log with duplicates and messy dates.
3. `blacklist.txt`: A list of banned user IDs (needs filtering).

Goal:
1. Load and flatten `users.json`.
2. Load `transactions.csv`, optimize memory, parse dates.
3. Merge Users and Transactions.
4. Filter out Blacklisted users.
5. Create a Pivot Table: Total Spend per City.
6. Export to `final_report.xlsx`.

Execution mode: python 26_capstone_final.py
"""

import pandas as pd
import numpy as np
import json
import os

def setup_data():
    # 1. Users (JSON)
    users = [
        {"id": 101, "profile": {"name": "Alice", "city": "New York"}},
        {"id": 102, "profile": {"name": "Bob", "city": "London"}},
        {"id": 103, "profile": {"name": "Charlie", "city": "Paris"}},
        {"id": 104, "profile": {"name": "David", "city": "New York"}} # Blacklisted
    ]
    with open('users.json', 'w') as f:
        json.dump(users, f)

    # 2. Transactions (CSV)
    trans = {
        'TransID': range(1, 7),
        'UserID': [101, 102, 101, 104, 103, 102],
        'Date': ['2023-01-01', 'Jan 02 23', '2023-01-01', '2023-01-05', '2023/01/06', '2023-01-02'],
        'Amount': [50.5, 20.0, 50.5, 1000.0, 75.0, 20.0] # Note duplicates
    }
    pd.DataFrame(trans).to_csv('transactions.csv', index=False)

    # 3. Blacklist (TXT)
    with open('blacklist.txt', 'w') as f:
        f.write("104\n999")

    print("✅ Test data generated (users.json, transactions.csv, blacklist.txt)")

def cleanup_data():
    for f in ['users.json', 'transactions.csv', 'blacklist.txt', 'final_report.xlsx']:
        if os.path.exists(f):
            os.remove(f)
    print("🧹 Cleaning up test data")

def process_data():
    # 1. Load Users
    with open('users.json', 'r') as f:
        users_df = pd.json_normalize(json.load(f))
    users_df.columns = [c.replace('profile.', '') for c in users_df.columns] # Clean headers
    print("--- Users ---")
    print(users_df)

    # 2. Load Transactions
    trans_df = pd.read_csv('transactions.csv')
    
    # 2a. Fix Dates
    trans_df['Date'] = pd.to_datetime(trans_df['Date'], errors='coerce')
    
    # 2b. Remove Duplicates
    trans_df = trans_df.drop_duplicates()

    # 3. Merge
    merged_df = pd.merge(trans_df, users_df, left_on='UserID', right_on='id', how='left')
    
    # 4. Filter Blacklist
    with open('blacklist.txt', 'r') as f:
        blacklist = [int(line.strip()) for line in f if line.strip().isdigit()]
    
    clean_df = merged_df[~merged_df['UserID'].isin(blacklist)]

    print("\n--- Cleaned & Merged ---")
    print(clean_df)

    # 5. Pivot: Spend per City
    report = clean_df.pivot_table(index='city', values='Amount', aggfunc='sum')
    print("\n--- Final Report ---")
    print(report)

    # 6. Export
    try:
        report.to_excel('final_report.xlsx')
        print("✅ Saved to final_report.xlsx")
    except:
        print("⚠️ Excel export skipped")

    # --- Verification ---
    # Alice (NY): 50.5 (Dupe removed)
    # Bob (London): 20.0 (Dupe removed)
    # Charlie (Paris): 75.0
    # David (NY): Blacklisted (Removed)
    # Total NY: 50.5, London: 20.0, Paris: 75.0
    if report.loc['New York', 'Amount'] == 50.5:
        print("\n🎉 Congratulations! Final Capstone Completed!")
    else:
        print("\n❌ Incorrect result.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
