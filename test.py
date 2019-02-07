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

continuer = 1
while continuer:
	
	window.blit(ACCUEIL, (0,0))
	pygame.display.flip()

	continuer_accueil = 1
	continuer_jeu = 1

	while continuer_accueil:	
		for event in pygame.event.get():
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_accueil = 0
				continuer_jeu = 0
				continuer = 0
				choix = 0
				
			elif event.type == KEYDOWN:				
				if event.key == K_F5:
					continuer_accueil = 0	
					choix = 'Map1.txt'		
	if choix != 0:		
		My_labyrinthe.creation()	
		My_labyrinthe.afficher(window)
		pygame.display.flip()
		mg = macgyver

	while continuer_jeu:
		for event in pygame.event.get():
		
			if event.type == QUIT:
				continuer_jeu = 0
				continuer = 0
		
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					continuer_jeu = 0

				elif event.key == K_RIGHT:
					mg.déplacements('droite')
				elif event.key == K_LEFT:
					mg.déplacements('gauche')
				elif event.key == K_UP:
					mg.déplacements('haut')
				elif event.key == K_DOWN:
					mg.déplacements('bas')	

		if My_labyrinthe.structure[mg.case_x][mg.case.y] == "F":
			continuer_jeu = 0 




	

	