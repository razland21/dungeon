import random


#draw grid
#pick random location for player
#pick random location for exit door
#pick random location for monster
#draw player in grid
#take input for movement
#check if move valid (i.e. not off grid)
#move player if valid
#check win/loss
#redraw board

#variables
size = 5
board = []
monster = None
door = None
player = None


def draw_board(size):
    for row in range(size):
        for col in range(size):
            board.append((col,row))
    
    print(board)

def set_locations():
    global monster, door, player

    monster = random.choice(board)
    door = random.choice(board)
    player = random.choice(board)

    while door == monster:
        door = random.choice(board)

    while player == monster or player == door:
        player = random.choice(board)

    return monster, door, player

def get_locations():
    return monster, door, player


def check_move_input(move):
    moves = ["RIGHT", "LEFT", "UP", "DOWN"]

    if move not in moves:
        return False
    
    else:
        return True


def move_player(locs, move):
    global player
    player_loc = locs[2]

    #Right = col + 1
    #Left = col - 1
    #Up = row - 1
    #Down = row + 1

    if move == "RIGHT":
        player_loc = (player_loc[0], player_loc[1]+1)
    elif move == "LEFT":
        player_loc = (player_loc[0], player_loc[1]-1)
    elif move == "UP":
        player_loc = (player_loc[0]-1, player_loc[1])
    elif move == "DOWN":
        player_loc = (player_loc[0]+1, player_loc[1])
        

    #check valid move
    if player_loc in board:
        player = player_loc
        get_locations()
        print("Player has moved.")
    else:
        print("That is not a valid move.")


# MAIN LOOP

def start_game():
    #later - can let player set board size
    draw_board(size)

    set_locations()

    while True:
        locs = get_locations()
        print("You're currently in room {}.".format(locs[2]))
        print("Select a move: RIGHT, LEFT, UP, DOWN\n")

        move = input("Type move: ").upper()

        if not check_move_input(move):
            print("That is not a valid move input.\n")
            continue

        #check move / make move
        move_player(locs, move)
        #check win/lose

def main():
    print("\nWelcome to the Dungeon game! \n")

    while True:
        print("   Type 1 to play")
        print("   Type QUIT to quit\n")

        user = input("Enter option: ").upper()

        if user == "1":
            start_game()
        elif user == "QUIT":
            print("Thanks for playing!")
            break
        else:
            print("Sorry, I don't understand {}".format(user))


main()