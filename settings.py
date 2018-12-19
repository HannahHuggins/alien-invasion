class Settings:
    """A class to store all the settings for Meme Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
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

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 10
        self.bullet_speed_factor = 50
        self.pika_speed_factor = 1

        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.pika_points = 20

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.pika_speed_factor *= self.speedup_scale






