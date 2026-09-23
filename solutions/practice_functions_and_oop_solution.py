"""
Solutions for exercises/intermediate/practice_functions_and_oop.py
"""


class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def word_frequencies(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    rect = Rectangle(4, 5)
    print(rect.area(), rect.perimeter())
    print(word_frequencies("the quick brown fox jumps over the lazy dog the fox runs"))
