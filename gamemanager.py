def check_hit(board, location):
    """Check if a location hits a ship."""
    x = ord(location[0]) - 65
    y = int(location[1:]) - 0  # Adjusted for 0-based indexing
    if board[x][y] != ' o' and board[x][y] != ' .' and board[x][y] != " X" :
        return True, board[x][y]
    return False, None

def check_game(board, ships):
    """Check if the game is over (any ship sunk)."""
    for ship in ships:
        if ship['hits'] == ship['length']:
            return True
    return False

def shiploc(name, length):
    """Get and validate ship location input."""
    location = input(f"Enter {name} ship location ({length}): ").upper().strip()
    while len(location) != 4:
        print("Invalid entry")
        location = input(f"Enter {name} ship location ({length}): ").upper().strip()
    
    while not ((location[0] == location[2] and abs(int(location[1]) - int(location[3])) == length - 1) or
               (location[1] == location[3] and abs(ord(location[0]) - ord(location[2])) == length - 1)):
        print("Invalid entry")
        location = input(f"Enter {name} ship location ({length}): ").upper().strip()
    return location

def assign(board, location, symbol):
    """Assign ship to board if no overlap."""
    x1 = ord(location[0]) - 65
    y1 = int(location[1]) - 0  
    x2 = ord(location[2]) - 65
    y2 = int(location[3]) - 0  
    cords = []
    if x1 == x2:
        for j in range(min(y1, y2), max(y1, y2) + 1):
            cords.append((x1, j))
    else:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            cords.append((i, y1))
    for (i, j) in cords:
        if board[i][j] != ' o':
            print("Overlapping! Try again.")
            return False
    for (i, j) in cords:
        board[i][j] = symbol  
    return True

def place_ship(board, symbol, length, name, ships):
    """Place a ship on the board."""
    while True:
        loc = shiploc(name, length)
        if assign(board, loc, symbol):
            ships.append({'name': name, 'symbol': symbol, 'length': length, 'hits': 0})
            print("Placed successfully!")
            break
        else:
            print("Enter again ↻:")

def play_turn(board, ships, player_name, opponent_ships):
    """Handle a player's turn."""
    print(f"It is {player_name}'s turn")
    x = input("Enter location (e.g., A0): ").upper().strip()
    while not (ord(x[0]) >= 65 and ord(x[0]) <= 74 and 0 <= int(x[1:]) <= 9):
        x = input("Invalid. Enter location (e.g., A0): ").upper().strip()
    
    hit, ship_symbol = check_hit(board, x)
    if hit:
        print("You hit the ship!")
        board[ord(x[0]) - 65][int(x[1:])] = " X"  
        for s in opponent_ships:
            if s['symbol'] == ship_symbol.strip():  
                s['hits'] += 1
                if s['hits'] == s['length']:
                    print(f"{s['name']} has been sunk!")
                    print(f"{player_name} wins!")
                    return True  # Game over
    else:
        print("Missed!")
        board[ord(x[0]) - 65][int(x[1:]) - 0] = " ."  
    return False  # Game continues