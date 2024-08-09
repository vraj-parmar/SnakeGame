import pygame
import time
from constants import black, red, window_x, window_y, white
from utils import show_text


def game_over(game_window, score):
    """
    Displays the game over screen with the player's score and then quits the game.

    Parameters:
    - game_window: The surface on which the game over screen will be displayed.
    - score: The player's final score to display.
    """
    # Fill the game window with a black background.
    game_window.fill(black)

    # Display the score in the center upper part of the screen.
    show_text(game_window, f'Your Score is : {score}', red, 'times new roman', 50, (window_x / 2, window_y / 4))

    # Update the entire display surface to reflect the score and background color.
    pygame.display.flip()

    # Pause for 2 seconds to let the player see their score.
    time.sleep(2)

    # De-initialize all pygame modules and close the window.
    pygame.quit()

    # Exit the program.
    quit()


def pause_game():
    """
    Pauses the game until the player presses the 'P' key to resume.
    """
    pause = True
    while pause:
        # Check for events (like key presses) in the event queue.
        for event in pygame.event.get():
            # If a key is pressed down.
            if event.type == pygame.KEYDOWN:
                # If the 'P' key is pressed, unpause the game.
                if event.key == pygame.K_p:
                    pause = False


def start_screen(game_window):
    """
    Displays the start screen until the player presses Enter to start the game.

    Parameters:
    - game_window: The surface on which the start screen will be displayed.
    """
    start = False
    while not start:
        # Fill the game window with a black background.
        game_window.fill(black)

        # Display the prompt to start the game in the center of the screen.
        show_text(game_window, 'Press Enter to Start', white, 'times new roman', 50, (window_x / 2, window_y / 2))

        # Update the display to show the start message.
        pygame.display.flip()

        # Check for events (like key presses) in the event queue.
        for event in pygame.event.get():
            # If a key is pressed down.
            if event.type == pygame.KEYDOWN:
                # If the Enter key is pressed, start the game by breaking out of the loop.
                if event.key == pygame.K_RETURN:
                    start = True
