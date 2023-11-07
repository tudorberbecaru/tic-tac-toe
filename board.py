class Board:
    def __init__(self):
        self.cells = {
            "TL": "-", "TM": "-", "TR": "-",
            "ML": "-", "MM": "-", "MR": "-",
            "BL": "-", "BM": "-", "BR": "-"
        }
        self.shape = \
            f"""
 {self.cells["TL"]} | {self.cells["TM"]} | {self.cells["TR"]} 
---|---|---
 {self.cells["ML"]} | {self.cells["MM"]} | {self.cells["MR"]} 
---|---|---
 {self.cells["BL"]} | {self.cells["BM"]} | {self.cells["BR"]} 
            """
        self.choices_left = 9

    def print_board(self):
        print(self.shape)

    def update_board(self, position, symbol):
        self.cells[position] = symbol
        self.shape = \
            f"""
 {self.cells["TL"]} | {self.cells["TM"]} | {self.cells["TR"]} 
---|---|---
 {self.cells["ML"]} | {self.cells["MM"]} | {self.cells["MR"]} 
---|---|---
 {self.cells["BL"]} | {self.cells["BM"]} | {self.cells["BR"]} 
            """
        self.choices_left -= 1

    def is_valid_choice(self, choice):
        return choice in self.cells and self.cells[choice] == "-"

    def is_full(self):
        return all(cell != "-" for cell in self.cells.values())
