"""
Exercise 9: Sorting and Ranking
Clients often ask: "Who are my top 10 customers?"

Goal:
1. Sort data by 'Sales' (Descending).
2. Sort data by 'Region' (Ascending) then 'Sales' (Descending).
3. Reset the index after sorting.

Execution mode: python 09_sorting.py
"""

import pandas as pd
import os

def setup_data():
    data = {
        'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Region': ['North', 'North', 'South', 'South', 'North'],
        'Sales': [200, 150, 300, 400, 250]
    }
    df = pd.DataFrame(data)
    df.to_csv('ranking.csv', index=False)
    print("✅ Test data ranking.csv generated")

def cleanup_data():
    if os.path.exists('ranking.csv'):
        os.remove('ranking.csv')
        print("🧹 Cleaning up test data")

def process_data():
    df = pd.read_csv('ranking.csv')
    print("--- Raw Data ---")
    print(df)

    # TODO: 1. Sort by Sales Descending
    df_sorted_sales = df.sort_values(by='Sales', ascending=False)
    print("\n--- Top Sales ---")
    print(df_sorted_sales)

    # TODO: 2. Sort by Region then Sales
    df_multi_sort = df.sort_values(by=['Region', 'Sales'], ascending=[True, False])
    
    # TODO: 3. Reset Index (drop=True prevents old index from becoming a column)
    df_multi_sort = df_multi_sort.reset_index(drop=True)

    print("\n--- Region Leaders ---")
    print(df_multi_sort)

    # --- Verification ---
    if df_multi_sort.iloc[0]['Salesperson'] == 'Eva':
        print("\n🎉 Congratulations! Exercise 9 completed!")
    else:
        print("\n❌ Incorrect result. Eva should be first in North region.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
