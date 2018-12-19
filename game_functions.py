import sys
import pygame
from bullet import Bullet
from pygame import mixer
from settings import Settings
from pika import Pika
from time import sleep

mixer.init()


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Respond to keypresses."""
    pygame.mixer.init()
    sound = mixer.Sound('sounds/laser.wav')
    dist = 1
    if event.key == pygame.K_RIGHT:
        ship.center += dist
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.center -= dist
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
            sound.play()
    elif event.key == pygame.K_q:
        sys.exit()



def check_keyup_events(event, ship):
    """ Respond to key releases. """
    dist = 1
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        ship.center -= dist
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        ship.center -= dist


def check_events(ai_settings, screen, stats, play_button, ship, pikas, bullets):
    """Respond to keypresses and mouse events."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, pikas, bullets,
                              mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, ship, pikas,
                      bullets, mouse_x, mouse_y):
    """Start a new game when player clicks Play game."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        if play_button.rect.collidepoint(mouse_x, mouse_y):
           # Reset the game stats
           stats.reset_stats()
           stats.game_active = True

        # Empty the list of pikas and bullets.
        pikas.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, pikas)
        ship.center_ship()





def update_screen(ai_settings, screen, ship, pika, pikas, bullets, stats,
                  play_button):
    """ Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop.
    background_image = pygame.image.load("images/space.png").convert()
    screen.fill(ai_settings.bg_color)
    screen.blit(background_image, [0, 0])
    ship.blitme()
    pika.blitme()
    pikas.draw(screen)

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()


def update_bullets(ai_settings, screen, ship, pikas, bullets):
    """ Update position of bullets and get rid of old bullets. """
    # Update bullet positions.

    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_pikas_collision(ai_settings, screen, ship, pikas, bullets)

def check_bullet_pikas_collision(ai_settings, screen, ship, pikas, bullets):
    """Respond to bullet-pika collisions."""
    # Remove any bullets and pikas that have collided.
    # Check for any bullets that have hit pikas.
    # If so, get rid of the bullet and the pika.
    collisions = pygame.sprite.groupcollide(bullets, pikas, True, True)

    if len(pikas) == 0:
        # Destroy exiting bullets and create new fleet.
        bullets.empty()
        create_fleet(ai_settings, screen, ship, pikas)

def create_fleet(ai_settings, screen, ship, pikas):
    """Create a full fleet of pikas"""
    # Create a pika and find the number of pikas in a row.
    # Spacing between each pika is equal to one pika width.
    pika = Pika(ai_settings, screen)
    number_pikas_x = get_number_pikas_x(ai_settings, pika.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  pika.rect.height)

    # Create the fleet of pikas.
    for row_number in range(number_rows):
        for pika_number in range(number_pikas_x):
            create_pika(ai_settings, screen, pikas, pika_number,
                        row_number)

def get_number_pikas_x(ai_settings, pika_width):
    """ Determine the number of pikas that fit in a row. """
    available_space_x = ai_settings.screen_width - 2 * pika_width
    number_pikas_x = int(available_space_x / (2 * pika_width))
    return number_pikas_x

def create_pika(ai_settings, screen, pikas, pika_number, row_number):
    """ Create a pika and place it in the row."""
    pika = Pika(ai_settings, screen)
    pika_width = pika.rect.width
    pika.x = pika_width + 1.5 * pika_width * pika_number
    pika.rect.x = pika.x
    pika.rect.y = pika.rect.height + 2 * pika.rect.height * row_number
    pikas.add(pika)


def get_number_rows(ai_settings, ship_height, pika_height):
    """ Determine the number of rows of pikas that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
                         (3 * pika_height) - ship_height)
    number_rows = int(available_space_y /(2 * pika_height))
    return number_rows


def check_fleet_edges(ai_settings, pikas):
    """Respond appropriately if any pikas have reached an edge."""
    for pika in pikas.sprites():
        if pika.check_edges():
            change_fleet_direction(ai_settings, pikas)
            break


def change_fleet_direction(ai_settings, pikas):
    """ Drop the entire fleet and change the fleet's direction."""
    for pika in pikas.sprites():
        pika.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, ship, pikas, bullets):
    """Respond to ships being hit by alien."""
    if stats.ships_left > 0:
       # Decrement ships left.
       stats.ships_left -= 1

       # Empty the list of pikas and bullets.
       pikas.empty()
       bullets.empty()

       # Create a new fleet and center the ship.
       create_fleet(ai_settings, screen, ship, pikas)
       ship.center_ship()

       # Pause.
       sleep(0.5)
    else:
        stats.game__active = False


def check_pikas_bottom(ai_settings, stats, screen, ship, pikas, bullets):
    """Check if any pikas have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for pika in pikas.sprites():
        if pika.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, pikas, bullets)
            break


def update_pikas(ai_settings, stats, screen, ship, pikas, bullets):
    """
    Check if the fleet is at an edge,
    and then update the positions of all pikas in the fleet.
    """
    check_fleet_edges(ai_settings, pikas)
    pikas.update()

    # Look for pika-ship collisions.
    if pygame.sprite.spritecollideany(ship, pikas):
        ship_hit(ai_settings, stats, screen, ship, pikas, bullets)
        print("Ship hit!")

    # Look for pikas hitting the bottom of the screen.
    check_pikas_bottom(ai_settings, stats, screen, ship, pikas, bullets)