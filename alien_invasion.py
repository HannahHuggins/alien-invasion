import sys
import pygame
from ship import Ship
from orca import Orca
from settings import Settings
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1200, 800)
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)
    # Make an orca
    orca = Orca(screen)

    # Set the background color.
    bg_color = (0,255,170)

    # Start the main loop for the game.
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship, orca)

        # Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)

        ship.blitme()
        orca.blitme()
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen.fill(bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()