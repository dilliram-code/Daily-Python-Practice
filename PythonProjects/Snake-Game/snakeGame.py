# import required modules
import pygame
import time
import random

# initialise pygame
pygame.init()

# screen dimensions
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)

# setup window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# clock(controls fps)
clock = pygame.time.Clock()
SNAKE_SPPED = 12  # more is the number, more will be the speed
