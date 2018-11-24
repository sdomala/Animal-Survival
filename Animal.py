# Animal class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 11/23/18

import pygame
import random
import math

# Animal class with properties and methods for domesticated and wild animals

class Animal(pygame.sprite.Sprite):

# Constructor method that initializes monster image, location, and speed
    def __init__(self, x, y):
        super(Animal, self).__init__()
        self.x, self.y = x, y
        self.image = pygame.image.load ('Dog2.png').convert_alpha()        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)

        
        
    

# Method that re-stores the x and y coordinates and the width and height of 
# the image

    def getRect(self): 
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)
    

