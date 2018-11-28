# Lion class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 11/25/18

# Citation: Received image from 
# https://pt.kisspng.com/kisspng-wo9199/preview.html

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
        self.originalX = self.x 
        self.originalY = self.y 
        self.direction = "right"
        self.damage = 1
                    
       
    
    
    def update (self) :
        if self.direction == "right" :
            self.x += 3
            if self.x > (self.originalX + 72) : #72 is width of each block
                self.direction = "up" 
        
        elif self.direction == "up" :
            self.y -= 3
            if self.y < (self.originalY - 55) :
                self.direction = "left" 
        
        elif self.direction == "left" :
            self.x -= 3
            if self.x < (self.originalX - 72) :
                self.direction = "down"
        
        else :
            self.y  += 3
            if self. y > (self.originalY + 55) :
                self.direction = "right"
        self.getRect()
        
    

# Method that re-stores the x and y coordinates and the width and height of 
# the image

    def getRect(self): 
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)
    

