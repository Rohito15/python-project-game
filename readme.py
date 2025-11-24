def display_readme():
    print("""
    Battleship Game Instructions:
    
    - This is a two-player Battleship game on a 10x10 grid (A-J rows, 0-9 columns).
    - Each player places 5 ships: Carrier (5), Battleship (4), Cruiser (3), Submarine (3), Destroyer (2).
    - Ship placement: Enter start and end coordinates (e.g., A1A5 for a horizontal 5-cell ship).
    - Ships cannot overlap.
    - Take turns guessing locations to hit opponent's ships.
    - 'X' = Hit, '.' = Miss.
    - Sink atleast one opponent's ships to win.
    
    Run 'python main.py' to start the game.
    """)

if __name__ == "__main__":
    display_readme()