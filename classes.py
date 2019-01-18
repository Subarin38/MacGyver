"""Classes part file"""

import pygame

from pygame import *
from constantes import *
from labyrinthe import *

class labyrinthe:
	def __init__(self):
		pass
		
	def creation(window, ARRAY, WALL, MACGYVER, GARDIEN, SOL)
	#méthode pour créer la fenêtre et afficher les premiers éléments
		with open("Map1", "r") as generating_file:
		#ouvrir le fochier map
			content = []
			#création de la liste
				for ligne in generating_file
					ligne_clear = ligne.rstrip("\n")
					#enlever les espaces et les trucs vides en fin de ligne
					content.append(ligne_clear)
					#ajout dans la liste de contenu
					
		numero_ligne = 0
		for element in content:
			numero_case = 0
			for sprite in element:
			x = numero_case * TAILLE_SPRITE
			y = numero_ligne * TAILLE_SPRITE
			if sprite == "m"
				window.blit(WALL, (x, y))
				ARRAY.append([x, y, "WALL"])
			elif sprite == "s"
				window.blit(SOL, (x, y))
				ARRAY.append([x, y), "SOL"])
			elif sprite == "F"
				window.blit(GARDIEN, (x, y))
				ARRAY.append([x, y), ("GARDIEN"])
			elif sprite == "G"
				window.blit(MACGYVER, (x, y))
				ARRAY.append([x, y), ("MACGYVER"])
			numero_case += 1
		numero_ligne += 1
		
	def affichage(BACKGROUND, window, ARRAY, WALL, MACGYVER, GARDIEN, SOL)
		window.blit(BACKGROUND, (0, 0))
		#penser à ajouter un fichier background aux images /!\ pas encore fait
		for elt in ARRAY:
            if "WALL" in elt:
                window.blit(WALL, (elt[0], elt[1]))
            elif "MACGYVER" in elt:
                window.blit(MACGYVER, (elt[0], elt[1]))
            elif "GARDIEN" in elt:
                window.blit(GARDIEN, (elt[0], elt[1]))
            elif "SOL" in elt:
                window.blit(SOL, (elt[0], elt[1]))
           # Il manque encore des images à rajouter pour les objets après
		    else:
                pass
		
		
		
if __name__ == "__main__":
	pass