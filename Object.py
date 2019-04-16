import random

from constantes import *


class Object:
    def __init__(self, my_map):
        """Set parameters for Object."""
        self.my_map = my_map
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0

    def randomize_position(self):
        """Generate a random position for objects."""
        while self.my_map[self.case_y][self.case_x] != "s":
            self.case_x = random.randint(0,14)
            self.case_y = random.randint(0,14)
        self.x = self.case_x * SIZE_SPRITE
        self.y = self.case_y * SIZE_SPRITE