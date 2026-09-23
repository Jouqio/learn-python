"""Mini Project 04: Grade Calculator"""


def weighted_average(scores, weights):
    if len(scores) != len(weights):
        raise ValueError("scores and weights must be the same length")
    total_weight = sum(weights)
    return sum(s * w for s, w in zip(scores, weights)) / total_weight


def letter_grade(average):
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def main():
    scores = [85, 90, 78, 92]
    weights = [0.2, 0.3, 0.2, 0.3]
    average = weighted_average(scores, weights)
    print(f"Weighted average: {average:.2f}")
    print(f"Letter grade: {letter_grade(average)}")


if __name__ == "__main__":
    main()
