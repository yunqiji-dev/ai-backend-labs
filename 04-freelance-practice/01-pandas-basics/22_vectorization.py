"""
Exercise 22: Performance Tuning (Vectorization)
Don't iterate! Loops in Python are slow. Vectorized operations in Pandas are fast.
Experian Test: "Rewrite this for-loop using pandas vectorization."

Goal:
1. (Bad) Calculate Tax using a for-loop.
2. (Good) Calculate Tax using vectorization (`df['Price'] * 0.1`).
3. Compare results.

Execution mode: python 22_vectorization.py
"""

import pandas as pd
import numpy as np
import os
import time

def setup_data():
    # 100k rows to make speed difference visible
    df = pd.DataFrame({'Price': np.random.uniform(10, 100, 100000)})
    df.to_csv('perf.csv', index=False)
    print("✅ Test data perf.csv generated")

def cleanup_data():
    if os.path.exists('perf.csv'):
        os.remove('perf.csv')
        print("🧹 Cleaning up test data")

def process_data():
    df = pd.read_csv('perf.csv')
    
    # --- BAD WAY: Loop ---
    start = time.time()
    taxes = []
    for price in df['Price']:
        taxes.append(price * 0.1)
    df['Tax_Loop'] = taxes
    end = time.time()
    print(f"Loop Time: {end - start:.4f} seconds")

    # --- GOOD WAY: Vectorization ---
    start = time.time()
    df['Tax_Vec'] = df['Price'] * 0.1
    end = time.time()
    print(f"Vector Time: {end - start:.4f} seconds")

    # --- Verification ---
    if df['Tax_Loop'].equals(df['Tax_Vec']):
        print("\n🎉 Congratulations! Exercise 22 completed! (Results match)")
    else:
        print("\n❌ Results don't match.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
