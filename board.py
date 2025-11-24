def initialize_board():
    #10 * 10 board
    return [[' o'] * 10 for _ in range(10)]
def print_board(board):
    #printing board
    print("  ", end=" ")
    for i in range(0, 10):
        print(i, " ", end="")
    print()
    for i in range(10):
        print(chr(65 + i), end=" ")
        for j in range(10):
            print(board[i][j], end=" ")
        print()