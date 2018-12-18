import sys
import pygame
from bullet import Bullet
from pygame import mixer

mixer.init()
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Respond to keypresses."""
    pygame.mixer.init()
    sound = mixer.Sound('sounds/laser.wav')
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
            sound.play()


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet. """



def check_keyup_events(event, ship):
    """ Respond to key releases. """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, pika, bullets):
    """Respond to keypresses and mouse events."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, pika, bullets):
    """ Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop.
    background_image = pygame.image.load("images/space.png").convert()
    screen.fill(ai_settings.bg_color)
    screen.blit(background_image, [0, 0])
    ship.blitme()
    pika.blitme()

    # Make the most recently drawn screen visible.
    # pygame.display.flip()

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()


def update_bullets(bullets):
    """ Update position of bullets and get rid of old bullets. """
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
