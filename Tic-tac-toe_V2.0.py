import sys
def main():
# The main function
    board = create_grid()
    symbol_1, symbol_2 = sym()
    grid = printBoard(board)
    full = Checkstat(board, symbol_1, symbol_2) # The function that starts the game is also in here.

def create_grid():
# This function creates a blank playboard
    print("Here is the playboard: ")
    board = [[' ',' ', ' ', ' '],
             [' ','-', '-', '-'],
             [' ','-', '-', '-'],
             [' ','-', '-', '-']]        
    return board

def sym():
# This function reads Players names and assigns symbols to both the players
    Player_1, symbol_1 = input("Enter Player1 Name"),'X'
    Player_2, symbol_2 = input("Enter Player2 Name"),'O'
    print(Player_1, "your symbol is 'X'. ")
    print(Player_2, "your symbol is 'O'. ")
    input("Press enter to start the game")
    print("\n")
    return (symbol_1, symbol_2)



def startGamming(board, symbol_1, symbol_2, count):
# This function starts the game.

    # Decides the turn
    if count % 2 == 0:
        player = symbol_2
    elif count % 2 == 1:
        player = symbol_1
    print("Player "+ player + ", it is your turn. ")
    try:
        row,column = list(map(int, input("Enter Row & column seperated by space").split()))
        if not (isinstance(row, int) and isinstance(column, int)):
            raise ValueError('Number required')
    except ValueError:
        printBoard(board)
        sys.exit()

    # Check if players' selection is out of range
    while (row > 3 or row < 1) or (column > 3 or column < 1):
        outOfBoard(row, column)
        try:
            row,column = list(map(int, input("Enter Row & column seperated by space").split()))
            if not (isinstance(row, int) and isinstance(column, int)):
                raise ValueError('Number required')
        except ValueError:
            printBoard(board)
            sys.exit()


        # Check if the square is already filled
    while (board[row][column] == symbol_1)or (board[row][column] == symbol_2):
        filled = illegal(board, symbol_1, symbol_2, row, column)
        try:
            row,column = list(map(int, input("Enter Row & column seperated by space").split()))
            if not (isinstance(row, int) and isinstance(column, int)):
                raise ValueError('Number required')
        except ValueError:
            printBoard(board)
            sys.exit()

        
    # Locates player's symbol on the board
    if row == 'exit' or column =='exit':
        GameAbort()
    if player == symbol_1:
        board[row][column] = symbol_1
            
    else:
        board[row][column] = symbol_2
    
    return (board)

def Checkstat(board, symbol_1, symbol_2):
    count = 1
    winner = True
# This function check the status of the board
    while count < 10 and winner == True:
        gaming = startGamming(board, symbol_1, symbol_2, count)
        grid = printBoard(board)

        # Check if here is a winner
        winner = isWinner(board, symbol_1, symbol_2, count)

        if count == 9:
            print("The board is full. Game over.")
            if winner == True:
                print("There is a tie. ")
                
        count += 1
    if winner == False:
        print("Game over.")


def outOfBoard(row, column):
# This function tells the players that their selection is out of range
    print("***Invalid Move***. Pick any other")
    
    
def printBoard(board):
# This function prints the board
    rows = len(board)
    cols = len(board)
    for r in range(1,rows):
        print(board[r][1], " ", board[r][2], " ", board[r][3])
    return board


def isWinner(board, symbol_1, symbol_2, count):
# This function checks if any winner is winning
    winner = True
    # Check whether there is a win across the rows
    for row in range (1, 4):
        if (board[row][1] == board[row][2] == board[row][3] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")
   
        elif (board[row][1] == board[row][2] == board[row][3] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")
            
            
    # Check whether there is a win across columns
    for col in range (1, 4):
        if (board[1][col] == board[2][col] == board[3][col] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")
        elif (board[1][col] == board[2][col] == board[3][col] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")

    # Check whether there is a win across diagnoals
    if board[1][1] == board[2][2] == board[3][3] == symbol_1:
        winner = False 
        print("Player " + symbol_1 + ", you won!")

    elif board[1][1] == board[2][2] == board[3][3] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")

    elif board[1][3] == board[2][2] == board[3][1] == symbol_1:
        winner = False
        print("Player " + symbol_1 + ", you won!")

    elif board[1][3] == board[2][2] == board[3][1] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")

    return winner
    


def illegal(board, symbol_1, symbol_2, row, column):
    print("***Invalid Move*** . Pick any other")


# Calling Main Function
main()
