finished = False
location = "forest"

while not finished:
    if location == "forest":
        print("You are in a forest")

        choice = input("Which direction: north or east? Choice: ")
        if choice == "north":
            location = "meadow"
        elif choice == "east":
            location = "river"
        else:
            print(f"I don't understand '{choice}'\n")

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
