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

        # Movement flag
        self.moving_right = False   # initially set it to false when initialising the moe rightattribute
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

