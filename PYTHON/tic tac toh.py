def print_board(board):
    print("\n")   
    for row in range(3):
        print(" | ".join(board[row])) 
        if row != 2:
            print("----------")


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True 
          
    for col in board:
        if all(board[col] == player for row in range(3)):
            return True   
        
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False


def is_full(board):
    return all(cell in ['x', 'o'] for row in board for cell in row)
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "x"
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
        except ValueError:
            print("Invalid input. Use numbers 0, 1, or 2.")
            continue
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = current_player
            print_board(board)
            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            elif is_full(board):
                print("Game draw!")
                break
            current_player = "o" if current_player == "x" else "x"
        else:
            print("Invalid move. Try again.")
tic_tac_toe()
