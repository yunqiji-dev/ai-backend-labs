"""
Exercise 23: JSON Normalization - Handling Nested Data
Not all client data is flat. APIs often return nested JSON.

Goal:
1. Load a nested JSON dataset.
2. Flatten it into a proper table using `pd.json_normalize`.

Execution mode: python 23_json_normalize.py
"""

import pandas as pd
import json
import os

def setup_data():
    data = [
        {"id": 1, "info": {"email": "alice@test.com", "city": "New York"}},
        {"id": 2, "info": {"email": "bob@test.com", "city": "London"}}
    ]
    with open('nested.json', 'w') as f:
        json.dump(data, f)
    print("✅ Test data nested.json generated")

def cleanup_data():
    if os.path.exists('nested.json'):
        os.remove('nested.json')
        print("🧹 Cleaning up test data")

def process_data():
    with open('nested.json', 'r') as f:
        raw_data = json.load(f)
    
    # TODO: Flatten
    df_users = pd.json_normalize(raw_data)
    print("\n--- Flattened Users ---")
    print(df_users)

    if 'info.city' in df_users.columns:
        print("\n🎉 Congratulations! Exercise 23 completed!")
    else:
        print("\n❌ Incorrect result.")

if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
