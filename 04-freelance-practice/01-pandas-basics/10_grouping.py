"""
Exercise 10: Grouping and Aggregation (Simple)
Before Pivot Tables, learn GroupBy. This is SQL's "GROUP BY".

Goal:
1. Calculate Total Sales per Region.
2. Calculate Average Age per Department.

Execution mode: python 10_grouping.py
"""

import pandas as pd
import os

def setup_data():
    data = {
        'Dept': ['HR', 'IT', 'HR', 'IT', 'Sales', 'Sales'],
        'Age': [30, 25, 45, 35, 22, 50],
        'Salary': [5000, 6000, 7000, 8000, 4000, 9000]
    }
    df = pd.DataFrame(data)
    df.to_csv('grouping.csv', index=False)
    print("✅ Test data grouping.csv generated")

def cleanup_data():
    if os.path.exists('grouping.csv'):
        os.remove('grouping.csv')
        print("🧹 Cleaning up test data")

def process_data():
    df = pd.read_csv('grouping.csv')
    print("--- Raw Data ---")
    print(df)

    # TODO: 1. Total Salary per Dept
    salary_sum = df.groupby('Dept')['Salary'].sum()
    print("\n--- Total Salary ---")
    print(salary_sum)

    # TODO: 2. Average Age per Dept
    age_mean = df.groupby('Dept')['Age'].mean()
    print("\n--- Avg Age ---")
    print(age_mean)

    # --- Verification ---
    if salary_sum['IT'] == 14000:
        print("\n🎉 Congratulations! Exercise 10 completed!")
    else:
        print("\n❌ Incorrect result.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
