"""Mini Project 15: Expense Analyzer"""
import pandas as pd


def analyze_expenses(records):
    df = pd.DataFrame(records)
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")
    by_category = df.groupby("category")["amount"].sum()
    by_month = df.groupby("month")["amount"].sum()
    return by_category, by_month


def main():
    records = [
        {"date": "2026-01-05", "category": "Food", "amount": 50000},
        {"date": "2026-01-15", "category": "Transport", "amount": 20000},
        {"date": "2026-02-02", "category": "Food", "amount": 45000},
    ]
    by_category, by_month = analyze_expenses(records)
    print(by_category)
    print(by_month)


if __name__ == "__main__":
    main()
