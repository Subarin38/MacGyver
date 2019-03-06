"""Constants part file"""
import pygame

pygame.display.init() 
pygame.display.set_mode()
#Window paramaters
NOMBRE_SPRITE_COTE = 15
NOMBRE_SPRITE_HAUTEUR = 16
TAILLE_SPRITE = 32
COTE_WINDOW = NOMBRE_SPRITE_COTE * TAILLE_SPRITE
HAUTEUR_WINDOW = NOMBRE_SPRITE_HAUTEUR * TAILLE_SPRITE
#Pictures paramaters
WALL = pygame.image.load("images/wall.png").convert()
SOL = pygame.image.load("images/sol.png").convert()
GARDIEN = pygame.image.load("images/gardien.png").convert()
MACGYVER = pygame.image.load("images/macgyver.png").convert()
OBJECT1 = pygame.image.load("images/object1.png").convert()
OBJECT2 = pygame.image.load("images/object2.png").convert()
OBJECT3 = pygame.image.load("images/object3.png").convert()
#OBJECT4 = pygame.image.load("images/object4.png").convert()




