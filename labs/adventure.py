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
