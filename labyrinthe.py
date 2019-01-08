#!/usr/bin/python3
# -*- coding: Utf-8 -*

# fichier cherchant à contenir le labyrinthe du projet macgyver
# Créer les cellules du labyrinthe

import pygame

class Labyrinthe ():


	Labyrinthe = ["D", "s", "s", "s", "s", "m", "m", "m", "m", "m", "m", "s", "s", "s", "s",
                  "m", "m", "m", "m", "s", "m", "m", "m", "m", "m", "m", "s", "m", "m", "m", 
                  "m", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "m", "m", "m",
                  "m", "s", "m", "m", "m", "m", "m", "m", "m", "m", "m", "s", "m", "s", "m", 
                  "m", "s", "m", "m", "m", "m", "s", "m", "m", "m", "m", "s", "m", "s", "m", 
                  # à continuer c'est juste pour voir si c'est la bonne méthode + j'ai trop d'indentation il me semble

    Blocs = {"sol": "s", "mur": "m", "départ": "D", "fin": "f"}

    def __init__(self):
        pass

# Généraion de la list pour le labyrinthe avec les images
@property
def show_Labyrinthe(sefl):
    # mettre ici les variables pour les images correspondant aux items de la liste


