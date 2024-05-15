# # give me a complete code following the instructions below
# '''
# Create class StateNode with its proper members (getScoreValue(), isValidMove(),
# isGameOver(), drawboard(), getEmptyCells(), setMove(), isWin(), etc.)
# • Create class ticTacToe with its proper members (minimax(), computerMove(),
# playerMove(), start_game (), etc.)
# • Output should be according shown in Output image
# • Use only math, random, matplotlib libraries in python.
# '''

# import matplotlib.pyplot as plt
# import numpy as np
# import math
# import random

# class StateNode:
#     def __init__(self):
#         self.board = [' ' for _ in range(9)]
#         self.player = 'X'
#         self.computer = 'O'
        
#     def getScoreValue(self):
#         if self.isWin(self.computer):
#             return 1
#         elif self.isWin(self.player):
#             return -1
#         else:
#             return 0
        
#     def isValidMove(self, move):
#         return self.board[move] == ' '
    
#     def isGameOver(self):
#         return self.isWin(self.player) or self.isWin(self.computer) or ' ' not in self.board
    
#     def draw_board(self):
#         fig, ax = plt.subplots()
#         ax.set_axis_off()
#         ax.plot([0, 3], [1, 1], 'k-')
#         ax.plot([0, 3], [2, 2], 'k-')
#         ax.plot([1, 1], [0, 3], 'k-')
#         ax.plot([2, 2], [0, 3], 'k-')
#         plt.show()
    
#     def getEmptyCells(self):
#         return [i for i, cell in enumerate(self.board) if cell == ' ']
    
#     def setMove(self, move, player):
#         self.board[move] = player
    
#     def isWin(self, player):
#         win_states = [
#             [0, 1, 2],
#             [3, 4, 5],
#             [6, 7, 8],
#             [0, 3, 6],
#             [1, 4, 7],
#             [2, 5, 8],
#             [0, 4, 8],
#             [2, 4, 6]
#         ]
        
#         for win_state in win_states:
#             if all(self.board[i] == player for i in win_state):
#                 return True
#         return False

# class TicTacToe:
#     def __init__(self):
#         self.state = StateNode()
        
#     def minimax(self, player):
#         if self.state.isWin(self.state.computer):
#             return 1
#         elif self.state.isWin(self.state.player):
#             return -1
#         elif not self.state.getEmptyCells():
#             return 0
        
#         if player == self.state.computer:
#             best_score = -math.inf
#             for move in self.state.getEmptyCells():
#                 self.state.setMove(move, player)
#                 score = self.minimax(self.state.player)
#                 self.state.setMove(move, ' ')
#                 best_score = max(score, best_score)
#             return best_score
#         else:
#             best_score = math.inf
#             for move in self.state.getEmptyCells():
#                 self.state.setMove(move, player)
#                 score = self.minimax(self.state.computer)
#                 self.state.setMove(move, ' ')
#                 best_score = min(score, best_score)
#             return best_score
        
#     def computerMove(self):
#         best_score = -math.inf
#         best_move = None
#         for move in self.state.getEmptyCells():
#             self.state.setMove(move, self.state.computer)
#             score = self.minimax(self.state.player)
#             self.state.setMove(move, ' ')
#             if score > best_score:
#                 best_score = score
#                 best_move = move
#         self.state.setMove(best_move, self.state.computer)
        
#     def playerMove(self):
#         move = int(input("Enter your move (0-8): "))
#         self.state.setMove(move, self.state.player)
        
#     def start_game(self):
#         while not self.state.isGameOver():
#             self.computerMove()
#             self.state.draw_board()
#             if self.state.isGameOver():
#                 break
#             self.playerMove()
#             self.state.draw_board()
#         if self.state.isWin(self.state.computer):
#             print("Computer wins!")
#         elif self.state.isWin(self.state.player):
#             print("Player wins!")
#         else:
#             print("It's a tie!")

# tic_tac_toe = TicTacToe()
# tic_tac_toe.start_game()

class TicTacToe:
    def __init__(self):
        self.board = [[0, 0, 0] for _ in range(3)]
        self.player = -1
        self.computer = 1

    def draw_board(self):
        symbols = {0: ' ', -1: 'X', 1: 'O'}
        print('\n' + '\n'.join([' '.join([symbols[cell] for cell in row]) for row in self.board]))

    def isValidMove(self, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2:
            return False
        elif self.board[x][y] != 0:
            return False
        return True

    def setMove(self, x, y, player):
        if self.isValidMove(x, y):
            self.board[x][y] = player
            return True
        return False

    def playerMove(self):
        move = int(input("Use numpad (1..9): ")) - 1
        x, y = move // 3, move % 3
        while not self.setMove(x, y, self.player):
            print("Invalid move! Try again.")
            move = int(input("Use numpad (1..9): ")) - 1
            x, y = move // 3, move % 3

    def computerMove(self):
        pass
        # Implement computer move here

    def isWin(self, player):
        # Indent the body of the function
        win_state = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]],
        ]
        if [player, player, player] in win_state:
            return True
        return False

    def isGameOver(self):
        return self.isWin(self.player) or self.isWin(self.computer) or len(self.getEmptyCells()) == 0

    def getEmptyCells(self):
        cells = []
        for x, row in enumerate(self.board):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])
        return cells

    def start_game(self):
        while not self.isGameOver():
            self.playerMove()
            self.draw_board()
            if self.isGameOver():
                break
            self.computerMove()
            self.draw_board()
        if self.isWin(self.computer):
            print("Computer wins!")
        elif self.isWin(self.player):
            print("Player wins!")
        else:
            print("It's a tie!")

tic_tac_toe = TicTacToe()
tic_tac_toe.start_game()