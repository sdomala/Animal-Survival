# Horn class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 12/5/18

# Citation: Got image from 
# https://www.kisspng.com/png-horn-ram-trucks-goat-sheep-horn-711962/#


import pygame
import random
import math
from Weapon import Weapon

# Horn subclass with methods and properties

class Horn(Weapon):

# Constructor method that initializes horn damage, position, and speed
    def __init__(self, x, y, xSpeed, ySpeed):
        super().__init__ (x, y, xSpeed, ySpeed)
        self.damage = 8
        self.image = pygame.image.load ('Horn.png').convert_alpha()        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)