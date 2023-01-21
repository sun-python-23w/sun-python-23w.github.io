# Lecture Notes


```{important}
# Beginning activity

- Circle and introduce names + some fun fact
- 'foo/bar/baz' like zip/zap/zop ...?
```

```{warning}
Still a work in progress!
```

## Comments

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


## Input

`input()` provides a way for our program to request input from the user.

- The _parameter_ (an input) for the prompt to show to the user
- The
