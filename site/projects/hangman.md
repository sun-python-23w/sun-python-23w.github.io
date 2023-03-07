# Hangman

A guided set of instructions for the classic game of hangman!

```text
_ _ a p e
Guess a letter: g
That is correct!

g _ a p e
Guess a letter:
```

1. Start by opening the [future coder editor](https://futurecoder.io/course/#ide) or creating a new file in vscode (see {ref}`new-file` for a refresher).

1. To begin, we import the function `choice` from the `random` library.

    Write the following code in your editor:

    ```python
    from random import choice
    ```

    This is a function that takes a `list` as an input and returns a random element from the list.

    (this is just an example and does not go in your code)

    ```python
    >>> from random import choice
    >>> choice(["heads", "tails"])
    "heads"
    ```

1. Create a list of words that the game will choose from. I'm going to list some fruits but you can choose any words you want. Try to generate 6-12:

    ```python
    words = ["apple", "banana", "cherry", "grape", "melon", "orange"]
    ```

1. Use `choice` to store a random word in the variable `word`:

    ```python
    chosen_word = choice(words)
    ```

1. Test the program. Temporarily add a print statement and run the program multiple times to see different outputs:

    ```python
    print(chosen_word)
    ```

    Delete the print statment before continuing.

1. Use the `list` function to create a list out of `word` where each element in the list is a single letter:

    ```python
    letters = list(chosen_word)
    ```

    Here's an example of how `list` works (this doesn't go in your code):

    ```python
    >>> list("hello")
    ['h', 'e', 'l', 'l', 'o']
    ```

1. Create a new variable `guesses` that is made up of underlines and is the same length as `letters`

    ```{tip}
    This time I'm not going to give you the code—let me know if you need any hints!
    ```

1. Next, we'll create the `while` loop that drives the game:

    ```python
    while guesses != letters:
        print(guesses)
        guess = input("Guess a letter: ")
    ```

1. Try out the program!

    Here's what happens when I run the program:

    ```python
    ['_', '_', '_', '_', '_', '_']
    Guess a letter: a
    ['_', '_', '_', '_', '_', '_']
    Guess a letter:
    ```

    The current way `guesses` is displayed (as a list with single commans, `'`) is pretty ugly; let's make that look better!

1. Change the line `print(guesses)` to the following:

    ```python
        print(" ".join(guesses))
    ```

    The function `" ".join` function takes a list of strings and _joins_ them together with the string `" "`.

    It should now look something like this:

    ```text
    _ _ _ _ _ _
    Guess a letter:
    ```

1. Finally, let's change the `guesses` list based on the user input (in the variable `guess`).

    This goes _inside_ the `while` loop (indented by 4 spaces), below the line `guess = input("Guess a letter: ")`:

    ```python
        for index in range(len(letters)):
            if letters[index] == guess:
                guesses[index] = guess
    ```

1. Test out the game! You should now be able to play and even win the game (although without any messaging)

    Here's the current program:

    ```python
    from random import choice

    words = [...]  # Your words are here

    chosen_word = choice(words)

    letters = list(chosen_word)
    guesses = []
    for letter in letters:
        guesses.append("_")

    while guesses != letters:
        print(" ".join(guesses))
        guess = input("Guess a letter: ")

        for index in range(len(letters)):
            if letters[index] == guess:
                guesses[index] = guess
    ```


    Here's an example from me running the program:

    ```text
    _ r a _ g _
    Guess a letter: b
    _ r a _ g _
    Guess a letter: o
    o r a _ g _
    Guess a letter: n
    o r a n g _
    Guess a letter: e
    ```

    It would be nice to get some feedback on whether or not the character we guessed is correct or not. Let's do that next.

1. Create a new variable `guess_in_word` which stores a Boolean value (`True` or `False`) that is `True` when `guess` is in `letters`. We will add one line above the `for` loop, and another line inside the `if` statement inside the `for` loop. I've used comments to point out which lines are new:

    ```python
        guess_in_word = False  # <- new line
        for index in range(len(letters)):
            if letters[index] == guess:
                guesses[index] = guess
                guess_in_word = True  # <- new line
    ```

1. Next, add a new `if` and `else` statement below the entire `for` loop but inside the `while` loop that prints out whether or not the letter is in the word:

    ```python
        guess_in_word = False
        for index in range(len(letters)):
            if letters[index] == guess:
                guesses[index] = guess
                guess_in_word = True

        # New lines:
        if guess_in_word:
            print("Yes! That letter is in the word.")
        else:
            print("No. That letter is not in the word...")
    ```


1. Test out the program.

    Here's the output I got:

    ```test
    _ _ _ _ _ _
    Guess a letter: a
    Yes! That letter is in the word.
    _ a _ a _ a
    Guess a letter: b
    Yes! That letter is in the word.
    b a _ a _ a
    Guess a letter: c
    No. That letter is not in the word...
    ```

1. The last thing we're going to add is a print statement for winning. Add this at the very end of the program and _outside_ the `while` loop (not indented at all):

    ```python
    print("You win!")
    ```

## Challenges

- Limit the number of incorrect letter guesses to 6
    ```{tip}
    Create a variable outside and _before_ the `while` loop to track this and increase it by one if `guess_in_word` is false (inside the `else`). Check this variable is less than `6` in the `while` statement.
    ```

- Create a function that draws a partial stick figure for 0-6 incorrect letter guesses and call the function inside the `while` loop:

    ```python
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
        # Continue on your own ...
    ```
