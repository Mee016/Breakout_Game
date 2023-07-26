import pygame, sys
import constants as c

# importing the game states
from states.menu import Menu
from states.gameplay import GamePlay
from states.game_over import GameOver
from states.splash import Splash
from states.credits import Credits
from game import Game

# khởi tạo pygame và thiết lập độ phân giải màn hình
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("Pygame Breakout")

# Game states
states = {
    "MENU": Menu(),
    "SPLASH": Splash(),
    "GAMEPLAY": GamePlay(),
    "GAMEOVER": GameOver(),
    "CREDITS": Credits(),
}

# Game class instance
game = Game(window, states, "SPLASH")
game.run()

# Closing the game
pygame.quit()
sys.exit()
