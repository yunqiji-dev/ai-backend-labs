"""
Exercise 15: Regex Cleaning - Extracting Information
Data Cleaning often involves extracting structured data from unstructured text.

Goal:
1. Extract valid email addresses from the 'Contact' column.
2. Extract phone numbers.
3. Remove rows where Email is missing.

Execution mode: python 15_regex_cleaning.py
"""

import pandas as pd
import os
import re

def setup_data():
    data = {
        'ID': [1, 2, 3, 4, 5],
        'Contact': [
            'Email: john@example.com, Phone: 123-456-7890',
            'Contact: jane.doe@test.co (555) 123-4567',
            'No email here, just phone 9876543210',
            'bob.smith@company.org is my email',
            'spam@spam.com 111-222-3333'
        ]
    }
    df = pd.DataFrame(data)
    df.to_csv('contacts.csv', index=False)
    print("✅ Test data contacts.csv generated")

def cleanup_data():
    if os.path.exists('contacts.csv'):
        os.remove('contacts.csv')
        print("🧹 Cleaning up test data")

def process_data():
    df = pd.read_csv('contacts.csv')
    print("--- Raw Data ---")
    print(df)

    # TODO: 1. Extract Email using Regex
    df['Email'] = df['Contact'].str.extract(r'([\w\.-]+@[\w\.-]+\.\w+)')

    # TODO: 2. Extract Phone Numbers
    df['Phone'] = df['Contact'].str.extract(r'(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})')

    # TODO: 3. Drop rows where Email is NaN
    df_clean = df.dropna(subset=['Email']).copy()

    print("\n--- Cleaned Data ---")
    print(df_clean[['ID', 'Email', 'Phone']])

    # --- Verification ---
    if len(df_clean) == 4 and df_clean.iloc[0]['Email'] == 'john@example.com':
        print("\n🎉 Congratulations! Exercise 15 completed!")
    else:
        print("\n❌ Incorrect result.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
