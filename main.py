import pygame
import sys
from sudoku_generator import generate_sudoku
from board import Board

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREY = (200, 200, 200)
FONT = pygame.font.Font(None, 50)
SMALL_FONT = pygame.font.Font(None, 30)

def draw_text(screen, text, hor_start, hor_end, height, font, color=BLACK):
    text = font.render(text, True, color)
    pos = text.get_rect(center=((hor_end+hor_start)/2, height))
    screen.blit(text, pos)

def start_menu(screen):
    screen.fill(WHITE)
    draw_text(screen, "Welcome to Sudoku", 0, SCREEN_WIDTH, 100, FONT)
    draw_text(screen, "Select Game Mode:", 0, SCREEN_WIDTH, 350, FONT)
    pygame.draw.rect(screen, GREY, (25, 400, 150, 50))
    draw_text(screen, "Easy", 25, 175, 425, SMALL_FONT)
    pygame.draw.rect(screen, GREY, (225, 400, 150, 50))
    draw_text(screen, "Medium", 225, 375, 425, SMALL_FONT)
    pygame.draw.rect(screen, GREY, (425, 400, 150, 50))
    draw_text(screen, "Hard", 425, 575, 425, SMALL_FONT)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 400 <= y <= 450:
                    if 25 <= x <= 175:
                        return "easy"
                    elif 225 <= x <= 375:
                        return "medium"
                    elif 425 <= x <= 575:
                        return "hard"

def end_screen(screen, win):
    """Display the end screen based on game result."""
    screen.fill(WHITE)
    if win:
        draw_text(screen, "You Win!", (200, 300), FONT, BLUE)
    else:
        draw_text(screen, "Game Over", (200, 300), FONT, RED)
    pygame.display.flip()
    pygame.time.wait(3000)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sudoku Game")

    while True:
        difficulty = start_menu(screen)
        removed_cells = {"easy": 30, "medium": 40, "hard": 50}[difficulty]

        # Generate Sudoku board
        sudoku = generate_sudoku(9,removed_cells)

        board = Board(SCREEN_WIDTH, SCREEN_HEIGHT, screen, difficulty)

        while True:
            screen.fill(WHITE)
            board.draw()

            # Buttons
            pygame.draw.rect(screen, GREY, (50, 650, 150, 40))
            draw_text(screen, "Reset", (85, 660), SMALL_FONT)
            pygame.draw.rect(screen, GREY, (225, 650, 150, 40))
            draw_text(screen, "Restart", (250, 660), SMALL_FONT)
            pygame.draw.rect(screen, GREY, (400, 650, 150, 40))
            draw_text(screen, "Exit", (445, 660), SMALL_FONT)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 50 <= x <= 200 and 650 <= y <= 690:
                        board.reset_to_original()
                    elif 225 <= x <= 375 and 650 <= y <= 690:
                        break
                    elif 400 <= x <= 550 and 650 <= y <= 690:
                        pygame.quit()
                        sys.exit()

                    clicked = board.click(x, y)
                    if clicked:
                        board.select(*clicked)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if board.is_full():
                            if board.check_board():
                                end_screen(screen, True)
                            else:
                                end_screen(screen, False)
                            break
                    elif event.unicode.isdigit():
                        board.sketch(int(event.unicode))

if __name__ == "__main__":
    main()