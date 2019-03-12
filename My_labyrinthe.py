"""Classes part file"""

import pygame
from pygame import *
from constantes import *

class Labyrinthe:
	def __init__(self):
		self.my_map = []

	def creation(self):
	
		with open("Map1.txt", "r") as generating_file:
			content = []
			for ligne in generating_file:
				ligne_map = []
				for element in ligne:
					if element != '\n':
						ligne_map.append(element)
				content.append(ligne_map)
			self.my_map = content
					
	def afficher(self, window):	
					
			numero_ligne = 0
			for ligne in self.my_map:
				numero_case = 0
				for element in ligne:
					x = numero_case * TAILLE_SPRITE
					y = numero_ligne * TAILLE_SPRITE
					if element == "s":
						window.blit(SOL, (x,y))
					elif element == "m":
						window.blit(WALL, (x, y))
					elif element == "F":
						window.blit(GARDIEN, (x, y))
					elif element == "D":
						window.blit(SOL, (x,y))

					numero_case += 1
				numero_ligne += 1

		





			
