### Creating a Pygame window and Responding to user input
import sys

import pygame

from ship import Ship

def run_game():
    # Initialize game, settings, and screen object
    pygame.init()  # Initilaizes background settings for Pygame to work
    screen = pygame.display.set_mode((1200, 800)) # the arguments (1200, 800) are dimension tuples
    pygame.display.set_caption("PETER'S INVASION GAME")

    # Set the background colour
    bg_colour = (150, 170, 230) # In pygame colours are RGB ranging from 0 to 255, (255, 0, 0) is red.

    # Make ship
    ship = Ship(screen)


    # Start the main loop for the game.
    while True:

        # Watch for keynoard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.Fill the screen with bg colour
        screen.fill(bg_colour)
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()  # Initializes the game and starts the main loop




