#!/usr/bin/python3
# -*- coding: Utf-8 -*

# fichier cherchant à contenir le labyrinthe du projet macgyver
# Créer les cellules du labyrinthe

import pygame


from pygame.locals import *
from constantes import *
from My_labyrinthe import *


pygame.init()
	
pygame.display.set_caption("Jeu")
window = pygame.display.set_mode((240, 180))

continuer = 1
while continuer:
	
	My_labyrinthe = labyrinthe()
	My_labyrinthe.creation()
	My_labyrinthe.afficher(self, window)