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
        #   0    1    2
board = [ [" ", " ", " "],  # 0
          [" ", " ", " "],  # 1
          [" ", " ", " "] ] # 2
          
def clear():
    board = [ [" ", " ", " "],  
              [" ", " ", " "],  
              [" ", " ", " "] ]

def vertical():
    if board[0][0] == board[1][0] and board[2][0] == board[1][0]:       #make sure all 3 are not empty, must be 3 o's or 3 1's
        return True
    elif board[0][1] == board[1][1] and board[2][1] == board[1][1]:
        return True
    elif board[0][2] == board[1][2] and board[2][2] == board[1][2]:
        return True
    else:
        return False
    
def horizontal():
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        return True
    elif board[1][0] == board[1][1] and board[1][2] == board[1][1]:
        return True
    elif board[2][0] == board[2][1] and board[2][2] == board[2][1]:
        return True
    else:
        return False
        
def diagonal():
    if board[0][2] == board[1][1] and board[2][0] == board[1][1]: #checks diagonal /
        return True
    elif board[0][0] == board[1][1] and board[2][2] == board[1][1]: #checks other diagonal \
        return True
    else:
        return False

def tictac(x,y,xo):
    if board[y][x] != " ":      #is the box empty
        print("Error space already filled!")
    elif y > 2 or x > 2:        #does the box exist?
        print("ERROR box does not exist!")
    else:
        board[y][x] = xo    #make the move!
    
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

    while(finished == False):
        board_print()
        x_input = int(input("Which Box? (x): "))
        y_input = int(input("Which Box? (y): "))
        move = input("X or O? ")
        tictac(x_input, y_input, move)
        #check if winner
        print(diagonal())
        if diagonal() == True:
            print("Winner! Diagonal Win :)")
            win = True
        elif horizontal() == True:
            print("Winner! Horizontal Win :)")
            win = True
        elif vertical() == True:
            print("Winner! Vertical Win :)")
            win = True
        
        if draw() == True or win == True:
            q = input("Would you like to play again? (Y/N): ")
            if q == "N":
                finished = True
            if q == "Y":
                clear()
                
        board_print()

play_game()
