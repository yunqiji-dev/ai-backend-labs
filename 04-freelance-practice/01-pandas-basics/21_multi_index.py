"""
Exercise 21: Multi-Index (The Expert's Headache)
Advanced grouping creates "Multi-Index" DataFrames. You must know how to flatten them.
Client: "Why does my Excel header look weird?" -> You: "Let me reset_index."

Goal:
1. Group by multiple columns (Region, Product).
2. Inspect the resulting Multi-Index.
3. Flatten it back to a normal table using `reset_index()`.

Execution mode: python 21_multi_index.py
"""

import pandas as pd
import os

def setup_data():
    data = {
        'Region': ['North', 'North', 'South', 'South'],
        'Product': ['A', 'B', 'A', 'B'],
        'Sales': [100, 200, 150, 250]
    }
    df = pd.DataFrame(data)
    df.to_csv('multi.csv', index=False)
    print("✅ Test data multi.csv generated")

def cleanup_data():
    if os.path.exists('multi.csv'):
        os.remove('multi.csv')
        print("🧹 Cleaning up test data")

def process_data():
    df = pd.read_csv('multi.csv')
    
    # TODO: 1. Group By Multiple Columns
    grouped = df.groupby(['Region', 'Product']).sum()
    
    print("--- Multi-Index DataFrame ---")
    print(grouped)
    print("Index Names:", grouped.index.names)

    # TODO: 2. Flatten (Reset Index)
    flat = grouped.reset_index()
    
    print("\n--- Flattened DataFrame ---")
    print(flat)

    # --- Verification ---
    if 'Region' in flat.columns and len(flat) == 4:
        print("\n🎉 Congratulations! Exercise 21 completed!")
    else:
        print("\n❌ Incorrect result.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
