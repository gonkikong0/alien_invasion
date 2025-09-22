import sys #Yet to figure out what exactly is SYS
import pygame
from settings import Settings

class AlienInvasion:
    """The class manages game assets and behavior."""

    def __init__(self):
        """Initialize the game, Create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        #Default Color : Black, setting up color -
        self.screen.fill(self.settings.bg_color)

    def run_game(self):
        """Start the main loop for the game."""
        while True: #infiniteloop
            #Tracks any kind of 'events' (Keyboard & Mouse)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)

            #Makes the most recently drawn screen visible (The changes to the screen, stay in a buffer --> with .display.flip() it presents the changes on the screen)
            pygame.display.flip()

if __name__ == '__main__': #Whenever a python file is executed directly the __name__ variable is __main__ !
    #Makes a game instance and runs it -
    ai = AlienInvasion()
    ai.run_game()

