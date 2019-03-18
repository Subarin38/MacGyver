from constantes import *
import random 


class Object: 
	def __init__(self, my_map):
		
		self.my_map = my_map
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		
		

	def randomize_position(self):
		while self.my_map[self.case_y][self.case_x] != "s":
			self.case_x = random.randint(0,14)
			self.case_y = random.randint(0,14)
		self.x = self.case_x * TAILLE_SPRITE
		self.y = self.case_y * TAILLE_SPRITE


		
		


	
			

			



			
			
		
