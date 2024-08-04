# Commander

Welcome to Commander, a text-based adventure game!

## Game Overview

In Commander, you explore rooms, take items, and use commands to interact with your environment. The game allows you to create custom commands dynamically to enhance your gameplay experience.

## How to Play

To start playing the game, go to [Commander on Replit](https://replit.com/@calestialashley/Commander?s=app).

### Available Commands

- **help**: Show the help message with a list of available commands.
- **look**: Look around your current location.
- **move**: Move to another location.
- **take [item]**: Take an item from your current location.
- **inventory**: Show your current inventory.
- **examine [item]**: Examine an item in your inventory.
- **quit**: Exit the game.
- **$createcommand [name]**: Create a new custom command.

### Creating Custom Commands

You can create custom commands to add new interactions to the game. To create a custom command, use the `$createcommand` command followed by the name of the new command. You will be prompted to enter a description and a message for the new command.

For example:
```
$createcommand greet
Enter a description for the command: Greet someone in the game
Enter the message for the command: You greet the person warmly.
```

Once created, you can use the new command by typing its name:
```
greet
```

### Example Gameplay

```
Welcome to the game!
Commands:
 - help: Show this help message
 - look: Look around
 - move: Move to another location
 - take [item]: Take an item
 - inventory: Show your inventory
 - examine [item]: Examine an item in your inventory
 - quit: Exit the game
 - $createcommand [name]: Create a new command

Enter a command: look
You are in a room. There is a door to the north.

Enter a command: move
You move to another room. There is a door to the south.

Enter a command: $createcommand greet
Enter a description for the command: Greet someone in the game
Enter the message for the command: You greet the person warmly.
Command 'greet' created successfully.

Enter a command: greet
You greet the person warmly.
```

## License

This game is provided as-is without any warranty. Feel free to use and modify it as you like.

Enjoy playing Commander!
```
