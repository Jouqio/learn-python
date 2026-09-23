"""Mini Project 13: CSV Data Analyzer"""
import pandas as pd

SAMPLE_FILE = "sample_sales.csv"


def create_sample_file():
    df = pd.DataFrame({
        "product": ["A", "B", "C", "A", "B"],
        "units_sold": [10, 5, 8, 12, 7],
        "price": [15000, 25000, 10000, 15000, 25000],
    })
    df.to_csv(SAMPLE_FILE, index=False)


def analyze(filepath):
    df = pd.read_csv(filepath)
    df["revenue"] = df["units_sold"] * df["price"]
    return df.groupby("product")["revenue"].sum()


def main():
    create_sample_file()
    print(analyze(SAMPLE_FILE))


if __name__ == "__main__":
    main()
