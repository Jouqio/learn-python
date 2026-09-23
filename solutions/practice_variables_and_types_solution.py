"""
Solutions for exercises/beginner/practice_variables_and_types.py
"""


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def is_even(number):
    return number % 2 == 0


def average_of_three(a, b, c):
    return (a + b + c) / 3


if __name__ == "__main__":
    print(celsius_to_fahrenheit(100))
    print(is_even(7))
    print(average_of_three(4, 8, 12))
