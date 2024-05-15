class StateNode:
    def __init__(self):
        # Initialize the board with 0 (empty), use -1 for player moves, +1 for "computer" moves
        self.board = [0 for _ in range(9)]
        self.board = [0 for _ in range(9)]
        self.player_symbol = -1  # Default player symbol
        self.computer_symbol = 1  # Default computer symbol

    # def draw_board(self):
    #     # Display the current state of the board
    #     symbols = {0: ' ', -1: 'X', +1: 'O'}
    #     for row in range(3):
    #         print('| ' + ' | '.join(symbols[self.board[row*3 + col]] for col in range(3)) + ' |')
    def draw_board(self):
        # Display the current state of the board with simplified line structure
        symbols = {0: '_', -1: 'X', +1: 'O'}
        for row in range(3):
            print('|'.join(symbols[self.board[row*3 + col]] for col in range(3)))

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
        # return self.isWin(-1) or self.isWin(1) or len(self.getEmptyCells()) == 0
        return self.isWin(self.player_symbol) or self.isWin(self.computer_symbol) or len(self.getEmptyCells()) == 0

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

# class TicTacToe:
#     def __init__(self):
#         self.state = StateNode()

#     def start_game(self):
#         # Main game loop
#         current_player = -1  # Human starts
#         while True:
#             self.state.draw_board()
#             if self.state.is_game_over():
#                 if self.state.isWin(-1):
#                     print("X wins!")  # Human wins
#                 elif self.state.isWin(1):
#                     print("O wins!")  # "Computer" wins
#                 else:
#                     print("It's a tie!")  # Tie
#                 break

#             if current_player == -1:
#                 self.player_move()  # Human's turn
#             else:
#                 self.manual_computer_move()  # "Computer's" turn, manually inputted
#             current_player *= -1  # Switch turns

#     def player_move(self):
#         # Handle player's move
#         move = int(input("Enter your move (1-9): ")) - 1
                    
#         if not self.state.set_move(move, -1):
#             print("Invalid move. Try again.")
#             self.player_move()

#     def manual_computer_move(self):
#         # Handle the "computer's" move, manually inputted
#         move = int(input("Enter computer's move (1-9): ")) - 1
#         if not self.state.set_move(move, 1):
#             print("Invalid move. Try again.")
#             self.manual_computer_move()

class TicTacToe:
    def __init__(self):
        self.state = StateNode()
        self.input_type = "manual"  # Default input type
        self.symbol_choice = "X"  # Default symbol choice

    def setup_game(self):
        # Let the user choose the symbol and input type
        self.symbol_choice = input("Choose your symbol [O/X]: ").upper()
        if self.symbol_choice not in ["O", "X"]:
            print("Invalid choice. Defaulting to X.")
            self.symbol_choice = "X"
        self.input_type = input("Choose input type [manual/auto]: ").lower()
        if self.input_type not in ["manual", "auto"]:
            print("Invalid choice. Defaulting to manual.")
            self.input_type = "manual"
        
        if self.symbol_choice == "O":
            self.state.player_symbol, self.state.computer_symbol = 1, -1
        else:
            self.state.player_symbol, self.state.computer_symbol = -1, 1

    def start_game(self):
        # Main game loop
        current_player = -1  # Human starts
        while True:
            self.state.draw_board()
            if self.state.is_game_over():
                if self.state.isWin(-1):
                    print("X wins!")  # Human wins
                elif self.state.isWin(1):
                    print("O wins!")  # "Computer" wins
                else:
                    print("It's a tie!")  # Tie
                break

            if current_player == -1:
                self.player_move()  # Human's turn
            else:
                self.manual_computer_move()  # "Computer's" turn, manually inputted
            current_player *= -1  # Switch turns

    def player_move(self):
        # Handle player's move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please enter a number between 1 and 9.")
                self.player_move()
            elif not self.state.set_move(move, -1):
                print("Invalid move. The cell is already occupied. Try again.")
                self.player_move()
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            self.player_move()

    def manual_computer_move(self):
        # Handle the "computer's" move, manually inputted
        try:
            move = int(input("Enter computer's move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please enter a number between 1 and 9.")
                self.manual_computer_move()
            elif not self.state.set_move(move, 1):
                print("Invalid move. The cell is already occupied. Try again.")
                self.manual_computer_move()
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            self.manual_computer_move()
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