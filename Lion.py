# Lion class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 11/25/18

# Citation: Received image from 
# https://pt.wikipedia.org/wiki/Ficheiro:Cow_cartoon_04.svg

import pygame
import random
import math
from Animal import Animal


# Lion Class with properties and methods for Lions

class Lion(Animal):

# Constructor method that initializes lion image and position
    def __init__(self, x, y):
        super().__init__(x,y)
        self.image = pygame.image.load ('Lion.png').convert_alpha()        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)
                    
       
    

# Method that re-stores the x and y coordinates and the width and height of 
# the image

    def getRect(self): 
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)
    

