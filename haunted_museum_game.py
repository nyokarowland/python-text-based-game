# Nyoka Rowland

def show_instructions():
    """Display the game title, goal, and valid commands."""
    print("Haunted Museum Text Adventure Game")
    print("Collect 6 items before entering the Basement Vault to defeat the Cursed Curator.")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: get [item name]")
    print("-" * 50)


def show_status(current_room, inventory, rooms):
    """Display the player's current room, inventory, and any item in the room."""
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")

    # Show item if the room has one and it has not already been collected
    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")

    print("-" * 50)


def main():
    # Dictionary linking rooms to other rooms and linking one item to each room
    rooms = {
        "Lobby": {"South": "Art Gallery"},
        "Art Gallery": {
            "North": "Lobby",
            "South": "Security Office",
            "East": "Ancient Egypt Room",
            "item": "Flashlight"
        },
        "Ancient Egypt Room": {
            "West": "Art Gallery",
            "item": "Ancient Coin"
        },
        "Security Office": {
            "North": "Art Gallery",
            "South": "Library Archive",
            "East": "Storage Room",
            "item": "Keycard"
        },
        "Storage Room": {
            "West": "Security Office",
            "item": "Protective Gloves"
        },
        "Library Archive": {
            "North": "Security Office",
            "South": "Basement Vault",
            "East": "Restoration Lab",
            "item": "Map"
        },
        "Restoration Lab": {
            "West": "Library Archive",
            "item": "Mirror Charm"
        },
        "Basement Vault": {
            "North": "Library Archive",
            "villain": "Cursed Curator"
        }
    }

    # Starting values
    current_room = "Lobby"
    inventory = []
    items_needed = 6

    show_instructions()

    # Gameplay loop
    while True:
        show_status(current_room, inventory, rooms)

        command = input("Enter your move:\n").strip()

        # Input validation for blank entry
        if command == "":
            print("Invalid input!")
            continue

        # Split command into parts
        command_parts = command.split(" ", 1)
        action = command_parts[0].lower()

        # Move command
        if action == "go":
            if len(command_parts) < 2:
                print("Invalid input!")
                continue

            direction = command_parts[1].title()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]

                # Lose condition: player enters villain room before collecting all items
                if current_room == "Basement Vault" and len(inventory) < items_needed:
                    print(f"You are in the {current_room}")
                    print(f"Inventory: {inventory}")
                    print("You see the Cursed Curator")
                    print("NOM NOM...GAME OVER!")
                    print("Thanks for playing the game. Hope you enjoyed it.")
                    break

                # Win condition: player enters villain room after collecting all items
                elif current_room == "Basement Vault" and len(inventory) == items_needed:
                    print(f"You are in the {current_room}")
                    print(f"Inventory: {inventory}")
                    print("You see the Cursed Curator")
                    print("Congratulations! You collected all items and defeated the Cursed Curator!")
                    print("Thanks for playing the game. Hope you enjoyed it.")
                    break
            else:
                print("You can't go that way!")

        # Get item command
        elif action == "get":
            if len(command_parts) < 2:
                print("Invalid input!")
                continue

            item_name = command_parts[1].strip().lower()

            if "item" in rooms[current_room]:
                room_item = rooms[current_room]["item"]

                if item_name == room_item.lower():
                    inventory.append(room_item)
                    del rooms[current_room]["item"]
                    print(f"{room_item} retrieved!")
                else:
                    print("Can't get that item!")
            else:
                print("There is no item in this room!")

        # Invalid command
        else:
            print("Invalid input!")


# Run the game
if __name__ == "__main__":
    main()