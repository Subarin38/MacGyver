#!/usr/bin/python3
# -*- coding: Utf-8 -*

# fichier cherchant à contenir le labyrinthe du projet macgyver
# Créer les cellules du labyrinthe

import pygame
import labyrinthe.py

from pygame.locals import *
from constantes import *
from classes import *

pygame.init()


def main():

	pygame.init()
	
	window = pygame.display.set_mode((COTE_WINDOW, COTE_WINDOW)
	
	My_labyrinthe = labyrinthe()
	My_labyrinthe.creation()
	My_labyrinthe.afficher()
	
	
	

	#Pourquoi certains utilisent convert() et d'autres convert_alpha() ??
	
	ARRAY = []
	
