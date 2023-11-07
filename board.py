# Define a class to represent the game board in Tic Tac Toe.
class Board:
    def __init__(self):

        # Initialize the game board with cells marked as '-' to represent empty positions.
        self.cells = {
            "TL": "-", "TM": "-", "TR": "-",
            "ML": "-", "MM": "-", "MR": "-",
            "BL": "-", "BM": "-", "BR": "-"
        }

        # Initialize the visual representation of the game board.
        self.shape = \
            f"""
 {self.cells["TL"]} | {self.cells["TM"]} | {self.cells["TR"]} 
---|---|---
 {self.cells["ML"]} | {self.cells["MM"]} | {self.cells["MR"]} 
---|---|---
 {self.cells["BL"]} | {self.cells["BM"]} | {self.cells["BR"]} 
            """

        # Initialize the number of available choices left on the board.
        self.choices_left = 9

    def print_board(self):
        print(self.shape)

    def update_board(self, position, symbol):

        # Update the game board by marking a cell with the player's symbol.
        self.cells[position] = symbol

        # Update the visual representation of the game board.
        self.shape = \
            f"""
 {self.cells["TL"]} | {self.cells["TM"]} | {self.cells["TR"]} 
---|---|---
 {self.cells["ML"]} | {self.cells["MM"]} | {self.cells["MR"]} 
---|---|---
 {self.cells["BL"]} | {self.cells["BM"]} | {self.cells["BR"]} 
            """

        # Decrease the count of available choices.
        self.choices_left -= 1

    def is_valid_choice(self, choice):
        # Check if a player's choice is a valid empty position on the board.
        return choice in self.cells and self.cells[choice] == "-"

    def is_full(self):
        # Check if the game board is completely filled, indicating a tie.
        return all(cell != "-" for cell in self.cells.values())
