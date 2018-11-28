# Enemy class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 11/23/18

import pygame
import random
import math

# Enemy class with properties and methods for monsters, zombies, and ghosts

class Enemy(pygame.sprite.Sprite):

# Constructor method that initializes monster image, location, and speed
    def __init__(self, x, y, rows, cols, margin, width, height, stepY, stepX, plantBlocks, grassSlot, direction):
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
        self.index = 0
        self.plantBlocks = plantBlocks
        self.health = 20
        self.grassSlot = grassSlot
        self.stepY = stepY
        self.stepX = stepX
        self.direction = direction
        
      

# Method that re-stores the x and y coordinates and the width and height of 
# the image

    def getRect(self): 
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)



# Helper function that checks if the enemy is at the grass, given the direction

    def atGrass (self) :
        
        if self.direction == "up" :
            if self.y <= (self.grassSlot[1] + self.stepY * (1.5)) :
                if self.x == (self.grassSlot[0] + self.stepX/2) :
                    return True
                    
        elif directio
            
            
    



# Method that updates the x and y values of the object

    def update(self, screenWidth, screenHeight):
        
        if self.atGrass () :
            return
        
        if self.index == (len (self.plantBlocks) -1) : #Checks if at last block
            self.x += self.xSpeed
            self.y += self.ySpeed
            self.getRect()
            return
        
        self.x += self.xSpeed
        self.y += self.ySpeed
        
        firstBlock = self.plantBlocks[self.index]
        secondBlock = self.plantBlocks[self.index + 1]
        
        firstXCoord = firstBlock[0][0]
        secondXCoord = firstBlock[1][0]
        firstYCoord = firstBlock[0][1]
        secondYCoord = firstBlock [1][1]
        xMidPoint = (firstXCoord + secondXCoord) / 2
        yMidPoint = (firstYCoord + secondYCoord) / 2
        
        if not (self.atBlock (firstBlock)):
            self.index += 1
            firstBlock = self.plantBlocks[self.index]
            if self.index == (len (self.plantBlocks) -1) :
                return
            
            secondBlock = self.plantBlocks[self.index + 1]
            firstXCoord = firstBlock[0][0]
            secondXCoord = firstBlock[1][0] #not second block, but second coordinate within same block
            firstYCoord = firstBlock[0][1]
            secondYCoord = firstBlock [1][1]
            xMidPoint = (firstXCoord + secondXCoord) / 2
            yMidPoint = (firstYCoord + secondYCoord) / 2
        
        if abs (self.x - xMidPoint) < 3 and abs (self.y - yMidPoint) < 3: #We're at the middle of a point
            if secondBlock [1][1] > firstBlock [1][1] :
                self.xSpeed = 0
                self.ySpeed = 1
            elif secondBlock [1][1] < firstBlock [1][1] :
                self.xSpeed = 0
                self.ySpeed = -1
            elif secondBlock [1][0] > firstBlock [1][0] :
                self.xSpeed = 1
                self.ySpeed = 0
            else:
                self.xSpeed = -1
                self.ySpeed = 0
        self.getRect()
    


# Helper function that checks if image coordinates are within specified block

    def atBlock (self, firstBlock) :
        firstXCoord = firstBlock [0][0]
        secondXCoord = firstBlock [1][0]
        
        firstYCoord = firstBlock [0][1]
        secondYCoord = firstBlock [1][1]
        if firstXCoord < self.x < secondXCoord:
            if firstYCoord < self.y < secondYCoord :
                return True
        return False

