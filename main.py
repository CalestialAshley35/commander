# Dictionary to store dynamic commands
commands = {}

def show_help():
    print("Commands:")
    print(" - help: Show this help message")
    print(" - look: Look around")
    print(" - move: Move to another location")
    print(" - take [item]: Take an item")
    print(" - inventory: Show your inventory")
    print(" - examine [item]: Examine an item in your inventory")
    print(" - quit: Exit the game")
    print(" - $createcommand [name]: Create a new command")

    # Include dynamically created commands
    if commands:
        print("\nCustom Commands:")
        for cmd, details in commands.items():
            print(f" - {cmd}: {details['description']}")

def look_around():
    print("You are in a room. There is a door to the north.")

def move():
    print("You move to another room. There is a door to the south.")

def take(item):
    print(f"You have taken the {item}.")

def show_inventory():
    print("Your inventory is empty.")

def examine(item):
    print(f"You see nothing special about the {item}.")

def create_command(name, description, message):
    if name in commands:
        print(f"The command '{name}' already exists.")
    else:
        commands[name] = {
            "description": description,
            "message": message
        }
        print(f"Command '{name}' created successfully.")

def main():
    print("Welcome to the game!")
    show_help()

    while True:
        command = input("\nEnter a command: ").strip().lower()
        parts = command.split()
        action = parts[0]

        if action == "help":
            show_help()
        elif action == "look":
            look_around()
        elif action == "move":
            move()
        elif action == "take":
            if len(parts) > 1:
                item = parts[1]
                take(item)
            else:
                print("Take what?")
        elif action == "inventory":
            show_inventory()
        elif action == "examine":
            if len(parts) > 1:
                item = parts[1]
                examine(item)
            else:
                print("Examine what?")
        elif action == "quit":
            print("Goodbye!")
            break
        elif action == "$createcommand":
            if len(parts) > 1:
                name = parts[1]
                description = input("Enter a description for the command: ").strip()
                message = input("Enter the message for the command: ").strip()
                create_command(name, description, message)
            else:
                print("Usage: $createcommand [name]")
        elif action in commands:
            print(commands[action]["message"])
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()