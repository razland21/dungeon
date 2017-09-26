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


draw_board(5)