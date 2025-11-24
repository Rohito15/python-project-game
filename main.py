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
place_ship(board1, "🔵C", 5, "Carrier1", ships_P1)
print_board(board1)
place_ship(board1, "🔵B", 4, "Battleship1", ships_P1)
print_board(board1)
place_ship(board1, "🔵R", 3, "Cruiser1", ships_P1)
place_ship(board1, "🔵S", 3, "Submarine1", ships_P1)
place_ship(board1, "🔵D", 2, "Destroyer1", ships_P1)

# Player 2 ship placement
print("\nPlayer 2: Place your ships")
place_ship(board2, "🔴C", 5, "Carrier2", ships_P2)
place_ship(board2, "🔴B", 4, "Battleship2", ships_P2)
place_ship(board2, "🔴R", 3, "Cruiser2", ships_P2)
place_ship(board2, "🔴S", 3, "Submarine2", ships_P2)
place_ship(board2, "🔴D", 2, "Destroyer2", ships_P2)

# Game loop
while True:
    # Player 1's turn
    print_board(board1)
    game_over = play_turn(board2, "Player 1", ships_P2)
    if game_over:
        break
    
    # Player 2's turn
    print_board(board2)
    game_over = play_turn(board1, "Player 2", ships_P1)
    if game_over:
        break