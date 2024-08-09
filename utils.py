import pygame
from constants import window_x, window_y, white


def show_text(game_window, message, color, font, size, position):
    """
    Displays a text message on the game window.

    Parameters:
    - game_window: The surface where the text will be displayed.
    - message: The text message to be displayed.
    - color: The color of the text.
    - font: The name of the font to be used.
    - size: The font size of the text.
    - position: A tuple (x, y) representing the center position of the text.
    """
    # Create a font object with the specified font and size.
    font = pygame.font.SysFont(font, size)

    # Render the text message onto a new surface with the specified color.
    surface = font.render(message, True, color)

    # Get the rectangle enclosing the text surface, centered at the given position.
    rect = surface.get_rect(center=position)

    # Blit (copy) the text surface onto the game window at the specified rectangle position.
    game_window.blit(surface, rect)


def show_score(game_window, score):
    """
    Displays the player's score in the top-left corner of the game window.

    Parameters:
    - game_window: The surface where the score will be displayed.
    - score: The player's current score to display.
    """
    # Call the show_text function to display the score in the top-left corner.
    # The text is set to be white, using the 'times new roman' font at size 20.
    show_text(game_window, f'Score : {score}', white, 'times new roman', 20, (60, 20))
