# Tic-Tac-Toe Game

This Python console-based Tic-Tac-Toe game allows users to play against a computer opponent. Enjoy a classic game of strategy and skill!

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/tudorberbecaru/tic-tac-toe.git
    ```

2. Navigate to the project directory:

    ```bash
    cd tic-tac-toe
    ```

3. Run the game:

    ```bash
    python main.py
    ```

## Files

### `board.py`

Defines a class `Board` to represent the game board in Tic Tac Toe.

- `__init__(self)`: Initializes the game board with cells marked as '-' to represent empty positions.
- `print_board(self)`: Prints the visual representation of the game board.
- `update_board(self, position, symbol)`: Updates the game board by marking a cell with the player's symbol.
- `is_valid_choice(self, choice)`: Checks if a player's choice is a valid empty position on the board.
- `is_full(self)`: Checks if the game board is completely filled, indicating a tie.

### `player.py`

Defines a class `Player` to represent a player in the Tic Tac Toe game.

- `__init__(self, symbol)`: Initializes the player with a symbol and turn status.

### `game.py`

Implements the `Game` class, orchestrating the Tic-Tac-Toe game.

- `__init__(self)`: Initializes the game with a welcome message, symbols, and winning combinations.
- `stop_game(self)`: Stops the game by setting the game state to False.
- `user_has_won(self)`: Checks if the user has won by iterating through winning combinations.
- `computer_has_won(self)`: Checks if the computer has won by iterating through winning combinations.
- `start(self)`: Initiates the game loop, allowing players to take turns until there is a winner or tie.

### `main.py`

Runs the Tic-Tac-Toe game by creating an instance of the `Game` class and starting the game loop.

## How to Play

1. Run `main.py` to start the game.
2. Follow the on-screen prompts to make your moves.
3. The game ends when there is a winner or a tie.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Contributions are welcome! Feel free to open issues or submit pull requests.

#### Enjoy playing Tic-Tac-Toe!
