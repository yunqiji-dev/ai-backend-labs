"""
Exercise 25: Categorical Encoding - Prep for ML
Preparing data for Machine Learning.

Goal:
1. Label Encoding (Low/High -> 0/1).
2. One-Hot Encoding (Countries -> Columns).

Execution mode: python 25_encoding.py
"""

import pandas as pd
import os

def setup_data():
    data = {
        'ID': [1, 2, 3],
        'Risk': ['Low', 'High', 'Medium'],
        'Country': ['USA', 'UK', 'USA']
    }
    df = pd.DataFrame(data)
    df.to_csv('ml_data.csv', index=False)
    print("✅ Test data ml_data.csv generated")

def cleanup_data():
    if os.path.exists('ml_data.csv'):
        os.remove('ml_data.csv')
        print("🧹 Cleaning up test data")

def process_data():
    df = pd.read_csv('ml_data.csv')
    
    # TODO: 1. Label Encoding
    mapping = {'Low': 0, 'Medium': 1, 'High': 2}
    df['Risk_Code'] = df['Risk'].map(mapping)

    # TODO: 2. One-Hot Encoding
    df_encoded = pd.get_dummies(df, columns=['Country'])

    print("\n--- Encoded Data ---")
    print(df_encoded)

    if 'Country_USA' in df_encoded.columns and df['Risk_Code'][1] == 2:
        print("\n🎉 Congratulations! Exercise 25 completed!")
    else:
        print("\n❌ Incorrect result.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
