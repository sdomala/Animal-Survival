# Barn class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 11/28/18

# Citation: Got image from
# https://www.pinterest.com/pin/380343131003261591/?lp=true

import pygame
import random
import math


# Barn class with properties 

class Barn(pygame.sprite.Sprite):

# Constructor method that initializes monster image, location, and speed
    def __init__(self, x, y):
        super(Barn, self).__init__()
        self.x, self.y = x, y
        self.image = pygame.image.load ('Barn.png').convert_alpha()        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)
       
    

# Method that re-stores the x and y coordinates and the width and height of 
# the image

    def getRect(self): 
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)