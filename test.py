#!/usr/bin/python3
# -*- coding: Utf-8 -*

# fichier cherchant à contenir le labyrinthe du projet macgyver
# Créer les cellules du labyrinthe

import pygame
from random import *

from pygame.locals import *
from constantes import *
from My_labyrinthe import *
from macgyver import *
from Object import *


pygame.init()
	
pygame.display.set_caption("Jeu")
window = pygame.display.set_mode((COTE_WINDOW,COTE_WINDOW))

My_labyrinthe = labyrinthe()

continuer_jeu = 1
			
My_labyrinthe.creation()
##print (My_labyrinthe.my_map)	
## object.creation()

## créer 3 objets indépendants que j'appelle chacun à leur tour
mg = macgyver(My_labyrinthe.my_map)
obj1 = object(My_labyrinthe.my_map)
obj1.randomize_position()
obj2 = object(My_labyrinthe.my_map)
obj2.randomize_position()
while obj1.case_y == obj2.case_y and obj1.case_x == obj2.case_x:
	obj2.randomize_position()
obj3 = object(My_labyrinthe.my_map)
obj3.randomize_position()
while (obj1.case_y == obj3.case_y and obj1.case_x == obj3.case_x) or (obj2.case_y == obj3.case_y and obj2.case_x == obj3.case_x):
	obj3.randomize_position()

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

		#while My_labyrinthe.my_map[obj1.case_x][obj1.case_y] != "s" True :

		
		window.blit(OBJECT1, (obj1.x, obj1.y))				
		window.blit(OBJECT2,(obj2.x,obj2.y))
		window.blit(OBJECT3,(obj3.x,obj3.y))
		pygame.display.flip()	

	if My_labyrinthe.my_map[mg.case_x][mg.case_y] == "F":
		continuer_jeu = 0 




	

	