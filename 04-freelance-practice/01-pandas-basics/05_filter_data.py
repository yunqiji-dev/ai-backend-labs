"""
Exercise 5: Data Filtering - Selecting Data Based on Conditions

Goal:
1. Filter rows where 'Age' is greater than 30
2. Filter rows where 'City' is 'New York'
3. Print filtering results

Execution mode: python 05_filter_data.py
"""

import pandas as pd
import os

# --- Automatically generate test data ---
def setup_data():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 35, 30, 45, 28],
        'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Miami']
    }
    df = pd.DataFrame(data)
    df.to_csv('people.csv', index=False)
    print("✅ Test data people.csv generated")

def cleanup_data():
    if os.path.exists('people.csv'):
        os.remove('people.csv')

# --- Your code ---
def process_data():
    df = pd.read_csv('people.csv')
    
    print("--- Filter Age > 30 ---")
    # TODO: 1. Filter rows where Age > 30
    # older_people = df[df['Age'] > 30]
    older_people = df[df['Age'] > 30] # Modify here
    print(older_people)
    
    print("\n--- Filter City == 'New York' ---")
    # TODO: 2. Filter rows where City is 'New York'
    ny_people = df[df['City'] == 'New York'] # Modify here
    print(ny_people)
    
    # --- Verification ---
    if older_people is not None and len(older_people) == 2:
        if ny_people is not None and len(ny_people) == 2:
            print("\n🎉 Congratulations! Data filtering successful!")
        else:
            print("\n❌ Error: Incorrect filtering result for New York")
    else:
        print("\n❌ Error: Incorrect filtering result for Age")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
