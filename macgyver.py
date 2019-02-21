"""Class macgyver // doit avoir sa propre position et gérer ses déplacements"""
from constantes import *



class macgyver:
	def __init__(self, my_map):
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		self.my_map = my_map

			
		

	def move(self, direction):
		if direction == "right":
			if self.my_map[self.case_y][self.case_x+1] != "m":
				self.case_x +=1
				self.x = self.case_x * TAILLE_SPRITE
		if direction == "left":
			if self.my_map[self.case_y][self.case_x-1] != "m":
				self.case_x -=1
				self.x = self.case_x * TAILLE_SPRITE
		if direction == "up":
			if self.my_map[self.case_y-1][self.case_x] != "m":
				self.case_y -= 1
				self.y = self.case_y * TAILLE_SPRITE
		if direction == "down":
			if self.my_map[self.case_y+1][self.case_x] != "m":
				self.case_y += 1
				self.y = self.case_y * TAILLE_SPRITE



