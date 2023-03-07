# Week 4

## Lecture

- comments
- `input()`
- `while` loops
- `import`s
- pseudocode for a guessing game

## Lab

Try to finish up all [futurecoder.io](https://futurecoder.io) labs up to **If statements**

_You can skip the "Understanding Programs With snoop" exercise in **If Statements**._

### A Guessing Game

Open up the [future coder editor](https://futurecoder.io/course/#ide) and paste in the following starter code:

```python
import random

# This generates a random number between 1 and 10.
number = random.randint(1,10)

# Tracks whether or not the player has won
win = False

while win == False:
    # This prompts the user for input and converts the
    # input to a number ('int' is short for 'integer').
    guess = int(input(f"Guess: "))

    if guess == number:
        win = True

    print("No! Guess again")

print("You win!")

# Tasks (you can delete the task descriptions as you complete them):
#
# 1. Try running the program, then read through the program and make
#    sure you understand it.
# 2. Change the program so it only prints 'No! Guess again' when
#    the user guesses incorrectly (right now it always prints out
#    even when the guess is correct and they win).
# 3. Change the program to tell the user if their guess is higher or
#    lower than the number (using `<` or `>`)
# 4. Create a new variable to keep track of the number of guesses and
#    print it out to the user after each guess.
# 5. Make the game end after 4 guesses.
# 6. (optional challenge) Tell the user if their guess is less than 1
#    or greater than 10 and ask them to enter again--without increasing
#    the number of guesses they have made.
```


### Baby (Turtle) Steps

Open up the [Python and Turtle website](https://pythonandturtle.com/turtle) (unfortunately FutureCoder does not support `turtle`) and paste in the following starter code:

```python
# This tells turtle to create a new instace of a 'Turtle', which we can also
# think of as our 'cursor' or 'pen' for drawing with.
t = turtle.Turtle()

# Here's an example program that draws a square:

t.color('red')

t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)


# Tasks (you can delete each task line as you do them):
#
# 1. Re-write the code to use a `for` loop
# 2. Draw a shape with 8 sides
# 3. Draw a shape with 10 sides
# 4. Modify the program so that the number of sides is input by the user
#    (using the 'input()' function)


# -- Don't edit below this line! --
# This function starts the animation
turtle.done()
```

### Adding some color

Open up the [Python and Turtle website](https://pythonandturtle.com/turtle) (unfortunately FutureCoder does not support `turtle`) and paste in the following starter code:

```python
t = turtle.Turtle()

# Here's an example program using turtle to draw a triangle with a green border
# and yellow fill color:

t.color('green')
t.fillcolor('yellow')

# This tells turtle to start watching our pen for fill coloring
t.begin_fill()

for _ in range(3):
    t.forward(60)
    t.left(120)

# This tells turtle our shape is finished and we want to fill it in now
t.end_fill()


# Tasks (you can delete each task line as you do them):
#
# 1. Change the line color to red
# 2. Change the fill color to pink
# 3. Draw a star with a blue line color and red fill color


# -- Don't edit below this line! --
# This function starts the animation
turtle.done()
```

### Marching turtles

Open up the [Python and Turtle website](https://pythonandturtle.com/turtle) (unfortunately FutureCoder does not support `turtle`) and paste in the following starter code:

```python
# Creates a cursor with the shape of a turtle
t = turtle.Turtle('turtle')

# Here's an example program drawing three turtles in a line:

# 'penup' turns off drawing a line while the cursor is moving
t.penup()

# 'goto' moves the cursor to a location.
t.goto(100,0)
# 'stamp places a picture of the cursor shape on the canvas at the current location
t.stamp()
t.goto(50,0)
t.stamp()
t.goto(0,0) # Back to the start (middle of screen)
t.stamp()

# 'pendown' resumes drawing a line when the cursor moves
t.pendown()

# Tasks (you can delete each task line as you do them):
#
# 1. Change the program to draw a grid of 4 x 4 turtle
# 2. Make all the turtle face upwards ^
# 3. (if you haven't already) write the program using two nested `for` loops


# -- Don't edit below this line! --
# This function starts the animation
turtle.done()
```
