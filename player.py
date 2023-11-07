# Define a class to represent a player in the Tic Tac Toe game.
class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.has_won = False
        self.turn = False
