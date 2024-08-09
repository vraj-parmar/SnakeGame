import pygame
import time
from constants import black, red, window_x, window_y, white
from utils import show_text

def game_over(game_window, score):
    game_window.fill(black)
    show_text(game_window, f'Your Score is : {score}', red, 'times new roman', 50, (window_x / 2, window_y / 4))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

def pause_game():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False

def start_screen(game_window):
    start = False
    while not start:
        game_window.fill(black)
        show_text(game_window, 'Press Enter to Start', white, 'times new roman', 50, (window_x / 2, window_y / 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = True
