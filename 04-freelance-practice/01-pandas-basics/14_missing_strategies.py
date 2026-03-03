"""
Exercise 14: Missing Data Strategies (Advanced)
Dropping NaNs is easy. Filling them intelligently is pro.
"Forward Fill" (ffill) is crucial for time-series (e.g. stock prices).

Goal:
1. Fill 'Region' using Forward Fill (propagates last valid observation).
2. Fill 'Sales' with the Median (robust to outliers).

Execution mode: python 14_missing_strategies.py
"""

import pandas as pd
import numpy as np
import os

def setup_data():
    data = {
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
        'Region': ['North', np.nan, np.nan, 'South'], # User only entered Region once
        'Sales': [100, np.nan, 300, 10000] # 10000 is outlier, so Mean would be skewed
    }
    df = pd.DataFrame(data)
    df.to_csv('missing_adv.csv', index=False)
    print("✅ Test data missing_adv.csv generated")

def cleanup_data():
    if os.path.exists('missing_adv.csv'):
        os.remove('missing_adv.csv')
        print("🧹 Cleaning up test data")

def process_data():
    df = pd.read_csv('missing_adv.csv')
    print("--- Raw Data ---")
    print(df)

    # TODO: 1. Forward Fill Region
    # Useful when data is sorted by time and values "carry over"
    df['Region'] = df['Region'].ffill()

    # TODO: 2. Fill Sales with Median
    median_val = df['Sales'].median()
    df['Sales'] = df['Sales'].fillna(median_val)

    print("\n--- Cleaned Data ---")
    print(df)

    # --- Verification ---
    # Region for row 2 should be 'North'. Sales should be 300 (Median of 100, 300, 10000 is 300).
    if df.iloc[1]['Region'] == 'North' and df.iloc[1]['Sales'] == 300:
        print("\n🎉 Congratulations! Exercise 14 completed!")
    else:
        print("\n❌ Incorrect result.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
