"""
Exercise 24: Memory Optimization - Handling Big Data
Handling large CSVs on small RAM.

Goal:
1. Inspect memory usage.
2. Optimize types (int64 -> int16, object -> category).

Execution mode: python 24_memory_optimization.py
"""

import pandas as pd
import numpy as np
import os

def setup_data():
    df = pd.DataFrame({
        'ID': np.arange(5000),
        'Status': np.random.choice(['Active', 'Inactive'], 5000),
        'Score': np.random.randint(0, 100, 5000)
    })
    df.to_csv('big_file.csv', index=False)
    print("✅ Test data big_file.csv generated")

def cleanup_data():
    if os.path.exists('big_file.csv'):
        os.remove('big_file.csv')
        print("🧹 Cleaning up test data")

def process_data():
    df = pd.read_csv('big_file.csv')
    mem_before = df.memory_usage(deep=True).sum()
    
    # TODO: Optimize
    df['Status'] = df['Status'].astype('category')
    df['Score'] = df['Score'].astype('int16')

    mem_after = df.memory_usage(deep=True).sum()
    print(f"Reduction: {100 * (1 - mem_after/mem_before):.1f}%")

    if mem_after < mem_before:
        print("\n🎉 Congratulations! Exercise 24 completed!")
    else:
        print("\n❌ Incorrect result.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
