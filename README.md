# OG Snakes Game - README

Welcome to the OG Snakes Game! This project is a classic Snake game implemented in Python using the Pygame library. The game follows a modular design where different functionalities are split across multiple files to keep the code organised and maintainable.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Files Description](#files-description)
- [Game Controls](#game-controls)
- [How the Files Interact](#how-the-files-interact)
- [Acknowledgements](#acknowledgements)

## Overview

In this Snake game, you control a snake that moves around the screen, eating fruits to grow in length. The objective is to avoid colliding with the walls or the snake's own body. The game gets faster as your score increases, making it more challenging.

## Installation

1. **Clone the Repository**:
   ```
   git clone https://github.com/yourusername/og-snakes-game.git
   cd og-snakes-game
   ```

2. **Install Pygame**:
   Make sure you have Python installed. Then, install the Pygame library:
   ```
   pip install pygame
   ```

## How to Run

To start the game, simply run the `main_oop.py` file. This script serves as the entry point to the game:

```bash
python main_oop.py
```

## Files Description

- **`constants.py`**: Contains game constants like the screen dimensions, snake speed, and color definitions.
- **`game.py`**: Implements the core game logic, handling the main game loop, snake movement, collision detection, and scoring.
- **`main_oop.py`**: The entry point of the game, initialises Pygame and starts the game loop from `game.py`.
- **`screens.py`**: Manages different game screens, such as the start screen and game over screen.
- **`utils.py`**: Provides utility functions for rendering text and displaying the score.
- **`main.py`**: An alternative entry point for the game, featuring similar functionality to `main_oop.py`, but without the object-oriented approach.

## Game Controls

- **Arrow Keys**: Move the snake (Up, Down, Left, Right).
- **P**: Pause/Resume the game.
- **Enter**: Start the game from the start screen.

## How the Files Interact

- **`main_oop.py`**:
  - Acts as the starting point of the game. When you run this file, it initialises Pygame and then calls the `main_game` function from `game.py`.

- **`game.py`**:
  - Handles the core game logic, such as snake movement, fruit spawning, collision detection, and score calculation.
  - It imports constants from `constants.py` for game settings and colour schemes.
  - Utilises the `screens.py` functions to display the start screen and the game over screen.
  - Calls `show_score` from `utils.py` to display the score on the screen.

- **`screens.py`**:
  - Manages the game's user interface screens.
  - The `start_screen` function waits for the user to start the game, and the `game_over` function displays the final score and ends the game.

- **`utils.py`**:
  - Contains utility functions like `show_text` for rendering text on the screen and `show_score` for displaying the player's score during the game.

- **`constants.py`**:
  - Stores constant values such as screen dimensions, colours, and snake speed, which are used across other modules to ensure consistency.

## Acknowledgements

This project is a learning exercise in Python and Pygame, inspired by the classic Snake game. Special thanks to the Pygame community and all contributors to open-source game development resources.

Enjoy the game! 🎮
