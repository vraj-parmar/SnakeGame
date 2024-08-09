import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Constants
snake_speed = 15
window_x = 720
window_y = 480

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Initialize game window
pygame.display.set_caption('OG Snakes Game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Game state
pause = False
start = False

# Functions
def show_text(message, color, font, size, position):
    font = pygame.font.SysFont(font, size)
    surface = font.render(message, True, color)
    rect = surface.get_rect(center=position)
    game_window.blit(surface, rect)

def show_score(score):
    show_text(f'Score : {score}', white, 'times new roman', 20, (60, 20))

def game_over(score):
    game_window.fill(black)
    show_text(f'Your Score is : {score}', red, 'times new roman', 50, (window_x / 2, window_y / 4))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

def pause_game():
    global pause
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False

def start_screen():
    global start
    while not start:
        game_window.fill(black)
        show_text('Press Enter to Start', white, 'times new roman', 50, (window_x / 2, window_y / 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = True

def main_game():
    global direction, change_to, fruit_spawn, score, pause
    direction = 'RIGHT'
    change_to = direction
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                      random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True
    score = 0

    start_screen()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                if event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'
                if event.key == pygame.K_p:
                    pause = True
                    pause_game()

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10]
        fruit_spawn = True

        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over(score)
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over(score)

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over(score)

        show_score(score)
        pygame.display.update()
        fps.tick(snake_speed)

if __name__ == "__main__":
    main_game()