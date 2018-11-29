# SmallCoin class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 11/25/18

# Citation: Got image from
# https://www.freeiconspng.com/img/3826

import pygame
import random
import math


# Coin class with properties and methods 

class SmallCoin(pygame.sprite.Sprite):

# Constructor method that initializes coin image, location
    def __init__(self, x, y):
        super(SmallCoin, self).__init__()
        self.x, self.y = x, y
        self.image = pygame.image.load ('Coin2.png').convert_alpha()        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)
       
    

# Method that re-stores the x and y coordinates and the width and height of 
# the image

    def getRect(self): 
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)