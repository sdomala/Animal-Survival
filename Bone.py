# Weapon class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 11/25/18


import pygame
import random
import math
import Weapon from Weapon

# Animal class with properties and methods for domesticated and wild animals

class Weapon(pygame.sprite.Sprite):

# Constructor method that initializes monster image, location, and speed
    def __init__(self, x, y, xSpeed, ySpeed):
        super().__init__ (x, y, xSpeed, ySpeed)
        self.damage = 4