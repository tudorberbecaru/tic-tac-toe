from board import Board
from player import Player
from random import choice


class Game:
    def __init__(self):

        # Initialize the game with a welcome message and symbols
        self.message = \
            """
Welcome to Tic Tac Toe!
You are playing against a robot.

How To Play:
TL - top left    | TM - top middle    | TR - top right
ML - middle left | MM - center        | MR - middle right
BL - bottom left | BM - bottom middle | BR - bottom right
            """
        self.symbols = ["X", "0"]

        # Define the winning combinations on the board
        self.winning_combinations = [
            ['TL', 'TM', 'TR'],
            ['ML', 'MM', 'MR'],
            ['BL', 'BM', 'BR'],
            ['TL', 'ML', 'BL'],
            ['TM', 'MM', 'BM'],
            ['TR', 'MR', 'BR'],
            ['TL', 'MM', 'BR'],
            ['BL', 'MM', 'TR']
        ]

        # Randomly assign symbols to the user and computer
        random_symbol = choice(self.symbols)
        self.symbols.remove(random_symbol)
        remaining_symbol = self.symbols[0]
        self.user = Player(symbol=random_symbol)
        self.computer = Player(symbol=remaining_symbol)

        # Initialize the game state
        self.game_is_on = True
        self.board = Board()

        # Create a list of possible choices on the game board by extracting keys from the board's cells
        self.possible_choices = list(self.board.cells.keys())

    def stop_game(self):
        # Stop the game by setting the game state to False
        self.game_is_on = False

    def user_has_won(self):
        # Check if the user has won by iterating through winning combinations
        for combination in self.winning_combinations:
            if all(self.board.cells[position] == self.user.symbol for position in combination):
                return True
        return False

    def computer_has_won(self):
        # Check if the computer has won by iterating through winning combinations
        for combination in self.winning_combinations:
            if all(self.board.cells[position] == self.computer.symbol for position in combination):
                return True
        return False

    def start(self):

        # Display the welcome message and initial game information
        print(self.message)
        print(f"You were randomly assigned '{self.user.symbol}'. Computer is '{self.computer.symbol}'.")

        # Determine who starts the game based on the user's symbol
        if self.user.symbol == "X":
            self.user.turn = True
            print("User starts first!")
        else:
            print("Computer starts first!")

        while self.game_is_on:
            if self.board.choices_left > 0:
                # Display the current state of the board
                self.board.print_board()
                if self.user.turn:
                    while True:
                        # Prompt the user for their move and validate it
                        human_choice = input(f"What's your move? ({self.user.symbol}): ").upper()
                        if self.board.is_valid_choice(choice=human_choice):
                            # Update the board with the user's move
                            self.board.update_board(position=human_choice, symbol=self.user.symbol)
                            self.possible_choices.remove(human_choice)
                            print(f"\nYou chose: '{human_choice}'")
                            if self.user_has_won():
                                # Check if the user has won and end the game
                                self.board.print_board()
                                print('You won!')
                                self.stop_game()
                                break
                            else:
                                try:
                                    # Let the computer make a move and update the board
                                    computer_choice = choice(self.possible_choices)
                                    self.possible_choices.remove(computer_choice)
                                    self.board.update_board(position=computer_choice, symbol=self.computer.symbol)
                                    print(f"Computer chose: '{computer_choice}'")
                                    if self.computer_has_won():
                                        # Check if the computer has won and end the game
                                        self.board.print_board()
                                        print('Computer won!')
                                        self.stop_game()
                                        break
                                    break
                                except IndexError:
                                    break
                        else:
                            print(f"'{human_choice}' is an invalid position. Please enter a valid position!")
                else:
                    # Let the computer make a move if the first turn is the computer's
                    computer_choice = choice(self.possible_choices)
                    self.possible_choices.remove(computer_choice)
                    self.board.update_board(position=computer_choice, symbol=self.computer.symbol)
                    print(f"Computer chose: '{computer_choice}'.")
                    self.user.turn = True
            else:
                # End the game if there are no more available moves
                self.stop_game()
                self.board.print_board()

        if self.board.is_full() and not self.user_has_won() and not self.computer_has_won():
            # If the board is full and no one has won, it's a tie
            print('Tie!')
