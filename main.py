#!/usr/bin/python3
# -*- coding: Utf-8 -*

# fichier cherchant à contenir le labyrinthe du projet macgyver

import pygame
from random import *
from pygame.locals import *
from constantes import *
from My_labyrinthe import *
from macgyver import *
from Object import *


pygame.init()
	
pygame.display.set_caption("Jeu")
window = pygame.display.set_mode((COTE_WINDOW,HAUTEUR_WINDOW))

My_labyrinthe = Labyrinthe()

continuer_jeu = 1
			
My_labyrinthe.creation()

mg = Macgyver(My_labyrinthe.my_map)
obj1 = Object(My_labyrinthe.my_map)
obj1.randomize_position()
obj2 = Object(My_labyrinthe.my_map)
obj2.randomize_position()
while obj1.case_y == obj2.case_y and obj1.case_x == obj2.case_x:
	obj2.randomize_position()

obj3 = Object(My_labyrinthe.my_map)
obj3.randomize_position()
while (obj1.case_y == obj3.case_y and obj1.case_x == obj3.case_x) or (obj2.case_y == obj3.case_y and obj2.case_x == obj3.case_x):
	obj3.randomize_position()

object_count = []

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


		if mg.case_x == obj1.case_x and mg.case_y == obj1.case_y:
			obj1.x = 0 
			obj1.y = 15 * TAILLE_SPRITE
			object_count.append("4")
	

		if mg.case_x == obj2.case_x and mg.case_y == obj2.case_y:
			obj2.x = 1 * TAILLE_SPRITE
			obj2.y = 15 * TAILLE_SPRITE
			object_count.append("8")
		
		if mg.case_x == obj3.case_x and mg.case_y == obj3.case_y:
			obj3.x = 2 * TAILLE_SPRITE
			obj3.y = 15 * TAILLE_SPRITE
			object_count.append ("9")


		My_labyrinthe.afficher(window)
		window.blit(MACGYVER, (mg.x, mg.y))
		window.blit(OBJECT1, (obj1.x, obj1.y))			
		window.blit(OBJECT2,(obj2.x,obj2.y)) 
		window.blit(OBJECT3,(obj3.x,obj3.y)) 
		pygame.display.flip()

		pass
		pygame.display.flip()

		

	if My_labyrinthe.my_map[mg.case_x][mg.case_y] == "F" and len(object_count) == 3:
		continuer_jeu = 0 
		print ("Bravo vous avez gagné")
	elif My_labyrinthe.my_map[mg.case_x][mg.case_y] == "F" and len(object_count) != 3:
		continuer_jeu = 0
		print ("Dommage c'est perdu !")




	

	