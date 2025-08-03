## Tic tac Toe

def print_board(board):
    for row in board:
        print(" | ".join(row)) #join elements with verticals bars
        print("-" * 10) #print seperator after each row


#Function to check if the current play has won

def check_winner(board,player):

    #check row

    for row in board:
        if row == [player,player,player]:
            return True
        

    #check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
        
    #check diagnoals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False #if no winning condition met


#main game function

def play_game():
    #create a 3x3 empty board filed with spaces

    board = [[" " for _ in range(3)] for _ in range(3)]

    '''
    simple logic also can apply
    board = []

    for i in range(3):
        row = []
        for j in range(3):
            row.append(" ")
        board.append(row)

    
    # board is now [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    '''

    current_player = "X"

    for move in range(9): #Total 9 possible moves
        print_board(board)

        #ask player for row & column input

        row = int(input(f"{current_player}'s turn- Enter row(0,1,2):"))
        col = int(input(f"{current_player}'s turn - Enter column(0,1,2,):"))

        #check if cell is already taken

        if board[row][col] != " ":
            print("That cell is already filled. Try again")
            continue # skip this turn & ask again

        # place the player's symbol (X or 0) on the board
        board[row][col] = current_player

        #check if this player wins

        if check_winner(board,current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return
        

        #Switch Player for next turn
        current_player = "O" if current_player == "X" else "X"

    #if loop ends without a winner, its a draw
    print_board(board)
    print("its a draw")


play_game()

        
