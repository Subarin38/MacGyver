"""Class macgyver // doit avoir sa propre position et gérer ses déplacements"""
from constantes import *



class macgyver:
	def __init__(self, my_map):
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		self.my_map = my_map
		self.num_object = 0

			
		

	def move(self, direction):
		if direction == "right":
			if self.my_map[self.case_y][self.case_x+1] != "m" and self.case_x+1 <= NOMBRE_SPRITE_COTE - 1:
				self.case_x +=1 
				self.x = self.case_x * TAILLE_SPRITE
		if direction == "left":
			if self.my_map[self.case_y][self.case_x-1] != "m" and self.case_x-1 >= 0:
				self.case_x -=1
				self.x = self.case_x * TAILLE_SPRITE
		if direction == "up":
			if self.my_map[self.case_y-1][self.case_x] != "m" and self.case_y-1 >= 0:
				self.case_y -= 1
				self.y = self.case_y * TAILLE_SPRITE
		if direction == "down":
			if self.my_map[self.case_y+1][self.case_x] != "m" and self.case_y+1 <= NOMBRE_SPRITE_COTE - 1:
				self.case_y += 1
				self.y = self.case_y * TAILLE_SPRITE

	#def inventory(self):
		#for objects in self.my_map.object:
			#if (self.my_map.object[objects].case_x == self.case_x and self.my_map.object[objects].case_y == self.case_y and mon objet est affiché mais je sais pas comment faire (pour éviter le fait que je repasse au même endroit):
				#self.num_object += 1
				#ne plus afficher l'objet (show = false ???)



# ce que je suis censé faire et que je ne sais pas faire :
		# tout d'abord créer une méthode inventaire de ma classe macgyver qui me permet de stocker sous forme de liste mes obj1, obj2, obj3 
		# est-ce que je dois créer ça ici ou bien ma liste objects = [obj1, obj2, obj3] que je mets dans le test.py ne renvoie à rien d'intéressant pour moi
		# je dois vérifier quand la postion de macgyver = celle d'un de mes objets :
		# My_labyrinthe.my_map[mg.case_x][mg.case_y] == My_labyrinthe.my_map[obj1.case_x][obj1.case_y]:
		# ici deux possibilités :
		#1#  soit j'utilise while avec la fonction dessus en mettant != au milieu et je décide de blit window.blit(OBJECT1, (obj1.x, obj1.y))
		# je ne blit plus à partir du moment où mg passe sur cette case (est ce que je peux mettre un truc genre window.blit(OBJECT1, (obj1.x, obj1.y)) = False ???)
		#2# même chose au début sauf que la je rajoute cet objet dans une liste, je le blit à un autre endroit (j'ai vu qu'on pouvait utiliser des canvas
		# pour mettre des conditions)
		#et après j'utilise len(objects) si j'ai appelé ma liste objects pour vérifier qu'elle fait bien 3 avant de pouvoir finir le jeu

