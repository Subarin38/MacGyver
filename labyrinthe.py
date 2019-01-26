"""Classes part file"""

import pygame

from pygame import *
from constantes import *


class labyrinthe:
	def __init__(self):
		my_map = []
		
	def creation(lab, ARRAY, WALL, MACGYVER, GARDIEN, SOL):
	#méthode pour créer la fenêtre et afficher les premiers éléments
		with open("Map1", "r") as generating_file:
		#ouvrir le fichier map
			content = []
			#création de la liste
			for ligne in generating_file:
				#ligne_clear = ligne.rstrip("\n") -- a remodifier plus tard
				ligne_map = []
				for element in ligne:
					ligne_map.append(element)
				content.append(ligne_map)
		my_map = content
						
			
					
	def afficher(self, window):	
	#création de la fonction permettant d'afficher la fenêtre de jeu

		# chargement des images			
		numero_ligne = 0
		for ligne in my_map:
			numero_case = 0
			for element in ligne:
				x = numero_case * TAILLE_SPRITE
				y = numero_ligne * TAILLE_SPRITE
				if element == "m"
					window.blit(WALL, (x, y))

				elif element == "s"
					window.blit(SOL, (x, y))

				elif element == "F"
					window.blit(GARDIEN, (x, y))

				elif element == "D"
					window.blit(MACGYVER, (x, y))
				
				numero_case += 1
			numero_ligne += 1
			
