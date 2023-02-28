# Adventure Game

An adventure game is a simple exploration and puzzle-solving game.

Here's an example: [Colossal Cave Adventure](https://rickadams.org/adventure/advent/)

![](images/adventure.png)

You can use the letters of cardinal directions (n, e, s, w) to move around, and simple commands, like "get torch" to put items in your inventory.

## Objectives

- Create a simple adventure game with:
    - At least 3 locations
    - An item that can be picked up and used in some way to 'win' the game
    - Clear descriptions of locations with easy to understand directions

## Step by Step Example

This is a very simple adventure game that only implements moving around this game world:

```
    meadow
       ↑
       ↓
    forest  ←→  river
```

```{tip}
💡 Write the code for this yourself without copying and pasting!
```

1. Create a variable `finished` set to `False`
    ```python
    finished = False
    ```
1. Create a `while`-loop that continues while `finished` is not true:
    ```python
    while not finished:
    ```
1. Inside the while loop tell the the user about their surroundings:
    ```python
    while not finished:
        print("You are in a forest")
    ```
1. Prompt the player for their choice of what to do next:
    ```python
    while not finished:
        print("You are in a forest")

        choice = input("Which direction: north or east? Choice: ")
    ```
1. Test out your program. It will probably be a bit repetitive... Press `control` and `c` at the same time to kill the program.
    ```
    You are in a forest
    Which direction: north or east? Choice: north
    You are in a forest
    Which direction: north or east? Choice: east
    You are in a forest
    ```
1. Create a new variable at the top level called `location` and set it to forest. This will allow us to change the player's location and give them different options for where to go next:
    ```python
    finished = False
    location = "forest"
    ```
1. Now check `location` inside the `while` loop:
    ```python
    while not finished:
        if location == "forest":
            print("You are in a forest")

            choice = input("Which direction: north or east? Choice: ")
    ```
1. Add the other locations:
    ```python
    while not finished:
        if location == "forest":
            print("You are in a forest")

            choice = input("Which direction: north or east? Choice: ")
        elif location == "meadow":
            print("You are in a meadow")
        elif location == "river":
            print("You are next to a river")
    ```
1. Next, add an `if` statement below the line that gets the user input (`choice = input(...`) that changes `location` based on `choice`:
    ```python
            choice = input("Which direction: north or east? Choice: ")
            if choice == "north":
                location = "meadow"
            elif choice == "east":
                location = "river"
    ```
1. Add an `else` and print an error (this uses the special f-string syntax that lets us embed variables in strings):
    ```python
            choice = input("Which direction: north or east? Choice: ")
            if choice == "north":
                location = "meadow"
            elif choice == "east":
                location = "river"
            else:
                print(f"I don't understand '{choice}'\n")
    ```
1. Add the input and if statements for meadow and river locations:
    ```python
        elif location == "meadow":
            print("You are in a meadow")

            choice = input("Which direction: south? Choice: ")
            if choice == "south":
                location = "forest"
            else:
                print(f"I don't understand '{choice}'\n")

        elif location == "river":
            print("You are next to a river")

            choice = input("Which direction: west? Choice: ")
            if choice == "west":
                location = "forest"
            else:
                print(f"I don't understand '{choice}'\n")
    ```
1. You should now be able to move around!
    ```
    You are in a forest
    Which direction: north or east? Choice: north
    You are in a meadow
    Which direction: south? Choice: south
    You are in a forest
    Which direction: north or east? Choice: east
    You are next to a river
    Which direction: west? Choice: west
    You are in a forest
    ```

## A More Complicated Example

```python
def describeRoom(roomName):
    if room == "Bridge":
        print(
            "You are standing in the bridge of a rigid airship (blimp).\n"
            + "The captain is franticly manipulating controls; sweat dripping down "
            + "her brow as she barely manages to keep the ship stable.\n"
        )
    elif room == "StarboardEngineRoom":
        # (1) Print a description for the engine room including the mechanic hard
        # at work and the engine not working properly.
        ...

    elif room == "MechanicalRoom":
        # (2) Print a description for the mechanical room that includes a box of
        # fuel hoses on a rack with other spare parts.
        ...


# These track the state of the game
finished = False
room = "Bridge"

# Start off the game by describing the starting room
describeRoom(room)

# Main game loop
while not finished:
    if room == "Bridge":
        choice = input(
            "You can [talk] to the captain, walk [starboard] into the engine room, "
            "or walk [aft] into the mechanical room. \n" + "Choice: "
        )

        print("\n========================================================\n")

        if choice == "talk":
            print(
                "The captain snarls back at you: 'What? Why are you bothering me?? "
                + "Go help the mechanic fix the starboard engine before we crash! "
                + "I won't be able to keep us up much longer.'\n"
            )

        elif choice == "starboard":
            print("You walk starboard into the engine room.\n")

            # By changing the value stored in the `room` variable we can 'move'
            # where the player is in our game world
            room = "StarboardEngineRoom"
            describeRoom(room)

        elif choice == "aft":
            print(
                "You head down the stairs toward the back of the ship and into the "
                + "mechanical room.\n"
            )
            room = "MechanicalRoom"
            describeRoom(room)

        else:
            print(
                f"[!] I don't understand '{choice}'. Please enter one of the words "
                + "surrounded in [square brackets].\n"
            )

    elif room == "StarboardEngineRoom":
        # (3) Using the code inside the `if` block for `"Bridge"` above implement
        # getting a choice from the user to let them go back to the bridge, or to talk
        # to the mechanic who tells the player the primary fuel hose burst and he needs
        # a replacement.
        ...

    elif room == "MechanicalRoom":
        # (4) Using the code inside the `if` block for `"Bridge"` above implement
        # getting a choice from the user to let them go back to the bridge.
        ...


# Make sure the program works by moving to the 3 different rooms
#
# Next steps:
# (5) Create a new variable `hasFuelHose` on line 22 to indicate whether or not the player
#     has picked up the replacement fuel hose from the mechanical room.
# (6) Add a choice in the mechanical room that allows the player to pick up the fuel
#     hose, and if the player selects that set `hasFuelHose` to True.
# (7) If `hasFuelHose` is True (and only when `hasFuelHose` is True), show a new
#     option in the mechanical room to give the mechanic the hose, then print a
#     description of the mechanic fixing the engine, and set `finished` to True to
#     end the game.
# (8) Add more features! Maybe more rooms or parts the mechanic needs!
#     Or, create a whole new game!

```
