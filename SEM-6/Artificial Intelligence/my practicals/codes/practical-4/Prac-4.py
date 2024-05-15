# class StateNode:
#     def __init__(self):
#         self.board = [0 for _ in range(9)]  # Use 0 for empty, -1 for player, +1 for computer

#     def draw_board(self):
#         symbols = {0: ' ', -1: 'X', +1: 'O'}
#         for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
#             print('| ' + ' | '.join(symbols[x] for x in row) + ' |')

#     def set_move(self, cell, player):
#         if self.board[cell] == 0:
#             self.board[cell] = player
#             return True
#         return False

#     def is_game_over(self):
#         winning_combinations = [
#             [0, 1, 2], [3, 4, 5], [6, 7, 8],
#             [0, 3, 6], [1, 4, 7], [2, 5, 8],
#             [0, 4, 8], [2, 4, 6]
#         ]
#         for combo in winning_combinations:
#             if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != 0:
#                 return self.board[combo[0]]
#         if 0 not in self.board:
#             return 'Tie'
#         return None

# class TicTacToe:
#     def __init__(self):
#         self.state = StateNode()

#     def start_game(self):
#         current_player = -1  # Start with human player
#         while True:
#             self.state.draw_board()
#             game_over = self.state.is_game_over()
#             if game_over:
#                 if game_over == 'Tie':
#                     print("It's a tie!")
#                 else:
#                     winner = 'X' if game_over == -1 else 'O'
#                     print(f"{winner} wins!")
#                 break

#             if current_player == -1:
#                 move = int(input("Enter your move (1-9): ")) - 1
#             else:
#                 move = int(input("Enter computer move (1-9): ")) - 1  # For simulation, take input for the computer's move

#             if self.state.set_move(move, current_player):
#                 current_player *= -1  # Switch player
#             else:
#                 print("Invalid move. Try again.")

# game = TicTacToe()
# game.start_game()

class StateNode:
    def __init__(self):
        # Initialize the board with 0 (empty), use -1 for player moves, +1 for computer moves
        self.board = [0 for _ in range(9)]

    def draw_board(self):
        # Display the current state of the board
        symbols = {0: ' ', -1: 'X', +1: 'O'}
        for row in range(3):
            print('| ' + ' | '.join(symbols[self.board[row*3 + col]] for col in range(3)) + ' |')
    
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

    def getScoreValue(self, depth):
        # Assign a score to the end state
        if self.isWin(1):
            return 10 - depth  # Favor quicker wins
        elif self.isWin(-1):
            return depth - 10  # Favor slower losses
        else:
            return 0  # Tie or intermediate state

class TicTacToe:
    def __init__(self):
        self.state = StateNode()

    def start_game(self):
        # Main game loop
        current_player = -1  # Human starts
        while True:
            self.state.draw_board()
            if self.state.is_game_over():
                if self.state.isWin(-1):
                    print("X wins!")  # Human wins
                elif self.state.isWin(1):
                    print("O wins!")  # Computer wins
                else:
                    print("It's a tie!")  # Tie
                break

            if current_player == -1:
                self.player_move()  # Human's turn
            else:
                self.computer_move()  # Computer's turn
            current_player *= -1  # Switch turns

    def player_move(self):
        # Handle player's move
        move = int(input("Enter your move (1-9): ")) - 1
        if not self.state.set_move(move, -1):
            print("Invalid move. Try again.")
            self.player_move()

    def computer_move(self):
        # Computer decides the best move
        _, move = self.minimax(self.state,True,0)
        self.state.set_move(move, 1)
        print(f"Computer chose: {move + 1}")

    def minimax(self, isMaximizing, depth=0):
        # Minimax algorithm to choose the best move
        if self.state.is_game_over():
            return self.state.getScoreValue(depth), None

        bestScore = float('-inf') if isMaximizing else float('inf')
        bestMove = None
        for move in self.state.getEmptyCells():
            self.state.board[move] = 1 if isMaximizing else -1
            score, _ = self.minimax(not isMaximizing, depth + 1)
            self.state.board[move] = 0  # Reset the move

            if isMaximizing and score > bestScore or not isMaximizing and score < bestScore:
                bestScore, bestMove = score, move

        return bestScore, bestMove
    

game = TicTacToe()
game.start_game()
