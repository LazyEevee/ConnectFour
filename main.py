import pygame
from math import ceil

pygame.init()

WIDTH, HEIGHT = 700, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four")

FPS = 60

BLACK = (0, 0, 0)  # background
BLUE = (0, 0, 255)  # board
YELLOW = (255, 255, 0)  # player 1 pieces
RED = (255, 0, 0)  # player 2 pieces

RADIUS = 40  # radius of player pieces and holes in board

TEXT = pygame.font.SysFont("arial", 50)

COLUMNS = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
ROWS = [550, 450, 350, 250, 150, 50]


def display_turns(player_one):
    """ blit to screen whose turn it is """
    if player_one:
        WINDOW.blit(TEXT.render("Player 1", True, YELLOW), (20, 620))
    else:
        WINDOW.blit(TEXT.render("Player 2", True, RED), (20, 620))


def draw(window):
    """ draw the game grid on screen """
    window.fill(BLUE)
    for x in range(50, WIDTH, 100):
        for y in range(50, HEIGHT - 100, 100):
            pygame.draw.circle(window, BLACK, [x, y], RADIUS, 0)
    pygame.draw.rect(window, BLACK, [10, 600, 680, 100], 0)


def place_yellow_counter(mouse_x, mouse_y, column):
    """ add YELLOW counters to COLUMNS lists """
    if mouse_x > 0 and mouse_y < 600:
        COLUMNS[column].append(YELLOW)


def place_red_counter(mouse_x, mouse_y, column):
    """ add RED counters to COLUMNS lists """
    if mouse_x > 0 and mouse_y < 600:
        COLUMNS[column].append(RED)


def draw_counter():
    """ draw counters into grid """
    for i in range(len(COLUMNS[1])):
        pygame.draw.circle(WINDOW, COLUMNS[1][i], [50, ROWS[i]], RADIUS, 0)
    for i in range(len(COLUMNS[2])):
        pygame.draw.circle(WINDOW, COLUMNS[2][i], [150, ROWS[i]], RADIUS, 0)
    for i in range(len(COLUMNS[3])):
        pygame.draw.circle(WINDOW, COLUMNS[3][i], [250, ROWS[i]], RADIUS, 0)
    for i in range(len(COLUMNS[4])):
        pygame.draw.circle(WINDOW, COLUMNS[4][i], [350, ROWS[i]], RADIUS, 0)
    for i in range(len(COLUMNS[5])):
        pygame.draw.circle(WINDOW, COLUMNS[5][i], [450, ROWS[i]], RADIUS, 0)
    for i in range(len(COLUMNS[6])):
        pygame.draw.circle(WINDOW, COLUMNS[6][i], [550, ROWS[i]], RADIUS, 0)
    for i in range(len(COLUMNS[7])):
        pygame.draw.circle(WINDOW, COLUMNS[7][i], [650, ROWS[i]], RADIUS, 0)


def check_win():
    # check for vertical win
    for i in range(1, 8):
        for j in range(0, 3):
            if len(COLUMNS[i]) >= j+4:
                if COLUMNS[i][j] == COLUMNS[i][j+1] == COLUMNS[i][j+2] == COLUMNS[i][j+3]:
                    return True
    # check for horizontal win
    for i in range(1, 5):
        for j in range(0, 6):
            if len(COLUMNS[i]) > j and len(COLUMNS[i+1]) > j and len(COLUMNS[i+2]) > j and len(COLUMNS[i+3]) > j:
                if COLUMNS[i][j] == COLUMNS[i+1][j] == COLUMNS[i+2][j] == COLUMNS[i+3][j]:
                    return True
    # check for diagonal up/right win
    for i in range(1, 5):
        for j in range(0, 3):
            if len(COLUMNS[i]) > j and len(COLUMNS[i+1]) > j+1 and len(COLUMNS[i+2]) > j+2 and len(COLUMNS[i+3]) > j+3:
                if COLUMNS[i][j] == COLUMNS[i+1][j+1] == COLUMNS[i+2][j+2] == COLUMNS[i+3][j+3]:
                    return True
    # check for diagonal up/left win
    for i in range(4, 8):
        for j in range(0, 3):
            if len(COLUMNS[i]) > j and len(COLUMNS[i-1]) > j+1 and len(COLUMNS[i-2]) > j+2 and len(COLUMNS[i-3]) > j+3:
                if COLUMNS[i][j] == COLUMNS[i-1][j+1] == COLUMNS[i-2][j+2] == COLUMNS[i-3][j+3]:
                    return True


def main():
    run = True
    clock = pygame.time.Clock()
    player_one = True
    message_text = ""

    while run:
        clock.tick(FPS)
        draw(WINDOW)
        display_turns(player_one)
        position = pygame.mouse.get_pos()
        mouse_x = position[0]
        mouse_y = position[1]
        column = (int(ceil(mouse_x / 100)))
        draw_counter()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONUP:
                if player_one:
                    if len(COLUMNS[column]) < 6:
                        place_yellow_counter(mouse_x, mouse_y, column)
                        player_one = False
                        message_text = ""
                    else:
                        message_text = "Invalid Move"
                else:
                    if len(COLUMNS[column]) < 6:
                        place_red_counter(mouse_x, mouse_y, column)
                        player_one = True
                        message_text = ""
                    else:
                        message_text = "Invalid Move"

        if check_win():
            if player_one:
                message_text = "Player 2 Wins!"
            else:
                message_text = "Player 1 Wins!"

        WINDOW.blit(TEXT.render(message_text, True, BLUE), (350, 620))
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
