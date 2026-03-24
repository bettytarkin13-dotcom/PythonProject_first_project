#First Project 31/03/2026

print("Welcome to Tic-Tac-Toe!")
print("player x vs player o")


def create_board():
    """
    Create a new Tic-Tac-Toe board.
    Returns a list ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    """
    board = [str(i) for i in range(1, 10)]
    return board

def print_board(board):
    """
    Print the board in a 3*3 grid format.
    Takes the board list as input and displays it on the screen.
    """
    print(f"""
    {board[0]} | {board[1]} | {board[2]} 
    ---+---+---
    {board[3]} | {board[4]} | {board[5]} 
    ---+---+---
    {board[6]} | {board[7]} | {board[8]} 
      """)

def get_move(player,board):
    """
    Ask the current player to make a move.
    Ensures the input is a number between 1 and 9 and spot is not already taken.
    Return the valid position chosen by the player (as an int).
    """
    while True:
        choice = input(f"player{player}:choose your move (1-9): ")
        if choice.isdigit():
            pos=int(choice)
            if 1 <= pos <= 9 and board[pos-1] not in ['x', 'o']:
                return pos
            else:
                print("spot already taken or the number is out of range")
        else:
            print("invalid input,please enter a number 1-9")

def make_move(board,position,symbol):
    """
    Updates the board list by placing the player's symbol ('x' or 'o')
    at the chosen position.
    """
    board[position-1]=symbol

def check_winner(board,symbol):
    """
    check if given symbol ('x' or 'o') has three in a row
    in any row,column or diagonal on the board.
    Return True if the player has won, False otherwise.
    """
    for row in [0, 3, 6]:
        if board[row] == board[row + 1] == board[row + 2] == symbol:
            return True


    for col in [0, 1, 2]:
        if board[col] == board[col + 3] == board[col + 6] == symbol:
            return True


    if board[0] == board[4] == board[8] == symbol:
        return True
    if board[2] == board[4] == board[6] == symbol:
        return True


    return False


def check_tie(board):
    """
    check if the board is full and there is no winner .
    Return True if it is a tie, False otherwise.
    """
    for cell in board:
        if cell.isdigit():
            return False
    return True

def play_game():
    """
    Main game loop for Tic-Tac-Toe.
    Create a new board,sets the starting player,
    and controls the game turns until there is a winner or a tie.
    """
    board = create_board()
    current_player = 'X'
    while True:
            print_board(board)

            move = get_move(current_player,board)
            make_move(board,move,current_player)

            if check_winner(board,current_player):
               print_board(board)
               print(f"🎉 Player {current_player} wins! 🎉")
               break

            if check_tie(board):
               print_board(board)
               print("🤝 It's a tie! Well played!")
               break

            if current_player == 'X':
               current_player = 'O'
            else:
                current_player = 'X'

while True:
    play_game()
    choice = input("Do you want to play again? (y/n):")
    if choice.lower() != 'y':
        break

x_score = 0
o_score = 0
ties=0

while True:
    result=play_game()
    if result == 'X':
        x_score += 1
    elif result == 'O':
        o_score += 1
    else:
        ties += 1

    print(f"score:x={x_score} , o={o_score} , ties={ties}")

    choice = input("Do you want to play again? (y/n):")
    if choice.lower() != 'y':
        break




