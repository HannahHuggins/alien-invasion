import pygame

class Orca():

    def __init__(self, ai_settings, screen):

        # Initialise the orca and set it's starting position
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the orca image and get it's rect
        self.image = pygame.image.load('images/try.bmp')


        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)
