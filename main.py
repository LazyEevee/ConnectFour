import pygame
from math import ceil
pygame.init()

WIDTH, HEIGHT = 700, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four")

FPS = 60

BLACK = (0, 0, 0)  # background
BLUE = (0, 0, 255)  # board
RED = (255, 0, 0)  # player 1 pieces
YELLOW = (255, 255, 0)  # player 2 pieces

RADIUS = 40  # radius of player pieces and holes in board

TEXT = pygame.font.SysFont("arial", 50)

COLUMNS = {
    "column_1": [],
    "column_2": [],
    "column_3": [],
    "column_4": [],
    "column_5": [],
    "column_6": [],
    "column_7": [],
}


def display_turns(player_one):
    if player_one:
        WINDOW.blit(TEXT.render("Player 1", True, YELLOW), (20, 620))
    else:
        WINDOW.blit(TEXT.render("Player 2", True, RED), (20, 620))


def draw(window):
    window.fill(BLUE)
    for x in range(50, WIDTH, 100):
        for y in range(50, HEIGHT-100, 100):
            pygame.draw.circle(window, BLACK, [x, y], RADIUS, 0)
    pygame.draw.rect(window, BLACK, [10, 600, 680, 100], 0)


def place_yellow_counter(mouse_x, mouse_y, column):
    if mouse_x > 0 and mouse_y < 600 and len(COLUMNS["column_{0}".format(column)]) < 7:
        COLUMNS["column_{0}".format(column)].append(YELLOW)


def place_red_counter(mouse_x, mouse_y, column):
    if mouse_x > 0 and mouse_y < 600 and len(COLUMNS["column_{0}".format(column)]) < 7:
        COLUMNS["column_{0}".format(column)].append(RED)


def draw_counter(rows):
    for i in range(len(COLUMNS["column_1"])):
        pygame.draw.circle(WINDOW, COLUMNS["column_1"][i], [50, rows[i]], RADIUS, 0)
    for i in range(len(COLUMNS["column_2"])):
        pygame.draw.circle(WINDOW, COLUMNS["column_2"][i], [150, rows[i]], RADIUS, 0)
    for i in range(len(COLUMNS["column_3"])):
        pygame.draw.circle(WINDOW, COLUMNS["column_3"][i], [250, rows[i]], RADIUS, 0)
    for i in range(len(COLUMNS["column_4"])):
        pygame.draw.circle(WINDOW, COLUMNS["column_4"][i], [350, rows[i]], RADIUS, 0)
    for i in range(len(COLUMNS["column_5"])):
        pygame.draw.circle(WINDOW, COLUMNS["column_5"][i], [450, rows[i]], RADIUS, 0)
    for i in range(len(COLUMNS["column_6"])):
        pygame.draw.circle(WINDOW, COLUMNS["column_6"][i], [550, rows[i]], RADIUS, 0)
    for i in range(len(COLUMNS["column_7"])):
        pygame.draw.circle(WINDOW, COLUMNS["column_7"][i], [650, rows[i]], RADIUS, 0)


def main():
    run = True
    clock = pygame.time.Clock()
    player_one = True

    while run:
        clock.tick(FPS)
        draw(WINDOW)
        display_turns(player_one)
        position = pygame.mouse.get_pos()
        mouse_x = position[0]
        mouse_y = position[1]
        column = (int(ceil(mouse_x / 100)))
        rows = [550, 450, 350, 250, 150, 50]
        draw_counter(rows)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONUP:
                if player_one:
                    place_yellow_counter(mouse_x, mouse_y, column)
                    player_one = False
                else:
                    place_red_counter(mouse_x, mouse_y, column)
                    player_one = True

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
