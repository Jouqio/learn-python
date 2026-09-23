"""Mini Project 07: Expense Tracker"""
import csv
import os
from datetime import date

DATA_FILE = "expenses.csv"


def add_expense(category, amount, when=None):
    when = when or date.today().isoformat()
    file_exists = os.path.exists(DATA_FILE)
    with open(DATA_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "category", "amount"])
        writer.writerow([when, category, amount])


def summarize_by_category():
    totals = {}
    if not os.path.exists(DATA_FILE):
        return totals
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            totals[row["category"]] = totals.get(row["category"], 0) + float(row["amount"])
    return totals


def main():
    add_expense("Food", 50000)
    add_expense("Transport", 20000)
    print(summarize_by_category())


if __name__ == "__main__":
    main()
