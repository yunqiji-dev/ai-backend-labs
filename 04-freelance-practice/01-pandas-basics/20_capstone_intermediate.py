"""
Exercise 20: Capstone Project (Intermediate) - Real World Data Cleaning
This is the "Mid-Boss". It combines everything you've learned so far.

Scenario:
You received a messy 'leads_raw.csv' from a client.
It contains duplicates, missing emails, messy dates, and salary fields with '$' signs.

Goal:
1. Load data.
2. Remove duplicates.
3. Clean 'Salary' (remove '$', convert to float).
4. Parse 'JoinDate' to YYYY-MM-DD.
5. Extract valid emails.
6. Filter for High Value Leads (Salary > 100k).
7. Save to 'leads_clean.csv'.

Execution mode: python 20_capstone_intermediate.py
"""

import pandas as pd
import numpy as np
import os

def setup_data():
    data = {
        'ID': [1, 2, 2, 3, 4, 5], 
        'Name': ['Alice', 'Bob', 'Bob', 'Charlie', 'David', 'Eva'],
        'Email': ['alice@test.com', 'bob@test.com', 'bob@test.com', 'no-email', 'david.corp@web.net', 'eva@gmail'],
        'JoinDate': ['2023-01-01', '01/02/2023', '01/02/2023', 'Jan 03 23', '2023.01.04', 'Invalid'],
        'Salary': ['$120,000', '$90,000', '$90,000', '$150,000', '$80,000', '$200,000']
    }
    df = pd.DataFrame(data)
    df.to_csv('leads_raw.csv', index=False)
    print("✅ Test data leads_raw.csv generated")

def cleanup_data():
    for f in ['leads_raw.csv', 'leads_clean.csv']:
        if os.path.exists(f):
            os.remove(f)
    print("🧹 Cleaning up test data")

def process_data():
    df = pd.read_csv('leads_raw.csv')
    
    # 2. Remove Duplicates
    df = df.drop_duplicates()

    # 3. Clean Salary
    df['Salary'] = df['Salary'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)

    # 4. Parse Dates
    df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce')

    # 5. Extract/Validate Emails
    valid_email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    is_valid_email = df['Email'].str.match(valid_email_pattern, na=False)
    df = df[is_valid_email]

    # 6. Filter High Value
    df_high_value = df[df['Salary'] > 100000]

    # 7. Save
    df_high_value.to_csv('leads_clean.csv', index=False)

    print("\n--- Final Clean Data ---")
    print(df_high_value)

    # --- Verification ---
    if len(df_high_value) == 1 and df_high_value.iloc[0]['Name'] == 'Alice':
        print("\n🎉 Congratulations! Intermediate Capstone Completed!")
    else:
        print(f"\n❌ Result count: {len(df_high_value)}")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
