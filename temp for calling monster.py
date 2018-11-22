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
        self.margin = 10
        self.numRows = 8
        self.numCols = 8
        self.counter = 0
        self.plantSpace = [[]]
        #self.stepX is the width of each grid block
        self.stepX = int ((self.width - (2*self.margin))/ self.numCols)
        self.stepY = int ((self.height - (2*self.margin))/self.numRows)
        self.boxes = [[]]
        self.createDifferentGrids () #Helper function
        self.boxes.remove ([])
        self.plantSpace.remove ([])
        self.monsters = pygame.sprite.Group(Zombie(self.boxes[0][0][0] +  \
                        self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.margin, self.width, 
                        self.height, self.stepY)) 
        self.highlighted = (-1, -1)
        
        
# Helper function that creates different grids for zombies and plants

    def createDifferentGrids (self) :
        plantTemp = []
        temp = []
        skip = 1
        first = True
        for row in range (self.margin, self.height - self.margin, self.stepY):
            for col in range (self.margin, self.width - self.margin, \
            self.stepX) :
                temp += [(col, row)]
                plantTemp += [(col, row)]
            if skip == 0: #plantSpace list takes in 2 lines of coordinates
                skip += 1
            elif skip == 1 :
                skip = 0
                if first: # skips first column
                    self.plantSpace.append ([plantTemp[1]] + \
                    [plantTemp[-1]])
                    first = False
                elif not first:
                    self.plantSpace.append ([plantTemp[0]] + \
                    [plantTemp[-2]])
                    first = True
                plantTemp = []
            self.boxes.append (temp) 
            temp = []
        
        

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
                        self.numRows, self.numCols, self.margin, self.width, 
                        self.height, self.stepY))) 
        self.monsters.update(self.width, self.height)

# View function that first generates grid and then the monsters
    def redrawAll(self, screen):
        screen.fill(self.otherLightBlue)
        points = []
        reversed = []
        self.getPlantSpace (screen) #Calls helper function to get plantList
        if not (self.highlighted == (-1,-1)) :
            pygame.draw.polygon (screen, (self.lightSalmon), self.highlighted,\
            0) #highlighted cell based on mouse click
        for col in range (self.margin, self.width - self.margin, \
            int ((self.width - (2*self.margin))/ self.numCols)) :
            for row in range (self.margin, self.height - self.margin, \
                int ((self.height - (2*self.margin)) / self.numRows)):
                point = (row, col) #horizontal lines
                revPoint = (col, row) #vertical lines
                points.append (point)
                reversed.append (revPoint)
            pygame.draw.lines(screen, self.black, False, points, 3)
            pygame.draw.lines (screen, self.black, False, reversed, 3)
            points = []
            reversed = []
        self.monsters.draw(screen)


# Helper function that draws boxes designated for plants

    def getPlantSpace (self, screen) :
        for row in self.plantSpace:
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
            pygame.draw.polygon (screen, (self.lightPurple), plantPoints, \
            0)

Game(600, 600).run()

