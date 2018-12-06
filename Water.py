# Water class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 12/5/18

# Citation: Got image from
# http://www.transparentpng.com/cats/water-drop-1950.html


import pygame
import random
import math
from Weapon import Weapon

# Water subclass with methods and properties

class Water(Weapon):

# Constructor method that initializes water damage, position, and speed
    def __init__(self, x, y, xSpeed, ySpeed):
        super().__init__ (x, y, xSpeed, ySpeed)
        self.damage = 16
        self.image = pygame.image.load ('Water2.png').convert_alpha()        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)