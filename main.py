#First Project 31/03/2026

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


