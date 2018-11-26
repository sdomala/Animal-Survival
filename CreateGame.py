# Main game class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 11/20/18


import pygame
from Enemy import Enemy
from Monster import Monster
from Zombie import Zombie
from Animal import Animal
from Weapon import Weapon
from Coin import Coin
from Dog import Dog
from Goat import Goat
from Cow import Cow
from Alligator import Alligator
from Gorilla import Gorilla
from Lion import Lion
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
        firstBox = [(self.firstMargin, self.firstMargin)] + [( self.firstMargin + self.stepX, self.firstMargin + self.stepY)]
        self.plantBlocks.append (firstBox)
        self.createDifferentGrids () #Helper functions
        self.createDifferentTracks(self.firstMargin, self.firstMargin)
        self.boxes.remove ([])
        self.plantBlocks.remove ([])
        self.enemies = pygame.sprite.Group(Zombie(self.boxes[0][0][0] +  \
                        self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.plantBlocks)) 
        self.highlighted = (-1, -1)
        self.firstAnimal = True
        self.hasAnimal = False
        self.weapons = []
        self.hasWeapon = False
        self.money = 10
        
     
        
        
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
                self.plantBlocks = self.plantBlocks[::-1]
                self.plantBlocks.remove (row)
                self.plantBlocks = self.plantBlocks [::-1]
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
        col = (x - self.firstMargin) // self.stepX
        row = (y - self.firstMargin) // self.stepY
        first = self.boxes[row][col]
        second = self.boxes[row + 1][col + 1]
        third = self.boxes [row][col + 1]
        fourth = self.boxes[row + 1][col]
        #Creates list of tuples of each box corner
        self.hasAnimal = True
        if self.firstAnimal:
            self.animals = pygame.sprite.Group(Animal(first[0] + self.stepX / 2, first[1] + self.stepY / 2)) 
            self.firstAnimal = False
        else :
            self.animals.add (pygame.sprite.Group(Animal(first[0] + self.stepX / 2, first[1] + self.stepY / 2)))

# Called approximately every 20 milliseconds and updates position of enemies

    def timerFired(self, dt):
        self.counter += 1
        if self.counter % 141 == 0: #Every 3 seconds generates a enemies
            y = random.randint (0, 7)
            self.enemies.add (pygame.sprite.Group(Monster(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.plantBlocks))) 
        self.enemies.update(self.width, self.height)
        
        
        if self.hasAnimal and self.counter % 47 == 0:
            for animal in self.animals:
                if self.hasWeapon == False :
                    self.weapons = pygame.sprite.Group(Weapon(animal.x, animal.y, 3, 0))
                    self.weapons.add (pygame.sprite.Group(Weapon(animal.x, animal.y, -3, 0)))
                    self.weapons.add (pygame.sprite.Group(Weapon(animal.x, animal.y, 0, 3)))
                    self.weapons.add (pygame.sprite.Group(Weapon(animal.x, animal.y, 0, -3)))
                    self.hasWeapon = True
                else: 
                    self.weapons.add (pygame.sprite.Group(Weapon(animal.x, animal.y, 3, 0)))
                    self.weapons.add (pygame.sprite.Group(Weapon(animal.x, animal.y, -3, 0)))
                    self.weapons.add (pygame.sprite.Group(Weapon(animal.x, animal.y, 0, 3)))
                    self.weapons.add (pygame.sprite.Group(Weapon(animal.x, animal.y, 0, -3)))
        if self.hasWeapon:
            self.weapons.update ()
            
        self.updateCollisions() 
        
    
# Helper function that checks for collisions and updates the health/existence
# of the enemies

    def updateCollisions (self) :
        for weapon in self.weapons:
            for enemy in self.enemies:
                if pygame.sprite.collide_mask (weapon, enemy) :
                    enemy.health -= weapon.damage
                    self.weapons.remove (weapon)
                    print (enemy.health, weapon.damage)
                    if enemy.health <= 0:
                        self.enemies.remove (enemy)

# View function that first generates grid and then the monsters
    def redrawAll(self, screen):
        screen.fill(self.lightBlue)
        points = []
        reversed = []
        self.getPlantBlocks (screen)
        if self.hasAnimal:
            self.animals.draw (screen)
        
        if self.hasWeapon:
            self.weapons.draw (screen)
        
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
        self.enemies.draw(screen)                                            
        self.createCoin(screen)
        self.createAnimalDisplay (screen)
        
        
        
# Helper function that creates coin in bottom right corner

    def createCoin (self, screen) :
        self.coin = pygame.sprite.Group(Coin(self.width - 5 * self.firstMargin,\
                                            self.height - 0.5 * self.endMargin))
        self.coin.draw (screen)
        pygame.font.init() 
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(str (self.money), False, (0, 0, 0))
        length = len (str (self.money))
        screen.blit(textsurface,(self.width - (6 + 0.8 * (length - 1)) * self.firstMargin, \
                                self.height - 0.66 * self.endMargin))
        

# Helper function that displays animals at the bottom of the screen

    def createAnimalDisplay (self, screen) :
        self.displayAnimals = pygame.sprite.Group(Dog(6 * self.firstMargin, self.height - 0.75 * self.endMargin))
        self.displayAnimals.add (pygame.sprite.Group (Goat (24 * self.firstMargin, self.height - 0.75 * self.endMargin)))
        self.displayAnimals.add (pygame.sprite.Group (Cow (42 * self.firstMargin, self.height - 0.75 * self.endMargin)))
        self.displayAnimals.add (pygame.sprite.Group (Alligator (6 * self.firstMargin, self.height - 0.2 * self.endMargin)))
        self.displayAnimals.add (pygame.sprite.Group (Gorilla (24 * self.firstMargin, self.height - 0.2 * self.endMargin)))
        self.displayAnimals.add (pygame.sprite.Group (Lion (42 * self.firstMargin, self.height - 0.2 * self.endMargin)))
        
        self.displayAnimals.draw (screen)

            
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

