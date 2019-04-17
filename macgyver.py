from constantes import *


class Macgyver:
    def __init__(self, my_map):
        """Set starting position for Macgyver."""
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.my_map = my_map
                    
    def move(self, direction):
        """Verify avalable position and change Macgyver position."""
        if direction == "right":
            if self.case_x < 14  and self.my_map[self.case_y][self.case_x+1] != "m" \
            and self.case_x+1 <= NUMBER_SPRITE_SIDE - 1:
                self.case_x +=1
                self.x = self.case_x * SIZE_SPRITE
        if direction == "left":
            if self.case_x >= 0 and self.my_map[self.case_y][self.case_x-1] != "m" \
            and self.case_x-1 >= 0:
                self.case_x -=1
                self.x = self.case_x * SIZE_SPRITE
        if direction == "up":
            if self.case_y >= 0 and self.my_map[self.case_y-1][self.case_x] != "m" \
            and self.case_y-1 >= 0:
                self.case_y -= 1
                self.y = self.case_y * SIZE_SPRITE
        if direction == "down":
            if self.case_y < 14 and self.my_map[self.case_y+1][self.case_x] != "m" \
            and self.case_y+1 <= NUMBER_SPRITE_SIDE - 1:
                self.case_y += 1
                self.y = self.case_y * SIZE_SPRITE
