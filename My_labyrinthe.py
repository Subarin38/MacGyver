import pygame

from constantes import *


class Labyrinth:
    def __init__(self):
        self.my_map = []

    def creation(self):
        """Create a double entry table based on the .txt file.""" 
        with open("Map1.txt") as generating_file:
            content = []
            for ligne in generating_file:
                ligne_map = []
                for element in ligne:
                    if element != '\n':
                        ligne_map.append(element)
                content.append(ligne_map)
            self.my_map = content

    def display_lab(self, window):
        """Use the double entry table to display each picture."""
        number_ligne = 0
        for ligne in self.my_map:
            number_case = 0
            for element in ligne:
                x = number_case * SIZE_SPRITE
                y = number_ligne * SIZE_SPRITE
                if element == "s":
                    window.blit(FLOOR, (x,y))
                elif element == "m":
                    window.blit(WALL, (x, y))
                elif element == "F":
                    window.blit(GUARDIAN, (x, y))
                elif element == "D":
                    window.blit(FLOOR, (x,y))

                number_case += 1
            number_ligne += 1
