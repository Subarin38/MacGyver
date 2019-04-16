import pygame


pygame.display.init()
pygame.display.set_mode()
""" Set the window parameters."""
NUMBER_SPRITE_SIDE = 15
NUMBER_SPRITE_HEIGHT = 16
SIZE_SPRITE = 32
SIDE_WINDOW = NUMBER_SPRITE_SIDE * SIZE_SPRITE
HEIGHT_WINDOW = NUMBER_SPRITE_HEIGHT * SIZE_SPRITE
"""Set the piictures paramaters."""
WALL = pygame.image.load("images/wall.png").convert()
FLOOR = pygame.image.load("images/sol.png").convert()
GUARDIAN = pygame.image.load("images/gardien.png").convert()
MACGYVER = pygame.image.load("images/macgyver.png").convert()
OBJECT1 = pygame.image.load("images/object1.png").convert()
OBJECT2 = pygame.image.load("images/object2.png").convert()
OBJECT3 = pygame.image.load("images/object3.png").convert()
WIN = pygame.image.load("images/WIN.png").convert()
LOST = pygame.image.load("images/Lost.png").convert()
HOME = pygame.image.load("images/home.png").convert()