class settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initializes the game's static settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (0, 255, 255)

        #ship settings
        self.ship_speed = 2.5
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 3.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 8

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 8
        # Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # How quickly the game speeds up 
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # Scoring settings
        self.alien_speed = 3.0

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings""" 
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale 
