.. sectnum::

# Lab 1 — Mad Libs

```{important}
Write on the board:
    sun-python-23w.github.io
```

```{important}
- Hand out laptops
- Use post-its to keep track of who has which laptop ...?
```

## Set up

1. Launch the application **Visual Studio Code** (should be in the dock)
1. Open the folder `week-1` in the `python` folder on the desktop.

    1. You can open the folder from VSCode by clicking *Open Folder* from the explorer, and then selecting `python` and `week-1`.
    ![](images/vscode-start.png)
    ![](images/vscode-open-folder.png)

    OR

    1. You can navigate to the `week-1` folder in finder and drop it in VSCode.
    ![](images/vscode-drop-folder.png)

Once your application looks like this you are ready to commence the lab!
![](images/vscode-interface.png)

See {ref}`vscode` for a refresher on the interface and buttons.

---


## Exercises

### Greetings

1. Start the python interactive interpreter (enter `python` in the terminal)

    You should see the interactive prompt:
    ```python
    >>>
    ```

1. Write `"Hello"` and press enter.

    Notice this string is already a value so there is nothing to evaluate and it is simply printed back out:

    ```{tip}
    We call this a _literal_, because when we define it we are _literally_ typing out the value.
    ```

1. Store `"Hello"` in a variable named `word`.

1. Type the name of the variable, `word`, and press enter.

    Notice that the output is the value _stored in_ the variable.

1. Next, assign to the variable `greeting` the result of combining `word` with a comma, a space, and your name (hint: see {ref}`combining-strings`).

    ```{caution}
    Do not type `"Hello"` out again for this step!
    ```

1. Display the value of `greeting` to check it is correct. It should look something like this:

    ```python
    >>> greeting
    'Hello, Julian'
    ```

1. Let's change up our greeting. Choose a new word you would use to greet someone and store that in the `word` variable (e.g., "Howdy", "Salutations", "Greetings", or anything you like).

1. Display the value of `greeting` again.

    Notice that the value of `greeting` _has not changed_. Take a moment to think about why this is the case.

1. Finally, define `greeting` again exactly as you did before (although the value of `word` has changed) by using the up arrow to step through your command history

1. Display `greeting` to check that it was updated.

    I stored `"Howdy"` in my `word` variable and got this output; your output should look similar but will have a different word and name:
    ```python
    >>> greeting
    'Howdy, Julian'
    ```

1. Exit the interactive interpreter by typing `exit()` and pressing enter.

<!-- Validated this exercise works as written ! -->

### Hello, world

Now that we're comfortable working in the interactive intepreter lets take a look at writing and running files.

1. Use `print()` to write a program in the file `hello-world.py` that will display **Hello, world!** when run:

    ```python
    % python hello-word.py
    "Hello, world!"
    ```

    ```{tip}
    This program will only be one line long.
    ```

    ```{note}
    The first known 'Hello world' program was written in [1974](https://en.m.wikipedia.org/wiki/%22Hello,_World!%22_program).
    ```

<!--
### Colors

Read the blog post [Build your own Command Line with ANSI escape codes](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html) and put colors into your madlibs program so that the final output displays each type of word inserted in a different color (for example, green corresponds to verb, yellow to noun, etc.).


```{important}
If everyone finishes the lab early:

- (10-15 minutes) explain `input()` and have people augment their mad libs program
- (5 minutes) start a discussion:
    - What did people learn?
    - What was hard?
    - What can we improve for next time?
``` -->
