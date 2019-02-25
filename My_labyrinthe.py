"""Classes part file"""

import pygame

from pygame import *
from constantes import *


class labyrinthe:
	def __init__(self):
		self.my_map = []

	def creation(self):
	#méthode pour créer la fenêtre et afficher les premiers éléments
		with open("Map1.txt", "r") as generating_file:
		#ouvrir le fichier map
			content = []
			#création de la liste
			for ligne in generating_file:
				ligne_map = []
				for element in ligne:
					if element != '\n':
						ligne_map.append(element)
				content.append(ligne_map)
			self.my_map = content
									

	
	def afficher(self, window):	
	#création de la fonction permettant d'afficher la fenêtre de jeu
		
			# chargement des images			
			numero_ligne = 0
			for ligne in self.my_map:
				numero_case = 0
				for element in ligne:
					x = numero_case * TAILLE_SPRITE
					#print (x)
					y = numero_ligne * TAILLE_SPRITE
					if element == "s":
						window.blit(SOL, (x,y))
										
					elif element == "m":
						window.blit(WALL, (x, y))

					elif element == "F":
						window.blit(GARDIEN, (x, y))

					numero_case += 1
				numero_ligne += 1

		##for ligne in self.my_map:
			##numero_case = 0
			##for element in ligne:
				##x = numero_case * TAILLE_SPRITE
				##y = numero_ligne * TAILLE_SPRITE
				##if element == "s":
					##for i in range(15): ## est ce que je peux mettre la constante NOMBRE_SPRITE_COTE ici
						##a = random.randint(0,15)
						##b = random.randint(0,15)
						##if "a" == "x" and "b" == "y":
							##window.blit(OBJECT1, (x, y))





			
