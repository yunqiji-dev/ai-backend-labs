"""
Exercise 6: Data Types (The Hidden Trap)
Why did "100" + "200" become "100200"? Because they were strings!
You MUST check and convert types before doing anything else.

Goal:
1. Inspect data types using `df.dtypes`.
2. Convert 'Price' from object (string) to float using `pd.to_numeric`.
3. Convert 'Quantity' to integer.

Execution mode: python 06_data_types.py
"""

import os

import pandas as pd


def setup_data():
    data = {
        "Product": ["Apple", "Banana", "Orange"],
        "Price": ["$1.50", "0.80", "1.20"],  # '$1.50' makes this a string
        "Quantity": ["10", "20", "15"],  # Strings "10"
    }
    df = pd.DataFrame(data)
    df.to_csv("types.csv", index=False)
    print("✅ Test data types.csv generated")


def cleanup_data():
    if os.path.exists("types.csv"):
        os.remove("types.csv")
        print("🧹 Cleaning up test data")


def process_data():
    df = pd.read_csv("types.csv")
    print("--- Raw Data Types ---")
    print(df.dtypes)
    print("\n--- Raw Data ---")
    print(df)

    # TODO: 1. Clean '$' so we can convert
    df["Price"] = df["Price"].str.replace("$", "", regex=False)

    # TODO: 2. Convert Price to Float
    # errors='coerce' is safe: turns invalid text into NaN
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

    # TODO: 3. Convert Quantity to Integer
    df["Quantity"] = df["Quantity"].astype(int)

    print("\n--- Fixed Data Types ---")
    print(df.dtypes)

    # Calculate Total to prove it works
    total_val = (df["Price"] * df["Quantity"]).sum()
    print(f"\nTotal Inventory Value: {total_val}")

    # --- Verification ---
    if df["Price"].dtype == "float64" and df["Quantity"].dtype == "int32":
        print("\n🎉 Congratulations! Exercise 6 completed!")
    else:
        # Note: Windows might use int32 or int64 depending on pandas version
        if "int" in str(df["Quantity"].dtype):
            print("\n🎉 Congratulations! Exercise 6 completed!")
        else:
            print("\n❌ Incorrect result. Check dtypes.")


if __name__ == "__main__":
    setup_data()
    try:
        process_data()
    finally:
        cleanup_data()
