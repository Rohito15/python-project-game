def initialize_board():
    """Initialize a 10x10 board with empty spaces."""
    return [[' o' for _ in range(10)] for _ in range(10)]

def print_board(board):
    """Print the board with row and column labels."""
    print("",end=" ")
    print("   " + "   ".join(str(i) for i in range(10)))  # Column headers 0-9
    for i in range(10):
        row_label = chr(65 + i)  # Row labels A-J
        print(f"{row_label}  " + " ".join(board[i]))