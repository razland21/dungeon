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
board = []

def draw_board(size):
    for row in range(size):
        for col in range(size):
            board.append((col,row))
    
    print(board)

def get_locations():
    monster = None
    door = None
    player = None

    return monster, door, player



# MAIN LOOP

def start_game():
    print("game start")


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