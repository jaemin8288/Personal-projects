import random

BLACK = "○"
WHITE = "●"

MAX_INDEX = 19

def print_board(board_raw):
    for i in range(len(board_raw)):

        if i == 0:
            print("     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 ")
            print("   ┌───────────────────────────────────────┐")
            
        if i < 9:
            print("", i + 1 , "│", end='')

        if i >= 9:
            print(i+1, "│", end='')
                
        for j in range(len(board_raw[i])):
            if j < len(board_raw[i]) - 1:
                print(" " + board_raw[i][j], end='')
            else:
                print(" " + board_raw[i][j] + " ", end='')
               
        print("│", end='\n')

        if i == len(board_raw) - 1:
            print("   └───────────────────────────────────────┘")

def board():
    board_raw = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    for i in range(len(board_raw)):
        a=0
        board_raw[i] = ["+", "+", "+", "+", "+", "+", "+", "+","+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"]

    global num_pieces
    num_pieces = 0

  #  populate_board(board_raw)

    return board_raw
    
def get_move():
    location = 0
    
    while location < 1 or location > 19:
        location = int(input("Enter a integer between 1 and 19: "))
        
        if location >= 1 and location <= 19:
            print("valid choice.")

        else:
            print("invalid input. Write again.")

    return location

def do_move(piece, game_board):
    print("Please enter an x value for", piece)
    loc_x = get_move()

    print("Please enter a y value for", piece)
    loc_y = get_move()

    print(str(loc_x) + ", " + str(loc_y))

    game_board = change_piece(game_board, loc_y, loc_x, piece)

    return game_board

def change_piece(board, x, y, piece):
    if board[x-1][y-1] != "+":
        print("wrong piece location")
        board = do_move(piece, board)

    else:      
        board[x - 1][y - 1] = piece

    return board

def win_condition(board, piece):
    for i in range(len(board[0])):
        for j in range(len(board[0])):

            count = 0
            if board[i][j] == piece:
                count += 1

                if (i + 1) < len(board):
                    #move S
                    for b in range(1,5):
                        if (i+b) < len(board) and board[i + b][j] == piece:
                            count += 1
                        else:
                            count = 1

                    if count != 5 and (j + 1) < len(board):
                        #move SE
                        for b in range(1,5):
                            if count != 5 and (j+b) < len(board) and (i+b) < len(board) and board[i + b][j + b] == piece:
                                count += 1
                            else:
                                count = 1


                    if count != 5 and (j - 1) >= 0:
                        #move SW
                        for b in range(1,5):
                            if count != 5 and (j-b) >= 0 and (i+b) < len(board) and board[i + b][j - b] == piece:
                                count += 1
                            else:
                                count = 1

                if count != 5 and (i - 1) >= 0:
                    #N
                    for b in range(1,5):
                        if count != 5 and (i-b) >= 0 and board[i - b][j] == piece:
                            count += 1
                        else:
                            count = 1
                    if count !=5 and (j + 1) < len(board):
                       #NE
                       for b in range(1,5):
                           if count != 5 and (i-b) >= 0 and (j+b) < len(board) and board[i - b][j + b] == piece:
                               count += 1
                           else:
                               count = 1
         
                    if count !=5 and (j - 1) >= 0:
                       #NW
                       for b in range(1,5):
                           if count != 5 and (i-b) >= 0 and (j-b) >= 0 and board[i - b][j - b] == piece:
                               count += 1
                           else:
                               count = 1
                if count !=5 and (j + 1) < len(board):
                    #E
                    for b in range(1,5):
                        if count != 5 and (j+b) < len(board) and board[i][j + b] == piece:
                            count += 1
                        else:
                            count = 1

                if count !=5 and (j - 1) >= 0:
                    #W
                    for b in range(1,5):
                        if count != 5 and (j-b) >= 0 and board[i][j - b] == piece:
                            count += 1
                        else:
                            count = 1

            if count == 5:
                return True
    return False
 
#If the bounds are crossed, return false
def check_bounds(x, y):
    if x > MAX_INDEX or y > MAX_INDEX or x < 0 or y < 0:
        return False  #out of bounds.
    return True  #in bounds

#def computer_priority(board, piece):


def computer_do_move(board, piece, enemy):
    found = False
    
    entry_list = []
    entry_size = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != "+":
                found = True
            if board[i][j] == enemy:
                entry_list.append([i,j])
                entry_size += 1
                
    if found == False:
        computer_x = random.randrange(8, 13)
        computer_y = random.randrange(8, 13)
        board[computer_x][computer_y] = piece

    else:
        out_of_index = False
        count = 0

        for i in range(entry_size):
            k = entry_list[i][0]
            h = entry_list[i][1]

    for i in range(len(board[0])):
        for j in range(len(board[0])):

            count = 0
            if board[i][j] == piece:
                count += 1

                if (i + 1) < len(board):
                    #move S
                    for b in range(1,5):
                        if (i+b) < len(board) and board[i + b][j] == enemy:
                            count += 1
                            board[i + b][j] 

                        else:
                            count = 1

                    if count != 5 and (j + 1) < len(board):
                        #move SE
                        for b in range(1,5):
                            if count != 5 and (j+b) < len(board) and (i+b) < len(board) and board[i + b][j + b] == enemy:
                                count += 1
                                board[i + b][j + b]
                            else:
                                count = 1


                    if count != 5 and (j - 1) >= 0:
                        #move SW
                        for b in range(1,5):
                            if count != 5 and (j-b) >= 0 and (i+b) < len(board) and board[i + b][j - b] == enemy:
                                count += 1
                                board[i + b][j - b]
                            else:
                                count = 1

                if count != 5 and (i - 1) >= 0:
                    #N
                    for b in range(1,5):
                        if count != 5 and (i-b) >= 0 and board[i - b][j] == enemy:
                            count += 1
                            board[i - b][j]
                        else:
                            count = 1
                    if count !=5 and (j + 1) < len(board):
                       #NE
                       for b in range(1,5):
                           if count != 5 and (i-b) >= 0 and (j+b) < len(board) and board[i - b][j + b] == enemy:
                               count += 1
                               board[i - b][j + b]
                           else:
                               count = 1
         
                    if count !=5 and (j - 1) >= 0:
                       #NW
                       for b in range(1,5):
                           if count != 5 and (i-b) >= 0 and (j-b) >= 0 and board[i - b][j - b] == enemy:
                               count += 1
                               board[i - b][j - b]
                           else:
                               count = 1
                if count !=5 and (j + 1) < len(board):
                    #E
                    for b in range(1,5):
                        if count != 5 and (j+b) < len(board) and board[i][j + b] == enemy:
                            count += 1
                            board[i][j + b]
                        else:
                            count = 1

                if count !=5 and (j - 1) >= 0:
                    #W
                    for b in range(1,5):
                        if count != 5 and (j-b) >= 0 and board[i][j - b] == enemy:
                            count += 1
                            board[i][j - b]
                        else:
                            count = 1


            '''
            if board[k][h] == enemy:
                x = random.randrange(-1, 2)
                y = random.randrange(-1, 2)
                if board[i+x][j+y] == "+" and check_bounds(i+x, j+y):
                    board[i+x][j+y] = piece
                    return board

                while not out_of_index:
                    x = random.randrange(-1, 2)
                    y = random.randrange(-1, 2)
                    count += 1
                    if check_bounds(i+x, j+y):
                        if board[i+x][j+y] == "+":
                            board[i+x][j+y] = piece
                            return board

                    if count > 20:
                        out_of_index = True

            '''



def main():

    gameover_black = False
    gameover_white = False
    game_board = board()

    print("Let's play Omok!")
    print("  :Start Game:  ")
    print("")
   
    print_board(game_board)
    

    #while not gameover:
    while not gameover_black and not gameover_white:
        do_move(BLACK, game_board)
        gameover_black = win_condition(game_board, BLACK)
        print_board(game_board)

        #if not gameover_black:
        #    game_board = computer_do_move(game_board, WHITE, BLACK)
        #    gameover_white = win_condition(game_board, WHITE)
        #    print_board(game_board)

        if not gameover_black:
            do_move(WHITE, game_board)
            gameover_white = win_condition(game_board, WHITE)
            print_board(game_board)

    if gameover_black:
        print(BLACK, "wins!")
    
    elif gameover_white:
        print(WHITE, "wins!")

main() 