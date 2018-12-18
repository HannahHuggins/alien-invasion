import pygame
from pygame.sprite import Sprite

class Pika(Sprite):

    def __init__(self, ai_settings, screen):

        # Initialise the pika and set it's starting position
        super(Pika, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the pika image and get it's rect
        self.image = pygame.image.load('images/try.bmp')
        self.rect = self.image.get_rect()

        # Start each new pika near the top left of the screen
        self.screen_rect = screen.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the exact position

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
