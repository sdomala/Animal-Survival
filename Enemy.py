# Enemy class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 11/20/18

import pygame
import random
import math

# Enemy class with properties and methods related to monster objects

class Enemy(pygame.sprite.Sprite):

# Constructor method that initializes monster image, location, and speed
    def __init__(self, x, y, rows, cols, margin, width, height, stepY):
        super(Enemy, self).__init__()
        self.x, self.y = x, y
        self.xSpeed = 1
        self.ySpeed = 0
        self.image = pygame.image.load ('BrownMonster2.png').convert_alpha()        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)
        self.first = margin #Top coordinate of grid
        self.end = height - (height - self.first) % (stepY) #Bottom coordinate 
        self.numRows = rows
        self.numCols = cols
        self.skip = 4 #Ignores 1st, second, and third row when calculating
                      # places where enemies change direction
        self.yPoints = []
        self.getYPoints ()

# Helper function that determines specific y-coordinates where the enemies
# change direction

    def getYPoints (self) :
        firstPoint = self.first
        secondPoint = self.first
        step = int ((self.end - self.first) / self.numRows)
        counter = 0
        for yCoordinate in range (self.first, self.end + step, step ) :
            temp = secondPoint
            secondPoint = yCoordinate
            firstPoint = temp
            counter += 1
            if yCoordinate == self.end:
                self.end = ((firstPoint + secondPoint) / 2)
                continue
            if counter < self.skip or not (counter % 2 == 0): #Skips every other
                if counter == 2:                              #point
                    self.start = ((firstPoint + secondPoint) / 2)
                continue
            self.yPoints.append ((firstPoint + secondPoint) / 2)
            
      

# Method that re-stores the x and y coordinates and the width and height of 
# the image

    def getRect(self): 
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)


# Method that updates the x and y values of the object

    def update(self, screenWidth, screenHeight):
        self.x += self.xSpeed
        self.y += self.ySpeed
        if self.y == self.yPoints[0] or self.y == self.yPoints[2] :
            self.xSpeed = -1
            self.ySpeed = 0
            if self.x == self.start:
                self.xSpeed = 0
                self.ySpeed = 1
            self.getRect()
            return #Ensures last if statement doesn't get called
        elif self.y == self.yPoints[1]:
            self.xSpeed = 1
            self.ySpeed = 0
            if self.x == self.end :
                self.ySpeed = 1
                self.xSpeed = 0
            self.getRect()
            return 
        if self.x == self.end: #First conditional statement to pass
            self.ySpeed = 1
            self.xSpeed = 0
        self.getRect()
        


# first = Enemy (20, 20, 20, 20, 20, 20, 20, 20)