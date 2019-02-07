"""Class macgyver // doit avoir sa propre position et gérer ses déplacements"""

import pygame
from pygame import *
from constantes import *

class macgyver:
	def __init__(self, droite, gauche, bas, haut):
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0

	def déplacements(self, direction):
		if direction == "droite":
			self.case_x +=1
			self.x = self.case_x * TAILLE_SPRITE
		if direction == "gauche":
			self.case_x -=1
			self.x = self.case_x * TAILLE_SPRITE
		if direction == "haut":
			self.case_y += 1
			self.y = self.case_y * TAILLE_SPRITE
		if direction == "bas":
			self.case_y -= 1
			self.y = self.case_y * TAILLE_SPRITE

