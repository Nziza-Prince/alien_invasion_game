import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent an alien in the fleet"""
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('/home/nziza/Documents/code/python/projects/alienInvasiongame/images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
        
    def update(self):
        """move the alien"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x
        
    def _check_edges(self):
        """Return true if alien at edge of screen"""
        screen_rect = self.screen.get_rect()
        
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        
    def update(self):
        self.rect.x += (self.settings.alien_speed * self.settings.fleet_direction)
        
        

        
        