# Lecture Notes

```{important}
**Beginning activity**

- Circle and introduce names + some fun fact
- 'foo/bar/baz' like zip/zap/zop ...?
```

```{warning}
Still a work in progress!
```

## `for`-loops

- Syntax is `for <var_name> in <collection>:` and then the 'body' of the for loop is all indented.
- Example:
    ```python
    for letter in "hello":
        print(letter)
    ```

    Produces the output:

    ```
    h
    e
    l
    l
    o
    ```


### Ranges

Allow executing a block a certain number of times based on an integer number:

```python
for iteration in range(3):
    print("hello")
```

```
hello
hello
hello
```

The variable starts at `0`, and goes up until one less than the number we specify:

```python
for iteration in range(3):
    print(iteration)
```

```
0
1
2
```



## `Boolean` expressions

Boolean expression is any expression that can determined to be 'true' or 'false'. You can think of boolean expressions as asking a yes or no question (where we say `True` or `False` instead of "yes" or "no").

### `==`

We use 2 equals signs to be different from the 'assignment operator' that we use to store a value in a variable.

Allows comparing to see if two values are the same:

```python
>>> "hello" == "hello"
True
>>> "a" == "abc"
False
>>> "Yes" == "yes"
False
```

### Numerical comparisons

We can use the less than (`<`) and greater than (`>`) signs to compare numbers.

```python
>>> 3 > 1
True
>>> 100 < 1
False
```

## Conditional blocks (`if`)

We can decide whether or not to evaluate some code based on a boolean expression.

```python
if user_name == "admin":
    print("As you wish!")
```

### `else`

We can provide an alternative piece of code to run when the condition is `False` using `else`:

```python
if guess == target:
    print("You win!")
else:
    print("Try again")
```
