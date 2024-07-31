class Settings:
    """A class to manage the settings"""
    
    def __init__(self):
        """initialising the game settings """
        #screen settings
        self.screen_width = 1200
        self.screen_length = 800
        self.bg_color = (230,230,230)
        self.bullet_width = 5
        self.bullet_length = 10
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 50
        self.fleet_drop_speed = 5
        self.ship_limit = 3
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        self.score_scale = 1.5
        
        
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1
        self.alien_speed = 1
        self.fleet_direction = 1
        self.alien_points = 50
        
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
        