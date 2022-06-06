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


def draw(window, text, column):
    window.fill(BLUE)
    for x in range(50, WIDTH, 100):
        for y in range(50, HEIGHT-100, 100):
            pygame.draw.circle(window, BLACK, [x, y], RADIUS, 0)
    pygame.draw.rect(window, BLACK, [10, 600, 680, 100], 0)

    WINDOW.blit(text, (20, 620))
    pygame.draw.circle(WINDOW, YELLOW, [column, 550], RADIUS, 0)


def main():
    run = True
    clock = pygame.time.Clock()
    position = (0, 0)
    mouse_position_text = TEXT.render("Start", True, BLUE)
    column = -50

    column_1 = []
    column_2 = []
    column_3 = []
    column_4 = []
    column_5 = []
    column_6 = []
    column_7 = []

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                mouse_x = position[0]
                mouse_y = position[1]
                column = (int(ceil(mouse_x / 100)) * 100) - 50
                if mouse_x > 0 and mouse_y < 600:
                    if column == 50:
                        column_1.append("yellow")
                        mouse_position_text = TEXT.render(f"{position}, {column_1}", True, BLUE)
                    if column == 150:
                        column_2.append("yellow")
                        mouse_position_text = TEXT.render(f"{position}, {column_2}", True, BLUE)
                    if column == 250:
                        column_3.append("yellow")
                        mouse_position_text = TEXT.render(f"{position}, {column_3}", True, BLUE)
                    if column == 350:
                        column_4.append("yellow")
                        mouse_position_text = TEXT.render(f"{position}, {column_4}", True, BLUE)
                    if column == 450:
                        column_5.append("yellow")
                        mouse_position_text = TEXT.render(f"{position}, {column_5}", True, BLUE)
                    if column == 550:
                        column_6.append("yellow")
                        mouse_position_text = TEXT.render(f"{position}, {column_6}", True, BLUE)
                    if column == 650:
                        column_7.append("yellow")
                        mouse_position_text = TEXT.render(f"{position}, {column_7}", True, BLUE)

        draw(WINDOW, mouse_position_text, column)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
