"""
Exercise 12: Saving Data (The Deliverable)
You cleaned the data, now you need to send it to the client.

Goal:
1. Save the dataframe to a clean CSV file.
2. Save the dataframe to an Excel file (requires openpyxl).
3. Save without the index numbers.

Execution mode: python 12_save_data.py
"""

import pandas as pd
import os

def setup_data():
    data = {'ID': [1, 2], 'Value': ['A', 'B']}
    df = pd.DataFrame(data)
    df.to_csv('input.csv', index=False)
    print("✅ Test data input.csv generated")

def cleanup_data():
    files = ['input.csv', 'output_clean.csv', 'output_clean.xlsx']
    for f in files:
        if os.path.exists(f):
            os.remove(f)
            print(f"🧹 Cleaned up {f}")

def process_data():
    df = pd.read_csv('input.csv')
    
    # TODO: 1. Save to CSV without index
    df.to_csv('output_clean.csv', index=False)
    
    # TODO: 2. Save to Excel
    try:
        df.to_excel('output_clean.xlsx', index=False)
        print("✅ Excel saved")
    except ImportError:
        print("⚠️ Skipped Excel (openpyxl not installed)")

    # --- Verification ---
    if os.path.exists('output_clean.csv'):
        print("\n🎉 Congratulations! Exercise 12 completed!")
    else:
        print("\n❌ File not found.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
