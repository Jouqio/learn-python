"""Mini Project 02: Number Guessing Game"""
import random


def play_game(lower=1, upper=100, max_attempts=7):
    secret = random.randint(lower, upper)
    for attempt in range(1, max_attempts + 1):
        guess_text = input(f"Attempt {attempt}/{max_attempts} - Guess ({lower}-{upper}): ")
        try:
            guess = int(guess_text)
        except ValueError:
            print("Please enter a valid whole number.")
            continue
        if guess == secret:
            print(f"Correct! The number was {secret}.")
            return True
        print("Too low!" if guess < secret else "Too high!")
    print(f"Out of attempts. The number was {secret}.")
    return False


if __name__ == "__main__":
    play_game()
