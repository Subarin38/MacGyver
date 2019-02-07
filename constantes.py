"""Constants part file"""
import pygame

pygame.display.init() 
pygame.display.set_mode()
#Paramètres de la fenêtre
NOMBRE_SPRITE_COTE = 15
TAILLE_SPRITE = 32
COTE_WINDOW = NOMBRE_SPRITE_COTE * TAILLE_SPRITE

WALL = pygame.image.load("images/wall.png").convert()
SOL = pygame.image.load("images/sol.png").convert()
GARDIEN = pygame.image.load("images/gardien.png").convert()
MACGYVER = pygame.image.load("images/macgyver.png").convert()


