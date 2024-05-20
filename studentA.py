def print_board(board):
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " | " + board[0][3] + " | " + board[0][4] + " ")
    print("---+---+---+---+---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " | " + board[1][3] + " | " + board[1][4] + " ")
    print("---+---+---+---+---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " | " + board[2][3] + " | " + board[2][4] + " ")
    print("---+---+---+---+---")
    print(" " + board[3][0] + " | " + board[3][1] + " | " + board[3][2] + " | " + board[3][3] + " | " + board[3][4] + " ")
    print("---+---+---+---+---")
    print(" " + board[4][0] + " | " + board[4][1] + " | " + board[4][2] + " | " + board[4][3] + " | " + board[4][4] + " ")
    
def new_board():
    return [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]]

def is_game_over(board):
    hcount = [0, 0, 0, 0, 0]
    vcount = [0, 0, 0, 0, 0]
    dcount = [0, 0]
    for x in range(len(board)):
        for y in range(len(board[x])):
            if(board[x][y] == "X"):
                hcount[x] += 1
                vcount[y] += 1
                if(x == y):
                    dcount[0] += 1
                if(x+y+1 == len(board)):
                    dcount[1] += 1
    for i in range(len(hcount)):
        if(hcount[i] == len(board)):
            return True
        if(vcount[i] == len(board)):
            return True
    for i in range(len(dcount)):
        if(dcount[i] == len(board)):
            return True
    
    ohcount = [0, 0, 0, 0, 0]
    ovcount = [0, 0, 0, 0, 0]
    odcount = [0, 0]
    for x in range(len(board)):
        for y in range(len(board[x])):
            if(board[x][y] == "O"):
                ohcount[x] += 1
                ovcount[y] += 1
                if(x == y):
                    odcount[0] += 1
                if(x+y+1 == len(board)):
                    odcount[1] += 1
    for i in range(len(hcount)):
        if(ohcount[i] == len(board)):
            return True
        if(ovcount[i] == len(board)):
            return True
    for i in range(len(dcount)):
        if(odcount[i] == len(board)):
            return True    
        
    return False

def announce_outcome(board, players_move):
    if(players_move):
        print("I kindly inform you user, that the game has concluded in positive outcome for you. (you won)")
    else:
        print("I kindly inform you sir user, that the game has concluded in negative outcome for you. (you lost)")

board = new_board()
print_board(board)
if(is_game_over(board)):
    print("Game Over")
    