import matplotlib.pyplot as plt
import numpy as np

class StateNode:
    def __init__(self):
        self.board = [0 for _ in range(9)]  # Initialize the board
    
    def draw_board(self):
        plt.figure(figsize=(5, 5))
        # Draw grid lines
        plt.plot([1, 1], [0, 3], 'k')
        plt.plot([2, 2], [0, 3], 'k')
        plt.plot([0, 3], [1, 1], 'k')
        plt.plot([0, 3], [2, 2], 'k')
        
        # Plot X and O in their positions
        for index, player in enumerate(self.board):
            marker = 'X' if player == -1 else 'O' if player == 1 else ''
            if marker:
                plt.text((index % 3) + 0.5, 2 - (index // 3) + 0.5, marker, fontsize=40, ha='center', va='center')
        
        plt.axis('off')
        plt.axis([0, 3, 0, 3])
        # plt.show()
        plt.draw() 
        
    # Other methods (isValidMove, getEmptyCells, is_game_over, isWin) remain unchanged
    def set_move(self, cell, player):
        # Set a move on the board if the cell is empty
        if self.isValidMove(cell):
            self.board[cell] = player
            return True
        return False

    def isValidMove(self, cell):
        # Check if a move is valid (i.e., if the cell is empty)
        return self.board[cell] == 0

    def getEmptyCells(self):
        # Get a list of all empty cells on the board
        return [i for i, x in enumerate(self.board) if x == 0]

    def is_game_over(self):
        # Check if the game is over (win or tie)
        return self.isWin(-1) or self.isWin(1) or len(self.getEmptyCells()) == 0

    def isWin(self, player):
        # Check if a player has won the game
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if all(self.board[pos] == player for pos in combo):
                return True
        return False