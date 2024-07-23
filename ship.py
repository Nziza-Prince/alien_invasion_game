import pygame
from settings import Settings
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class for the ship"""
    
    def __init__(self, ai_game):
        """Initialization of the ship and its position"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = Settings()
        # Loading the image and getting its rect
        self.image = pygame.image.load('/home/nziza/Documents/code/python/projects/alienInvasiongame/images/ship.png')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed
            
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """Drawing the ship at its current location"""
        self.screen.blit(self.image, self.rect)
