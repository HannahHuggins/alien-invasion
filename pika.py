import pygame
from pygame.sprite import Sprite
from pygame import mixer
from random import randint

mixer.init()
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

    def __del__(self):
        pygame.mixer.init()
        pika_sound = mixer.Sound('sounds/Pikachu.wav')
        pika_sound_two = mixer.Sound('sounds/pikachutwo.wav')
        pika_sound.play()
        # pika_sound_two.play()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """ Move the pika right or left."""
        self.x += (self.ai_settings.pika_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x