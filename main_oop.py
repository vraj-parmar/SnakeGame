import pygame
from game import main_game

# This ensures that the following code runs only if this file is executed directly.
# If this file is imported as a module, the code below won't run.
if __name__ == "__main__":
    # Initializes all the modules in the pygame library.
    # This is necessary before using any other pygame functions.
    pygame.init()

    # Calls the main game loop or function from the 'game' module.
    # This function is expected to contain the core game logic.
    main_game()
