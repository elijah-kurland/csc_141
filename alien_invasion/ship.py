import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load("media/ship.gif")
        self.rect = self.image.get_rect()

        # Scale the ship image (for example, 50% of the original size)
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * 0.7), int(self.rect.height * 0.7)))

        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact h orizontal position.
        self.x = float(self.rect.x)

        # Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position bassed on the movement flags."""
        # Update the ship's x value, not the rect.
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.x += 1
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            #self.x -= 1
            self.x -= self.settings.ship_speed
            

        # Update rect object from self.x.
        self.x = max(0, min(self.screen_rect.width - self.rect.width, self.x))

        self.rect.x = int(self.x)


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)