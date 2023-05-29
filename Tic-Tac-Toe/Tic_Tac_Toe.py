import random

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i*3 + j], end=" ")
        print("|")
    print("---------")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        move = int(input("Enter your move (1-9): "))
        if move < 1 or move > 9 or board[move - 1] != " ":
            print("Invalid move. Try again.")
        else:
            board[move - 1] = "O"
            break

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in range(9):
        if board[i] == " ":
            free_fields.append(i + 1)
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if (board[0] == board[1] == board[2] == sign or
        board[3] == board[4] == board[5] == sign or
        board[6] == board[7] == board[8] == sign or
        board[0] == board[3] == board[6] == sign or
        board[1] == board[4] == board[7] == sign or
        board[2] == board[5] == board[8] == sign or
        board[0] == board[4] == board[8] == sign or
        board[2] == board[4] == board[6] == sign):
        return True
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    computer_move = random.choice(free_fields)
    board[computer_move - 1] = "X"

def tic_tac_toe():
    board = [" "] * 9
    board[4] = "X"  # Computer's first move
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, "O"):
            print("You win!")
            break
        if len(make_list_of_free_fields(board)) == 0:
            print("It's a tie!")
            break

        draw_move(board)
        display_board(board)
        if victory_for(board, "X"):
            print("Computer wins!")
            break
        if len(make_list_of_free_fields(board)) == 0:
            print("It's a tie!")
            break

tic_tac_toe()
