import pygame

class Background:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the background image and get its rect.
        self.image = pygame.image.load("media/background_small.jpg")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        #self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        #self.x = float(self.rect.x)

    def update(self):
        """ Not sure if this is needed"""


    def blitme(self):
        """Draw the background at its current location."""
        self.screen.blit(self.image, self.rect)