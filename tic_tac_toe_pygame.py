import pygame
import sys

pygame.init()

# הגדרות מסך
WIDTH, HEIGHT = 300, 350
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# צבעים
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# פונקציות מהקוד שלך (כמעט בלי שינוי)
def create_board():
    return [""] * 9

def check_winner(board, symbol):
    combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in combos:
        if all(board[i] == symbol for i in combo):
            return True
    return False

def check_tie(board):
    return all(cell != "" for cell in board)

def make_move(board, position, symbol):
    board[position] = symbol

# ציור
def draw_grid():
    WIN.fill(WHITE)
    for i in range(1, 3):
        pygame.draw.line(WIN, BLACK, (0, i*100), (300, i*100), 3)
        pygame.draw.line(WIN, BLACK, (i*100, 0), (i*100, 300), 3)

def draw_marks(board):
    font = pygame.font.SysFont(None, 80)
    for i in range(9):
        if board[i] != "":
            x = (i % 3) * 100 + 30
            y = (i // 3) * 100 + 10
            text = font.render(board[i], True, BLACK)
            WIN.blit(text, (x, y))

def draw_status(text):
    font = pygame.font.SysFont(None, 30)
    label = font.render(text, True, BLACK)
    WIN.blit(label, (10, 310))

# התחלה
board = create_board()
current_player = "X"
game_over = False

# ניקוד
x_score = 0
o_score = 0
ties = 0

# לולאת משחק
while True:
    draw_grid()
    draw_marks(board)

    if not game_over:
        draw_status(f"Turn: {current_player}")
    else:
        draw_status("Click to restart")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over:
                board = create_board()
                current_player = "X"
                game_over = False
            else:
                x, y = pygame.mouse.get_pos()
                if y < 300:
                    col = x // 100
                    row = y // 100
                    index = row * 3 + col

                    if board[index] == "":
                        make_move(board, index, current_player)

                        if check_winner(board, current_player):
                            if current_player == "X":
                                x_score += 1
                            else:
                                o_score += 1
                            print(f"{current_player} wins!")
                            game_over = True

                        elif check_tie(board):
                            ties += 1
                            print("It's a tie!")
                            game_over = True

                        else:
                            current_player = "O" if current_player == "X" else "X"

    pygame.display.update()
#עדין לא סיימתי יש לי בעיה עם ההתקנה