from pygame import mixer

class Settings:
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (255,255,255)

        # Ship settings
        self.ship_speed_factor = 10
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 50
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 0,255,255
        self.bullets_allowed = 100

        # Pika settings
        self.pika_speed_factor = 1
        self.fleet_drop_speed = 10
        # Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1




