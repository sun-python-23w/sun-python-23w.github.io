from math import pi
from turtle import Screen, Turtle

# 'FACTOR' signifies the multiplicative factor
# which expands or shrinks the scale of the plot:
FACTOR = 2


def fiboPlot(n):
    a, b = 0, 1

    # Setting the colour of the plotting pen to blue
    turtle.pencolor("blue")

    # Drawing the first square
    for _ in range(4):
        turtle.forward(b * FACTOR)
        turtle.left(90)

    turtle.right(90)

    # Drawing the rest of the squares
    for _ in range(n - 1):
        # Proceeding in the Fibonacci Series
        a, b = b, b + a

        turtle.backward(a * FACTOR)
        turtle.right(90)
        turtle.forward(b * FACTOR)
        turtle.left(90)
        turtle.forward(b * FACTOR)
        turtle.left(90)
        turtle.forward(b * FACTOR)

    # Bringing the pen to starting point of the spiral plot
    turtle.penup()
    turtle.setposition(FACTOR, 0)
    turtle.setheading(90)
    turtle.pendown()

    # Setting the colour of the plotting pen to red
    turtle.pencolor("red")

    a, b = 0, 1

    # Fibonacci Spiral Plot
    for _ in range(n):
        print(b)
        distance = pi * b * FACTOR / 180

        for _ in range(90):
            turtle.forward(distance)
            turtle.left(1)

        a, b = b, b + a


# Input the number of iterations our algorithm will run:
n = int(input("Enter the number of iterations (must be > 1): "))

# Plot the fibonacci spiral fractal and
# print the corresponding fibonacci number:
if n > 0:
    print("Fibonacci series for", n, "elements:")
    screen = Screen()
    turtle = Turtle()
    turtle.speed("fastest")
    fiboPlot(n)
    screen.mainloop()
else:
    print("Number something or other")
