"""Mini Project 14: Student Data Analyzer"""
import pandas as pd


def analyze_grades(records):
    df = pd.DataFrame(records)
    summary = {
        "average": df["score"].mean(),
        "top_student": df.loc[df["score"].idxmax(), "name"],
        "pass_rate": (df["score"] >= 60).mean() * 100,
    }
    return summary


def main():
    records = [
        {"name": "Adi", "score": 78},
        {"name": "Bunga", "score": 92},
        {"name": "Cahyo", "score": 55},
    ]
    print(analyze_grades(records))


if __name__ == "__main__":
    main()
