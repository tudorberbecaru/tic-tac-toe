from board import Board
from player import Player
from random import choice


class Game:
    def __init__(self):
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
        random_symbol = choice(self.symbols)
        self.symbols.remove(random_symbol)
        remaining_symbol = self.symbols[0]
        self.user = Player(symbol=random_symbol)
        self.computer = Player(symbol=remaining_symbol)
        self.game_is_on = True
        self.board = Board()

    def stop_game(self):
        self.game_is_on = False

    def user_has_won(self):
        if (
                self.board.cells['TL'] == self.user.symbol and self.board.cells['TM'] == self.user.symbol and
                self.board.cells['TR'] == self.user.symbol or
                self.board.cells["ML"] == self.user.symbol and self.board.cells["MM"] == self.user.symbol and
                self.board.cells["MR"] == self.user.symbol or
                self.board.cells["BL"] == self.user.symbol and self.board.cells["BM"] == self.user.symbol and
                self.board.cells["BR"] == self.user.symbol or
                self.board.cells["TL"] == self.user.symbol and self.board.cells["ML"] == self.user.symbol and
                self.board.cells["BL"] == self.user.symbol or
                self.board.cells["TM"] == self.user.symbol and self.board.cells["MM"] == self.user.symbol and
                self.board.cells["BM"] == self.user.symbol or
                self.board.cells["TR"] == self.user.symbol and self.board.cells["MR"] == self.user.symbol and
                self.board.cells["BR"] == self.user.symbol or
                self.board.cells["TL"] == self.user.symbol and self.board.cells["MM"] == self.user.symbol and
                self.board.cells["BR"] == self.user.symbol or
                self.board.cells["BL"] == self.user.symbol and self.board.cells["MM"] == self.user.symbol and
                self.board.cells["TR"] == self.user.symbol):
            return True
        return False

    def computer_has_won(self):
        if (
                self.board.cells['TL'] == self.computer.symbol and self.board.cells['TM'] == self.computer.symbol and
                self.board.cells['TR'] == self.computer.symbol or
                self.board.cells["ML"] == self.computer.symbol and self.board.cells["MM"] == self.computer.symbol and
                self.board.cells["MR"] == self.computer.symbol or
                self.board.cells["BL"] == self.computer.symbol and self.board.cells["BM"] == self.computer.symbol and
                self.board.cells["BR"] == self.computer.symbol or
                self.board.cells["TL"] == self.computer.symbol and self.board.cells["ML"] == self.computer.symbol and
                self.board.cells["BL"] == self.computer.symbol or
                self.board.cells["TM"] == self.computer.symbol and self.board.cells["MM"] == self.computer.symbol and
                self.board.cells["BM"] == self.computer.symbol or
                self.board.cells["TR"] == self.computer.symbol and self.board.cells["MR"] == self.computer.symbol and
                self.board.cells["BR"] == self.computer.symbol or
                self.board.cells["TL"] == self.computer.symbol and self.board.cells["MM"] == self.computer.symbol and
                self.board.cells["BR"] == self.computer.symbol or
                self.board.cells["BL"] == self.computer.symbol and self.board.cells["MM"] == self.computer.symbol and
                self.board.cells["TR"] == self.computer.symbol):
            return True
        return False

    def start(self):
        print(self.message)
        print(f"You were randomly assigned '{self.user.symbol}'. Computer is '{self.computer.symbol}'.")
        possible_choices = list(self.board.cells.keys())

        if self.user.symbol == "X":
            self.user.turn = True
            print("User starts first!")
        else:
            print("Computer starts first!")

        while self.game_is_on:
            if self.board.choices_left > 0:
                self.board.print_board()
                if self.user.turn:
                    while True:
                        human_choice = input(f"What's your move? ({self.user.symbol}): ").upper()
                        if self.board.is_valid_choice(choice=human_choice):
                            self.board.update_board(position=human_choice, symbol=self.user.symbol)
                            possible_choices.remove(human_choice)
                            print(f"\nYou chose: '{human_choice}'")
                            if self.user_has_won():
                                self.board.print_board()
                                print('You won!')
                                self.stop_game()
                                break
                            else:
                                try:
                                    computer_choice = choice(possible_choices)
                                    possible_choices.remove(computer_choice)
                                    self.board.update_board(position=computer_choice, symbol=self.computer.symbol)
                                    print(f"Computer chose: '{computer_choice}'")
                                    if self.computer_has_won():
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
                    computer_choice = choice(possible_choices)
                    possible_choices.remove(computer_choice)
                    self.board.update_board(position=computer_choice, symbol=self.computer.symbol)
                    print(f"Computer chose: '{computer_choice}'.")
                    self.user.turn = True
            else:
                self.stop_game()
                self.board.print_board()

        if self.board.is_full() and not self.user_has_won() and not self.computer_has_won():
            print('Tie!')
