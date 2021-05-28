#Creating an Object Oriented game of chess in Python
#so far ... set up board with most pieces initialized and printing out

class square:                           #represents single square on chess board
    def __init__(self, piece, colour):
        self.piece = piece
        self.colour = colour
        
#2-d list comprehension for chess board, allows us to use 1-8 instead of 0-7
board = [[square(" ", " ") for i in range(9)] for j in range(9)]    

#colours
for y in range(1,3):
    for x in range(1,9):
        board[y][x].colour = "B"

for y in range(7,9):
    for x in range(1,9):
        board[y][x].colour = "W"

#pawn
for x in range(1,9):
    board[2][x].piece = "P"
    board[7][x].piece = "P"

#rook
board[1][1].piece = "R"
board[1][8].piece = "R"
board[8][1].piece = "R"
board[8][8].piece = "R"

#bishop
board[1][2].piece = "B"
board[1][7].piece = "B"
board[8][2].piece = "B"
board[8][7].piece = "B"

#knight
board[1][3].piece = "N"
board[1][6].piece = "N"
board[8][3].piece = "N"
board[8][6].piece = "N"

#king & queen
board[1][4].piece = "Q"
board[1][5].piece = "K"
board[8][4].piece = "Q"
board[8][5].piece = "K"

#print the board
def print_board():
    for y in range(1,9):
        for x in range(1,9):
            print(board[y][x].colour,end="") #print colur and no space
            print(board[y][x].piece,end="  ") #print piece next to colour and space after
        print(" ")                           #prints newline

def move(x1,y1,x2,y2):
    if x2 > 8 or y2 > 8 or x2 < 1 or y2 < 1:
        print("Out of Bounds, go again!")
    elif board[y1][x1].piece == " " or board[y1][x1].colour == " ":
        print("No piece there, try again!")
    else:
        board[y2][x2].piece = board[y1][x1].piece
        board[y2][x2].colour = board[y1][x1].colour
        board[y1][x1].piece = " "
        board[y1][x1].colour = " "

#test 
#print_board()
#move(1,1,3,3)
#print("\n")

print_board()

#we need a loop here to play the game and keep making moves ...
finished = False
while(finished == False):
    print("What piece would you like to move?")
    x1 = int(input("x: "))
    y1 = int(input("y: "))
    print("Where would you like to move it?")
    x2 = int(input("x: "))
    y2 = int(input("y: "))
    
    move(x1,y1,x2,y2)
    print_board()