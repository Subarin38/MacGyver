#!/usr/bin/python3
# -*- coding: Utf-8 -*

# fichier cherchant à contenir le labyrinthe du projet macgyver
# Créer les cellules du labyrinthe

import pygame


from pygame.locals import *
from constantes import *
from My_labyrinthe import *
from macgyver import *


pygame.init()
	
pygame.display.set_caption("Jeu")
window = pygame.display.set_mode((COTE_WINDOW,COTE_WINDOW))

My_labyrinthe = labyrinthe()

continuer_jeu = 1
			
My_labyrinthe.creation()
##print (My_labyrinthe.my_map)	
## object.creation()

mg = macgyver(My_labyrinthe.my_map)

while continuer_jeu:
	for event in pygame.event.get():
	
		if event.type == QUIT:
			continuer_jeu = 0
			continuer = 0
	
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				continuer_jeu = 0

			elif event.key == K_RIGHT:
				mg.move('right')
			elif event.key == K_LEFT:
				mg.move('left')
			elif event.key == K_UP:
				mg.move('up')
			elif event.key == K_DOWN:
				mg.move('down')
			

		My_labyrinthe.afficher(window)
		window.blit(MACGYVER, (mg.x, mg.y))
		pygame.display.flip()	

	if My_labyrinthe.my_map[mg.case_x][mg.case_y] == "F":
		continuer_jeu = 0 




	

	