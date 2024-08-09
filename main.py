import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Constants
snake_speed = 15  # Speed of the snake (frames per second)
window_x = 720  # Width of the game window in pixels
window_y = 480  # Height of the game window in pixels

# Colors
black = pygame.Color(0, 0, 0)  # RGB color for black (background)
white = pygame.Color(255, 255, 255)  # RGB color for white (fruit, score text)
red = pygame.Color(255, 0, 0)  # RGB color for red (game over text)
green = pygame.Color(0, 255, 0)  # RGB color for green (snake body)

# Initialize game window
pygame.display.set_caption('OG Snakes Game')  # Set the window title
game_window = pygame.display.set_mode((window_x, window_y))  # Create the game window

# FPS (frames per second) controller
fps = pygame.time.Clock()  # Used to control the game's frame rate

# Game state
pause = False  # Indicates whether the game is paused
start = False  # Indicates whether the game has started


# Functions
def show_text(message, color, font, size, position):
    """
    Renders text on the game window.

    Parameters:
    - message: The text to display.
    - color: The color of the text.
    - font: The font type for the text.
    - size: The size of the font.
    - position: The center position (x, y) where the text should be displayed.
    """
    font = pygame.font.SysFont(font, size)  # Create a font object
    surface = font.render(message, True, color)  # Render the text onto a surface
    rect = surface.get_rect(center=position)  # Get the rectangle enclosing the text
    game_window.blit(surface, rect)  # Draw the text surface onto the game window


def show_score(score):
    """
    Displays the current score on the game window.

    Parameters:
    - score: The player's current score.
    """
    show_text(f'Score : {score}', white, 'times new roman', 20, (60, 20))  # Show the score at the top-left corner


def game_over(score):
    """
    Displays the game over screen with the final score and then quits the game.

    Parameters:
    - score: The final score to display.
    """
    game_window.fill(black)  # Fill the window with a black background
    show_text(f'Your Score is : {score}', red, 'times new roman', 50,
              (window_x / 2, window_y / 4))  # Show game over message
    pygame.display.flip()  # Update the display to show the game over message
    time.sleep(2)  # Wait for 2 seconds so the player can see the score
    pygame.quit()  # Quit Pygame
    quit()  # Exit the program


def pause_game():
    """
    Pauses the game until the player presses the 'P' key to resume.
    """
    global pause
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False  # Resume the game when 'P' is pressed


def start_screen():
    """
    Displays the start screen until the player presses Enter to start the game.
    """
    global start
    while not start:
        game_window.fill(black)  # Fill the window with a black background
        show_text('Press Enter to Start', white, 'times new roman', 50,
                  (window_x / 2, window_y / 2))  # Show start message
        pygame.display.flip()  # Update the display to show the start message
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = True  # Start the game when Enter is pressed


def main_game():
    """
    Main function to run the Snake game. Handles game initialization,
    game loop, event handling, snake movement, fruit spawning,
    collision detection, and scoring.
    """
    global direction, change_to, fruit_spawn, score, pause
    direction = 'RIGHT'  # Initial direction of the snake
    change_to = direction  # Direction to change to (initially the same as current direction)
    snake_position = [100, 50]  # Initial position of the snake's head
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]  # Initial positions of the snake's body
    fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                      random.randrange(1, (window_y // 10)) * 10]  # Initial position of the fruit
    fruit_spawn = True  # Whether the fruit needs to be spawned
    score = 0  # Initial score

    start_screen()  # Show the start screen before starting the game

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Change direction based on key presses, avoiding 180-degree turns
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
                    pause_game()  # Pause the game if 'P' is pressed

        # Update the direction only if it doesn't result in an opposite movement
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
            snake_body.pop()  # Remove the last part of the snake's body

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
            game_over(score)
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over(score)

        # Check for collisions with the snake's own body (Game Over)
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over(score)

        # Display the current score
        show_score(score)

        # Update the display to show the latest changes
        pygame.display.update()

        # Control the game's frame rate
        fps.tick(snake_speed)


# Entry point of the program
if __name__ == "__main__":
    main_game()
