# Main game class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 11/20/18


import pygame
from Enemy import Enemy
from Monster import Monster
from Zombie import Zombie
from pygamegame import PygameGame
import random
import math

# Game class that generates grid and monsters

class Game(PygameGame):
    
# Constructor method that initializes 2-D grid list

    def init(self):
        #rgb values of colors stored as tuples
        self.black = (0,0,0)
        self.lightSalmon = (255,160,122)
        self.lightBlue = (204, 255, 255)
        self.otherLightBlue = (173,216,230)
        self.lightPurple = (204, 204, 255)
        self.peach = (255, 229, 153)
        self.lightPink = (255, 204, 204)
        self.lightYellow = (250, 250, 210)
        self.firstMargin = 10
        self.endMargin = 150
        self.numRows = 8
        self.numCols = 8
        self.counter = 0
        self.plantBlocks = [[]]
        #self.stepX is the width of each grid block
        self.stepX = int ((self.width - (2*self.firstMargin))/ self.numCols)
        self.stepY = int ((self.height - (self.endMargin) - self.firstMargin)/self.numRows)
        self.boxes = [[]]
        
        actualXChange = (self.width - 2 *self.firstMargin) / self.numCols
        self.offSet = int (self.numCols * (actualXChange) - (self.stepX * self.numCols))
        print (self.offSet)
        
        firstBox = [(self.firstMargin, self.firstMargin)] + [( self.firstMargin + self.stepX, self.firstMargin + self.stepY)]
        self.plantBlocks.append (firstBox)
        self.createDifferentGrids () #Helper functions
        self.createDifferentTracks(self.firstMargin, self.firstMargin)
        self.boxes.remove ([])
        self.plantBlocks.remove ([])
        self.monsters = pygame.sprite.Group(Zombie(self.boxes[0][0][0] +  \
                        self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY)) 
        self.highlighted = (-1, -1)
     
        
        
# Helper function that creates overall grid

    def createDifferentGrids (self) :
        temp = []
        for row in range (self.firstMargin, self.height - self.endMargin + 1, self.stepY):
            for col in range (self.firstMargin, self.width - self.firstMargin, \
            self.stepX) :
                temp += [(col, row)]
            self.boxes.append (temp) 
            temp = []
            
    
# Helper function that creates different tracks for enemies

    def createDifferentTracks (self, xValue, yValue) :
        if (xValue + self.stepX)  >= (self.width - self.firstMargin - self.offSet) :
            print ("Good luck!")
            return self.plantBlocks
        for move in self.getPossibleMoves ():
            tempXValue = xValue + move[0]
            tempYValue = yValue + move[1]
            p1 = (tempXValue, tempYValue)
            p2 = (tempXValue + self.stepX, tempYValue + self.stepY)
            row = [p1] + [p2]
            if self.checkValues(row) :
                self.plantBlocks.append (row)
                xValue += move[0]
                yValue += move[1]
                tmpSolution = self.createDifferentTracks(xValue, yValue)
                if tmpSolution != None:
                    return tmpSolution
                self.plantBlocks[::-1].remove (row)
                xValue -= move[0]
                yValue -= move[1]
                
        return None
        
       
# Helper function that checks if the new block's side is touching an already
# stored block's side

    def checkValues (self, row) :
        if row in self.plantBlocks: #Can't go backwards
            return False
            
        firstXCoord = row[0][0]
        firstYCoord = row[0][1]
        
        endXCoord = row[1][0]
        endYCoord = row[1][1]
        
        if firstXCoord < self.firstMargin: #Following if statements check if block goes off grid
            return False
        elif firstYCoord < self.firstMargin or endYCoord > (self.height - self.endMargin) :
            return False
        
        for block in range (len (self.plantBlocks)): #Checks if touching right side, then check if left side
            if block == (len  (self.plantBlocks) - 1) or block == 0 :
                continue
            if endXCoord == self.plantBlocks[block][0][0] and firstYCoord == self.plantBlocks[block][0][1] : #checks if new block is bordering from right
                return False
            elif firstXCoord == self.plantBlocks[block][1][0] and firstYCoord == self.plantBlocks[block][0][1]  : #checks if new block is bordering from left
                return False
            elif firstYCoord == self.plantBlocks[block][1][1] and firstXCoord == self.plantBlocks[block][0][0]: #checks if bordering from top
                return False
            elif endYCoord == self.plantBlocks [block][0][1] and firstXCoord == self.plantBlocks[block][0][0]: #checks if bordering from bottom
                return False
        return True
        
    
# Helper function that randomly generates new change in xValue and yValue of
# blocks

    def getPossibleMoves (self) :
        numBlocks = 0
        moves = []
        while numBlocks != 4:
            xChange = random.randint (-1, 1)
            yChange = random.randint (-1, 1)
            specBlock = (xChange * self.stepX, yChange * self.stepY)
            if not (specBlock in moves):
                if not (abs(xChange) == abs(yChange)) :
                    moves.append (specBlock)
                    numBlocks += 1
        return moves
                
        
        

# MousePressed function allows you to highlight cells

    def mousePressed (self, x, y) :
        col = (x - self.margin) // self.stepX
        row = (y - self.margin) // self.stepY
        first = self.boxes[row][col]
        second = self.boxes[row + 1][col + 1]
        third = self.boxes [row][col + 1]
        fourth = self.boxes[row + 1][col]
        #Creates list of tuples of each box corner
        self.highlighted = [first] + [third] + [second] + [fourth]

# Called approximately every 20 milliseconds and updates position of monsters

    def timerFired(self, dt):
        self.counter += 1
        if self.counter % 94 == 0: #Every 2 seconds generates a monster
            y = random.randint (0, 7)
            self.monsters.add (pygame.sprite.Group(Monster(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY))) 
        self.monsters.update(self.width, self.height)

# View function that first generates grid and then the monsters
    def redrawAll(self, screen):
        screen.fill(self.lightYellow)
        points = []
        reversed = []
        self.getPlantBlocks (screen)
        if not (self.highlighted == (-1,-1)) :
            pygame.draw.polygon (screen, (self.lightSalmon), self.highlighted,\
            0) #highlighted cell based on mouse click
        for col in range (self.firstMargin, self.width - self.firstMargin, \
            self.stepX) :
            for row in range (self.firstMargin, self.height - self.endMargin + 1, \
                self.stepY):
                point = (col, row) #vertical lines
                revPoint = (row, col) #horizontal lines
                points.append (point)
                reversed.append (revPoint)
                
            pygame.draw.lines(screen, self.black, False, points, 3)
            #pygame.draw.lines (screen, self.black, False, reversed, 3)
            # print ("Points", points)
            
            points = []
            reversed = []
            

        for row in range (self.firstMargin, self.height - self.endMargin + 1, \
                            self.stepY) :
            for col in range (self.firstMargin, self.width - self.firstMargin, \
                            self.stepX):
                revPoint = (col, row)
                reversed.append (revPoint)
            pygame.draw.lines (screen, self.black, False, reversed, 3)
            reversed = []
        self.monsters.draw(screen)


            
# Helper function that gets plant boxes
    def getPlantBlocks (self, screen) :
        for row in self.plantBlocks:
            x1 = row[0][0]
            x2 = row[1][0]
            y1 = row[0][1]
            y2 = row[1][1]
            p1 = [(x1, y1)]
            p2 = [(x2, y2)]
            p3 = [(x1, y2)]
            p4 = [(x2, y1)]
            plantPoints = p1 + p3 + p2 + p4 #4 tuple points that make up 
            #rectangle where plants will be stored
            pygame.draw.polygon (screen, (self.lightSalmon), plantPoints, \
            0)

Game(600, 600).run()

