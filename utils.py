import pygame
from constants import window_x, window_y, white

def show_text(game_window, message, color, font, size, position):
    font = pygame.font.SysFont(font, size)
    surface = font.render(message, True, color)
    rect = surface.get_rect(center=position)
    game_window.blit(surface, rect)

def show_score(game_window, score):
    show_text(game_window, f'Score : {score}', white, 'times new roman', 20, (60, 20))
