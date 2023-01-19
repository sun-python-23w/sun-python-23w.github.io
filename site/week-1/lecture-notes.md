# Lecture 1 — Introduction to Python

```{important}
## Warm up

<!-- TODO: Need to do some sort of 'community building' thing for ~10 minutes-->

- Circle up and introduce names + some fun fact
- Name point & swap game ?

Timecheck: 10 minutes

## Introduction

- Introduce myself
    - School
    - Current job
    - General background
- Course overview
    - This is my first time teaching this
    - Feedback form on the website
    - Structure of lecture / labs
    - What to do if stuck / confused
        - Check the lecture notes
        - Ask someone next to you
        - Raise hand / get my attention
    - ???

Timecheck: 15 minutes
```

(vscode)=
## VSCode

VSCode is a popular choice of _integrated development environment_ (IDE) for developing Python.

![VSCode Interface](./images/vscode-interface.png)

The interface has 3 main regions, shown in purple, green, and orange:

![VSCode Interface with markings to show the main regions](./images/vscode-interface-annotated.png)

1. The file explorer (purple 🟪)
    - Shows a tree view of the current folder
    - Selecting a file here will open it in the editor
    - Can be opened/closed by pressing either button circled in purple
1. The editor (green 🟩)
    - Where we interact with files and write code
1. Console area (orange 🟧)
    - Shows outputs from our code
    - Can be opened/closed by clicking the top right button circled in orange
    - Has 4 different tabs but we will only use the "Terminal" tab (red 🟥)
        - The terminal lets us run commands and see output

Other elements of the interface:
- The arrows in the top bar (<- ->) navigate back / forward through editors
- The gear (⚙️) in the bottom left corner opens settings


## The Interactive Interpreter (Console)

Python has an interactive interpreter that allows you to type code and immediately see the result of evaluating that line.

We can launch the interpreter by running the command `python` in the terminal (see {ref}`vscode` if you're not sure where the terminal is):
```text
% python
Python 3.11.1 ... (a bunch of debug info)
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Here’s an example of adding two numbers in the interpreter:

```python
>>> 1 + 1
2
```

Pressing the return key tells Python to evaluate the line.

### Exiting

When you are finished using the interpreter, type `exit()` and press the return key to exit the interpreter.

```python
>>> exit()
```

## Strings

### Writing

### Combining strings

We can combine multiple strings into one using the addition operator (aka "the plus sign"), `+`:
```python
>>> "abc" + "def"
'abcdef'
```

This might be useful for constructing a date:
```python
>>> "January" + "16th" + "2023"
'January16th2023'
```

We can add some spaces to make it look a little nicer:
```python
>>> "January" + " " + "16th" + ", " + "2023"
'January 16th, 2023'
```

### Can we add strings and numbers?

What happens if we try to build a date using a number?

```python
>>> "January" + 16 + "th"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

We get an error! The first two lines tell us _where_ the error occurred (not very meaningful to us becuase we know it was the line we just entered), and the last line explains what the error was, a _TypeError_, with a message to elaborate, "can only concatenate str (not 'int') to str".

This is telling us that the plus operator, `+`, is not defined when the thing (_operand_) on the left is a string, and the thing on the right is a number. So we cannot use the `+` for strings and numbers.

Generally, when a situation arises during the execution of our code where the behavior is not defined, the best choice is to simple stop and throw an error.

However, there is a simple way to combine numbers and strings...

### Interpolation with `f`-strings

_String interpolation_ allows us to insert things (literals, variables, or expressions) into our strings:

```python
>>> name = "Yoda"
>>> height = 0.66  # meters
>>> f"{name} is {height * 39.37} inches tall and {900} years old!"
'Yoda is 25.9842 inches tall and 900 years old!'
```


## Scripts — Writing and Running Files

The interactive interpreter is a convenient way to experiment and iterate on ideas quickly, but is challenging to reuse.

Alternatively, we can write a series of lines in a file and then evaluate that file all at once.

- Instructions for the command line

    From the command line, run `python <file name>`, where `<file name>` is the path to the file you authored.


## Printing

Unlike the interactive interpreter, running a script does not automatically display a value. In order to display values we can use the `print` function. This script:

```python
print("Hi!")
```

Will produce the following output when run:

```
Hi!
```

```{tip}
`print` is a function, which we *invoke* (tell it to run) using parenthesis.
```

```{important}
TIMECHECK: 30 minutes
```


## Variables

TODO: What are variables and why do we need them?

### Naming Rules

1. Variable names can contain any of these characters:
    - Lowercase letters (`a`, `b`, … , `z`)
    - Uppercase letters (`A`, `B`, … , `Z`)
    - An underscore (`_`)
    - Numbers (`0`, `1`, … `9`)
2. Variable names *may not begin with a number*.
3. Python reserves some special names for itself that you are not allowed to use as names for your variables:

    ```
    False      await      else       import     pass
    None       break      except     in         raise
    True       class      finally    is         return
    and        continue   for        lambda     try
    as         def        from       nonlocal   while
    assert     del        global     not        with
    async      elif       if         or         yield
    ```


#### Examples

Here are some examples of valid names:

```python
x = 1
count = 2
power_level = 9001
```

Here are some names that will cause errors

```yaml
1person = "tim"  # Variable names cannot start with a number
class = "fun"    # The name `class` is reserved by Python
my-variable = 1  # The hyphen will be interpreted as a minus sign
```

### Naming Conventions

- Generally we write variable names all lower case letters
- If a variable name contains multiple words we connect them with underscores—we can't use spaces or python would think each word was a variable name:
    ```python
    days_in_a_year = 365
    ```


<!-- May or may not get to this ? -->

## ---- If time allows ----


## Input

```{important}
TIMECHECK: 55 minutes
```

## Comments

```{important}
Only if ahead of schedule
```

A _comment_ is a line that is ignored by the interpreter and can contain any text. A line is a comment if there is a hashtag, `#` (or "_octothorp_"), at the beginning of the line. Here’s an example:

```python
# This is a comment!
```

We generally use comments for:

- Providing context
- Explaining why a decision was made
- Documenting the inputs and outputs to a function or program

By convention, we put comments *before* the line that they reference. Here’s an example:

```python
# This computes an approximation for pi
# See: https://en.wikipedia.org/wiki/Leibniz_formula_for_π
(1 - 1/3 + 1/5 - 1/7) * 4
```

*Note: It is always a good idea to cite sources and provide links when borrowing formulas or code from elsewhere.*
