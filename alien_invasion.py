import pygame
import sys
from ship import Ship
from pika import Pika
from settings import Settings
import game_functions as gf
from pygame.sprite import Group
from pygame import mixer
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

mixer.init()
pika_sound = mixer.Sound('sounds/poketheme.wav')
pika_sound.play()


def run_game():
    # Initialize game, settings, and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((900, 525))
    pygame.display.set_caption("Meme invasion")

    # Make the play button.
    play_button = Button(ai_settings, screen, "Play Game")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    background_image = pygame.image.load("images/space.png").convert()

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a pika
    pika = Pika(ai_settings, screen)
    # Make a group to store bullets in
    bullets = Group()
    pikas = Group()

    gf.create_fleet(ai_settings, screen, ship, pikas)

    # Start the main loop for the game.
    while True:
        # screen.blit(background_image, [0, 0])

        gf.check_events(ai_settings, screen, stats, play_button, ship, pikas, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, pikas, bullets)
            gf.update_pikas(ai_settings, stats, screen, ship, pikas, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, pikas, bullets,
                         play_button, pika)

        # Redraw the screen during each pass through the loop

        # ship.blitme()
        pika.blitme()

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn screen visible.
        pygame.display.update()


run_game()
pika_sound.play()