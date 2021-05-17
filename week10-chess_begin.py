#Creating an Object Oriented game of chess in Python
#so far ... set up board with most pieces initialized and printing out

class square:                           #represents single square on chess board
    def __init__(self, piece, colour):
        self.piece = piece
        self.colour = colour

board = [[square(" ", " ") for i in range(9)] for j in range(9)]    #2-d list comprehension for chess board, allows us to us 1-8 instead of 0-7

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

#knight
board[1][3].piece = "N"
board[1][6].piece = "N"

#king & queen
board[1][4].piece = "Q"
board[1][5].piece = "K"

#print the board
for y in range(1,9):
    for x in range(1,9):
        print(board[y][x].colour,end="") #print colur and no space
        print(board[y][x].piece,end=" ") #print piece next to colour and space after
    print(" ")                           #prints newline
