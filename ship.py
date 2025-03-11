import pygame

class Ship():

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() # Access the image surface's rect attribute
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom centre of the screen
        self.rect.centerx = self.screen_rect.centerx # x coordinate of the ship center equal with centerx of attribute of screen's rect
        self.rect.bottom = self.screen_rect.bottom # y coordinate of ship's bootom equal with screen rect;s bottom attribute

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

