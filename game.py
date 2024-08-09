import pygame
import random
from constants import black, green, white, window_x, window_y, snake_speed
from screens import game_over, pause_game, start_screen
from utils import show_score

def main_game():
    """
    The main function to run the Snake game.
    It handles game initialization, the game loop, event handling,
    snake movement, fruit spawning, collision detection, and scoring.
    """
    # Initial direction of the snake
    direction = 'RIGHT'
    change_to = direction

    # Initial position of the snake's head
    snake_position = [100, 50]

    # Initial positions of the snake's body (head + initial length)
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

    # Random initial position of the fruit
    fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                      random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True

    # Initial score
    score = 0

    # Setting up the game window with specified dimensions
    game_window = pygame.display.set_mode((window_x, window_y))
    pygame.display.set_caption('OG Snakes Game')  # Window title

    # Display the start screen before beginning the game
    start_screen(game_window)

    # Create a clock object to manage the frame rate
    fps = pygame.time.Clock()

    # Main game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Change direction based on key press, but prevent 180-degree turns
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                if event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'
                # Pause the game if 'P' is pressed
                if event.key == pygame.K_p:
                    pause_game()

        # Update direction only if it doesn't result in an opposite movement
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Move the snake in the updated direction
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Update the snake's body
        snake_body.insert(0, list(snake_position))
        # Check if the snake has eaten the fruit
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False  # Disable fruit spawn for the next loop
        else:
            # Remove the last part of the snake's body (moving forward)
            snake_body.pop()

        # Spawn a new fruit if the previous one was eaten
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10]
        fruit_spawn = True

        # Clear the game window and redraw everything
        game_window.fill(black)

        # Draw the snake
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        # Draw the fruit
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

        # Check for collisions with the window boundaries (Game Over)
        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over(game_window, score)
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over(game_window, score)

        # Check for collisions with the snake's own body (Game Over)
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over(game_window, score)

        # Display the current score
        show_score(game_window, score)

        # Update the display to show the latest changes
        pygame.display.update()

        # Control the game's frame rate
        fps.tick(snake_speed)
