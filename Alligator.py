# Alligator class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 11/25/18

# Citation: Received image from 
# https://www.clipartmax.com/middle/m2i8K9i8Z5Z5b1A0_crocodile-clipart/

import pygame
import random
import math
from Animal import Animal


# Alligator Class with properties and methods specific for alligators

class Alligator(Animal):

# Constructor method that initializes Alligator image and position
    def __init__(self, x, y):
        super().__init__(x,y)
        self.image = pygame.image.load ('Alligator.png').convert_alpha()        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)
                    
       
    

# Method that re-stores the x and y coordinates and the width and height of 
# the image

    def getRect(self): 
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)
    

