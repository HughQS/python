class GameStats():
    """Track statistic for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistic."""
        self.ai_settings = ai_settings
        self.reset_stats()
        #Start Alien Invasion in an active state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
