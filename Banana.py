# Banana class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 11/26/18

# Citation: Got image from
#


import pygame
import random
import math
from Weapon import Weapon

# Water subclass with methods and properties

class Banana(Weapon):

# Constructor method that initializes water damage, position, and speed
    def __init__(self, x, y, xSpeed, ySpeed):
        super().__init__ (x, y, xSpeed, ySpeed)
        self.damage = 50
        self.image = pygame.image.load ('banana.png').convert_alpha()        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)