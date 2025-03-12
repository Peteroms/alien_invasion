### Creating a Pygame window and Responding to user input

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game, settings, and screen object
    pygame.init()  # Initilaizes background settings for Pygame to work
    al_settings = Settings()
    screen = pygame.display.set_mode((al_settings.screen_width, al_settings.screen_height))
    pygame.display.set_caption("PETER'S INVASION GAME")

    # Make ship
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:
        gf.check_events()
        gf.update_screen(al_settings, screen, ship)

run_game()  # Initializes the game and starts the main loop




