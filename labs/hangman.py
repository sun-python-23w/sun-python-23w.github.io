from random import choice

words = ["apple", "banana", "cherry", "orange", "grape"]


def draw_hangman(incorrect_guesses):
    if incorrect_guesses == 0:
        print(" +--+")
        print("    |")
        print("    |")
        print("    |")
    elif incorrect_guesses == 1:
        print(" +--+")
        print(" O  |")
        print("    |")
        print("    |")
    elif incorrect_guesses == 2:
        print(" +--+")
        print(" O  |")
        print(" |  |")
        print("    |")
    elif incorrect_guesses == 3:
        print(" +--+")
        print(" O  |")
        print(" |  |")
        print("/   |")
    elif incorrect_guesses == 4:
        print(" +--+")
        print(" O  |")
        print(" |  |")
        print("/ \ |")
    elif incorrect_guesses == 5:
        print(" +--+")
        print(" O  |")
        print("-|  |")
        print("/ \ |")
    elif incorrect_guesses == 6:
        print(" +--+")
        print(" O  |")
        print("-|- |")
        print("/ \ |")


chosen_word = choice(words)

letters = list(chosen_word)
guesses = []
for letter in letters:
    guesses.append("_")

incorrect_guesses = 0

while guesses != letters:
    draw_hangman(incorrect_guesses)

    print(" ".join(guesses))
    guess = input("Guess a letter: ")

    guess_in_word = False
    for index in range(len(letters)):
        if letters[index] == guess:
            guesses[index] = guess
            guess_in_word = True

    if guess_in_word:
        print("Yes! That letter is in the word.")
    else:
        incorrect_guesses += 1
        print("No. That letter is not in the word...")


print("You win!")
