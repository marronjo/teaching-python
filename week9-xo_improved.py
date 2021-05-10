#Tic Tac Toe

#To Do
#Fix Winning Check
#Distinguish between player 1 and 2

        #   0    1    2
board = [ [" ", " ", " "],  # 0
          [" ", " ", " "],  # 1
          [" ", " ", " "] ] # 2

def clear():
    board = [ [" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "] ]

def vertical():
    if board[0][0] == board[1][0] and board[2][0] == board[1][0] and board[0][0] != " ":       #make sure all 3 are not empty, must be 3 o's or 3 1's
        return True
    elif board[0][1] == board[1][1] and board[2][1] == board[1][1] and board[1][1] != " ":
        return True
    elif board[0][2] == board[1][2] and board[2][2] == board[1][2] and board[0][2] != " ":
        return True
    else:
        return False

def horizontal():
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != " ":
        return True
    elif board[1][0] == board[1][1] and board[1][2] == board[1][1] and board[1][0] != " ":
        return True
    elif board[2][0] == board[2][1] and board[2][2] == board[2][1] and board[2][0] != " ":
        return True
    else:
        return False

def diagonal():
    if board[0][2] == board[1][1] and board[2][0] == board[1][1] and board[0][2] != " ": #checks diagonal /
        return True
    elif board[0][0] == board[1][1] and board[2][2] == board[1][1] and board[0][0] != " ": #checks other diagonal \
        return True
    else:
        return False

def tictac(x,y,xo):
    if board[y][x] != " ":      #is the box empty
        print("Error space already filled!")
        return False
    elif y > 2 or x > 2:        #does the box exist?
        print("ERROR box does not exist!")
        return False
    else:
        board[y][x] = xo    #make the move!
        return True

def draw():
    for y in range(0,3):
        for x in range(0,3):
            if board[y][x] == " ":
                return False
    return True


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
    win = False
    player = 1

    board_print()

    while(finished == False):
        print("Player {}'s Turn".format(player))
        x_input = int(input("Which Box? (x): "))
        y_input = int(input("Which Box? (y): "))
        if player == 1:
            move = "x"
        else:
            move = "o"
        change = tictac(x_input, y_input, move)
        if change == True and player == 1:
            player = 2
        elif change == True and player == 2:
            player = 1
        #check if winner
        if diagonal() == True:
            print("Winner! Diagonal Win :)")
            win = True
        elif horizontal() == True:
            print("Winner! Horizontal Win :)")
            win = True
        elif vertical() == True:
            print("Winner! Vertical Win :)")
            win = True

        board_print()

        if draw() == True or win == True:
            q = input("Would you like to play again? (Y/N): ")
            if q == "N":
                finished = True
            if q == "Y":
                clear()

play_game()
