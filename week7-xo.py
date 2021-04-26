#First Attempt X and O's
#So Far:
#Input and make moves on the board
#checks if box exists and is empty
#prints a pretty board (kind of)

#To Do
#Check for winner and stop game
#Reset board?
#Distinguish between player 1 and 2
#if board is full either reset or stop game

board = [ ["x", " ", " "],
          [" ", "x", " "],
          [" ", " ", "x"] ]

def tictac(x,y,xo):
    if board[y][x] != " ":      #is the box empty
        print("Error space already filled!")
    elif y > 2 or x > 2:        #does the box exist?
        print("ERROR box does not exist!")
    else:
        board[y][x] = xo    #make the move!

def board_print():
    print("-------------")
    for y in range(0,3):
        print("|",end=" ")
        for x in range(0,3):
            print(board[y][x],end=" ")
            print("|",end=" ")
        print("\n-------------")

def play_game():
    finished = False

    while(finished == False):
        x_input = int(input("Which Box? (x): "))
        y_input = int(input("Which Box? (y): "))
        move = input("X or O? ")
        tictac(x_input, y_input, move)
        print(board)

#play_game()
board_print()
