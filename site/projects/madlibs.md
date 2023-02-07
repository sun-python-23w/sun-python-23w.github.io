
# Mad libs

1. Select a Mad-Libs page from the book.

1. Create a new file `madlib.py` (see {ref}`new-file` for a refresher).

1. Implement the madlib in a program:
    - Use variables to store the input words that will fill in the blanks.
        If there are multiple inputs with the same prompt you can add a number to the end of the variable name (for example, `verb2`).
    - You only need to put the first 2 or 3 sentences in your program (but you're welcome to do the whole thing!).

    Here's an example:

    ```python
    adjective = "_"
    first_name = "_"
    adjective2 = "_"
    noun = "_"

    print(
        f"They say my school is haunted! " +
        f"My {adjective} friend {first_name} says she saw " +
        f"a {adjective2} {noun} floating at the end of the " +
        f"hall near the cafeteria."
    )
    ```

1. Pair up with someone else in the class and for each of you:
    - Prompt your partner for the input words and write them as string literal in your program
    - Run the program to generate an output!

    ```python
    adjective = "disappointing"
    first_name = "Charles"
    adjective2 = "sparkling"
    noun = "goose"

    print(
        "They say my school is haunted! " +
        f"My {adjective} friend {first_name} says she saw " +
        f"a {adjective2} {noun} floating at the end of the " +
        "hall near the cafeteria."
    )
    ```

    Here's the output from running `python madlib.py`:

    ```
    They say my school is haunted! My disappointing friend Charles
    says she saw a sparkling goose floating at the end of the hall
    near the cafeteria.
    ```
