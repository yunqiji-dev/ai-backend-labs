"""
Exercise 18: Pivot Tables - Summarizing Data
Clients often want "Summary Reports" (e.g., Total Sales per Region).

Goal:
1. Create a Pivot Table showing Total Sales per Region.
2. Create a Pivot Table showing Average Sales per Product.

Execution mode: python 18_pivot_tables.py
"""

import pandas as pd
import os

def setup_data():
    data = {
        'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-01'],
        'Region': ['North', 'South', 'North', 'South', 'North'],
        'Product': ['A', 'A', 'B', 'B', 'A'],
        'Sales': [100, 200, 150, 250, 120]
    }
    df = pd.DataFrame(data)
    df.to_csv('sales.csv', index=False)
    print("✅ Test data sales.csv generated")

def cleanup_data():
    if os.path.exists('sales.csv'):
        os.remove('sales.csv')
        print("🧹 Cleaning up test data")

def process_data():
    df = pd.read_csv('sales.csv')
    
    # TODO: 1. Pivot: Total Sales by Region
    pivot_region = df.pivot_table(index='Region', values='Sales', aggfunc='sum')
    print("\n--- Total Sales by Region ---")
    print(pivot_region)

    # TODO: 2. Pivot: Average Sales by Product
    pivot_product = df.pivot_table(index='Product', values='Sales', aggfunc='mean')
    print("\n--- Avg Sales by Product ---")
    print(pivot_product)

    # --- Verification ---
    north_sales = pivot_region.loc['North', 'Sales']
    if north_sales == 370:
        print("\n🎉 Congratulations! Exercise 18 completed!")
    else:
        print("\n❌ Incorrect result.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
