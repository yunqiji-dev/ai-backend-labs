"""
Exercise 16: Date Parsing - Handling Mixed Formats
Clients often send dates in random formats (US vs UK, Text vs Number).

Goal:
1. Convert the 'Date' column to a standardized datetime object.
2. Handle errors (coerce invalid dates to NaT).
3. Format the date as 'YYYY-MM-DD'.

Execution mode: python 16_date_parsing.py
"""

import pandas as pd
import os

def setup_data():
    data = {
        'Event': ['Signup', 'Purchase', 'Login', 'Logout', 'Error'],
        'Date_Raw': [
            '2023-01-15',       # Standard
            '01/15/2023',       # US Format
            '15 Jan 2023',      # Text
            '2023.01.15',       # Dot separated
            'Not a Date'        # Garbage
        ]
    }
    df = pd.DataFrame(data)
    df.to_csv('dates.csv', index=False)
    print("✅ Test data dates.csv generated")

def cleanup_data():
    if os.path.exists('dates.csv'):
        os.remove('dates.csv')
        print("🧹 Cleaning up test data")

def process_data():
    df = pd.read_csv('dates.csv')
    print("--- Raw Data ---")
    print(df)

    # TODO: 1. Convert to datetime
    df['Date_Parsed'] = pd.to_datetime(df['Date_Raw'], errors='coerce')

    # TODO: 2. Remove rows with invalid dates (NaT)
    df_clean = df.dropna(subset=['Date_Parsed']).copy()

    # TODO: 3. Format as string 'YYYY-MM-DD'
    df_clean['Date_String'] = df_clean['Date_Parsed'].dt.strftime('%Y-%m-%d')

    print("\n--- Cleaned Data ---")
    print(df_clean)

    # --- Verification ---
    if len(df_clean) == 4 and df_clean['Date_String'].nunique() == 1:
        print("\n🎉 Congratulations! Exercise 16 completed!")
    else:
        print("\n❌ Incorrect result.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
