import sys #Yet to figure out what exactly is SYS
import pygame

class AlienInvasion:
    """The class manages game assets and behavior."""

    def __init__(self):
        """Initialize the game, Create game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True: #infiniteloop
            #Tracks any kind of 'events' (Keyboard & Mouse)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Makes the most recently drawn screen visible 
            pygame.display.flip()

if __name__ == '__main__':
    #Makes a game instance and runs it -
    ai = AlienInvasion()
    ai.run_game()
