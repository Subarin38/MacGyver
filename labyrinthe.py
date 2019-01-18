#!/usr/bin/python3
# -*- coding: Utf-8 -*

# fichier cherchant à contenir le labyrinthe du projet macgyver
# Créer les cellules du labyrinthe

import pygame

from pygame.locals import *
from constantes import *
from classes import *

def main():

	pygame.init()
	
	window = pygame.display.set_mode((COTE_WINDOW, COTE_WINDOW)
	
	
	GARDIEN = pygame.image.load("images/Gardien.png").convert()
	MACGYVER = pygame.image.load("images/MacGyver.png").convert()
	SOL = pygame.image.load("images/sol.png").convert()
	WALL = pygame.image.load("images/wall.png").convert()
	#Pourquoi certains utilisent convert() et d'autres convert_alpha() ??
	
	ARRAY = []
	
