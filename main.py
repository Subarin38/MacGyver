import pygame

from random import *
from pygame.locals import *

from constantes import *
from My_labyrinthe import *
from macgyver import *
from Object import *


def init_items(my_map):
    """Generate multiple objects at different positions"""
    obj1 = Object(my_map)
    obj1.randomize_position()
    obj2 = Object(my_map)
    obj2.randomize_position()

    while obj1.case_y == obj2.case_y and obj1.case_x == obj2.case_x:
        obj2.randomize_position()
    obj3 = Object(my_map)
    obj3.randomize_position()
    while (obj1.case_y == obj3.case_y and obj1.case_x == obj3.case_x) \
    or (obj2.case_y == obj3.case_y and obj2.case_x == obj3.case_x):
        obj3.randomize_position()
    return(obj1, obj2, obj3)


pygame.init()
pygame.display.set_caption("MacGyver Labyrinth")
window = pygame.display.set_mode((SIDE_WINDOW, HEIGHT_WINDOW))
window.blit(HOME, (0, 0))
play_game = 1

while play_game:
    """Main function."""
    pygame.display.flip()
    continue_game = 1
    continue_home = 1
    while continue_home:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continue_home = 0
                continue_game = 0
                play_game = 0
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    continue_home = 0
                    continue_game = 1
                    pygame.display.flip()
    My_labyrinth = Labyrinth()
    My_labyrinth.creation()
    obj1, obj2, obj3 = init_items(My_labyrinth.my_map)
    mg = Macgyver(My_labyrinth.my_map)
    object_count = 0

    while continue_game:
        for event in pygame.event.get():
            if event.type == QUIT:
                continue_game= 0
                play_game = 0
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continue_game = 0
                    play_game = 0
                elif event.key == K_RIGHT:
                    mg.move('right')
                elif event.key == K_LEFT:
                    mg.move('left')
                elif event.key == K_UP:
                    mg.move('up')
                elif event.key == K_DOWN:
                    mg.move('down')

            if mg.case_x == obj1.case_x and mg.case_y == obj1.case_y:
                obj1.case_x = 0
                obj1.case_y = 15
                object_count += 1
            if mg.case_x == obj2.case_x and mg.case_y == obj2.case_y:
                obj2.case_x = 1
                obj2.case_y = 15
                object_count += 1
            if mg.case_x == obj3.case_x and mg.case_y == obj3.case_y:
                obj3.case_x = 2
                obj3.case_y = 15
                object_count += 1

            My_labyrinth.display_lab(window)
            window.blit(MACGYVER, (mg.x, mg.y))
            window.blit(OBJECT1, (obj1.case_x * SIZE_SPRITE, obj1.case_y * SIZE_SPRITE))
            window.blit(OBJECT2, (obj2.case_x * SIZE_SPRITE, obj2.case_y * SIZE_SPRITE))
            window.blit(OBJECT3, (obj3.case_x * SIZE_SPRITE, obj3.case_y * SIZE_SPRITE))
            pygame.display.flip()

        if My_labyrinth.my_map[mg.case_x][mg.case_y] == "F" and object_count == 3:
            window.blit(WIN, (0, 0))
            pygame.display.flip()
            continue_game = 0
            continue_home = 1
        elif My_labyrinth.my_map[mg.case_x][mg.case_y] == "F" and object_count != 3:
            window.blit(LOST, (0, 0))
            continue_game = 0
            continue_home = 1





