# Bone class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 12/5/18

# Citation: Got image from
# https://techflourish.com/categories/dog-bone-clipart-transparent-background.html


import pygame
import random
import math
from Weapon import Weapon

# Bone subclass with methods and properties

class Bone(Weapon):

# Constructor method that initializes bone damage, position, and speed
    def __init__(self, x, y, xSpeed, ySpeed):
        super().__init__ (x, y, xSpeed, ySpeed)
        self.damage = 4