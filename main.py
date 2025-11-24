from board import initialize_board, print_board
from gamemanager import place_ship, play_turn, check_game

# Initialize boards and ships
board1 = initialize_board()
board2 = initialize_board()
ships_P1 = []
ships_P2 = []

# Player 1 ship placement
print("Player 1: Place your ships")
print_board(board1)
place_ship(board1, "🔵", 5, "Carrier1", ships_P1)
place_ship(board1, "🔵", 4, "Battleship1", ships_P1)
place_ship(board1, "🔵", 3, "Cruiser1", ships_P1)
place_ship(board1, "🔵", 3, "Submarine1", ships_P1)
place_ship(board1, "🔵", 2, "Destroyer1", ships_P1)
print_board(board1)
# Player 2 ship placement
print("\nPlayer 2: Place your ships")
print_board(board2)
place_ship(board2, "🔴", 5, "Carrier2", ships_P2)
place_ship(board2, "🔴", 4, "Battleship2", ships_P2)
place_ship(board2, "🔴", 3, "Cruiser2", ships_P2)
place_ship(board2, "🔴", 3, "Submarine2", ships_P2)
place_ship(board2, "🔴", 2, "Destroyer2", ships_P2)
print_board(board2)

# Game loop
while True:
    # Player 1's turn
    ch1 = input("Press any key to display next board1 of player1")
    print_board(board1)
    game_over = play_turn(board2, ships_P2, "Player 1", ships_P2)
    if game_over:
        print("Player 1 Won!")
        break
    
    # Player 2's turn
    ch2 = input("Press any key to display next board2 of player2")
    print_board(board2)
    game_over = play_turn(board1, ships_P1, "Player 2", ships_P1)
    if game_over:
        print("Player 2 Won!")
        break