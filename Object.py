from constantes import *
import random 


class object: 
	def __init__(self, my_map):
		
		self.my_map = my_map
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0



	def randomize_position(self):
		self.case_x = random.randint(0,14)
		self.case_y = random.randint(0,14) 
		while self.my_map[self.case_y][self.case_x] != "s":
			self.case_x = random.randint(0,14)
			self.case_y = random.randint(0,14)
		self.x = self.case_x * TAILLE_SPRITE
		self.y = self.case_y * TAILLE_SPRITE


			#if self.my_map[self.case_x][self.case_y] == "s":
				#break
			#elif self.my_map[self.case_x][self.case_y] != "s":
				#x = random.randint(0,14)



		#while True :
			#self.my_map[self.case_x][self.case_y] == "s":
			#if x == x+1 and x+1 <= 14:
				#break
			

			
			
		
