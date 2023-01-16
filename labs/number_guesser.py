# === first version ===
# + constant number to guess
# ---
# - printing
# - variables
# - strings
# - input
# - ints
# - converting from string to int
# - `while` loop

number = 7
guess = None

win = False

while not win:
    guess = int(input(f"Guess: "))
    win = guess == number

print("You win!")

# === second version ===
# + random number
# - modules
# - `randint` function

from random import randint

number = randint(1, 10)

guess = None

while guess != number:
    guess = int(input(f"Guess: "))

print("You win!")

# === third version ===
# + tells the player if they are too low or too high
# - comparing integers
# - `if` statements

import random

number = random.randint(1, 10)

guess = None

while guess != number:
    guess = int(input(f"Guess: "))

    if guess > number:
        print("Too high!")
    if guess < number:
        print("Too low!")

print("You win!")

# === fourth version ===
# + limits the number of guesses the player can make

MAX_GUESSES = 3

import random

number = random.randint(1, 10)

guess = None
guesses = 0

while guess != number and guesses <= MAX_GUESSES:
    guess = int(input(f"[{MAX_GUESSES - guesses} remaining] guess: "))

    if guess > number:
        print("Too high!")
    if guess < number:
        print("Too low!")

    guesses += 1

if guess == number:
    print("You win!")
else:
    print("Better luck next time...")


# === stretch ===
# + handle any input without crashing (example: user just hits enter, use types a letter, etc.)
# + don't allow the user to enter numbers outside the range
# + use ANSI colors to make the messages different colors
# +
