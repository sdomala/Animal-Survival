# Main game class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 11/28/18

# Citation: Got this starter class from Pygame manual from 112 website
# Created by Lukas Peraza


import pygame
from Enemy import Enemy
from Monster import Monster
from Zombie import Zombie
from Ghost import Ghost
from Animal import Animal
from Weapon import Weapon
from Bone import Bone
from Horn import Horn
from Milk import Milk
from Water import Water
from Banana import Banana
from Coin import Coin
from Dog import Dog
from Goat import Goat
from Cow import Cow
from Alligator import Alligator
from Gorilla import Gorilla
from Lion import Lion
from Grass import Grass
from Fruit import Fruit
from Barn import Barn
from SmallCoin import SmallCoin
from Earth import Earth
from pygamegame import PygameGame
import random
import math
import copy

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
        self.purple = (102, 0, 204)
        self.peach = (255, 229, 153)
        self.lightPink = (255, 204, 204)
        self.lightYellow = (250, 250, 210)
        self.turquoise = (64, 224, 208)
        self.firstMargin = 10
        self.endMargin = 150
        self.numRows = 8
        self.numCols = 8
        self.counter = 0
        
        #self.stepX is the width of each grid block
        self.stepX = int ((self.width - (2*self.firstMargin))/ self.numCols)
        self.stepY = int ((self.height - (self.endMargin) - self.firstMargin)/self.numRows)
        
        actualXChange = (self.width - 2 *self.firstMargin) / self.numCols
        self.offSet = int (self.numCols * (actualXChange) - (self.stepX * self.numCols))        
        
        self.firstAnimal = True
        self.hasAnimal = False
        self.animals = []
        self.weapons = []
        self.hasWeapon = False
        self.money = 10
        self.chooseAnimal = True
        self.type = "dog"
        self.level = 0
        self.makeVariousGrids() 
        self.dogPrice = 5
        self.goatPrice = 10
        self.cowPrice = 20
        self.alligatorPrice =70
        self.gorillaPrice = 150
        self.lionPrice = 2
        self.stopMoving = False
        self.weaponCounter = 0
        self.levelDisplay = False
        self.enemySpeed = 1
        self.enemies = pygame.sprite.Group(Monster(self.boxes[0][0][0] +  \
                        self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.stepX, self.plantBlocks, self.grassSlot, self.direction, self.enemySpeed)) 
        self.highlighted = (-1, -1)
        self.firstStep = 0
        self.enemiesEatingGrass = []
        self.enemiesEatingFruit = []
        self.enemiesEatingBarn = []
        self.fruitLength = 0
        self.grassLength = 0
        self.barnLength = 0
        self.grassHealth = 200
        self.fruitHealth = 200
        self.barnHealth = 200
        self.firstGrass = False
        self.firstBarn = False
        self.firstFruit = False
        self.gameOver = False
        self.noBarn = False
        self.noGrass = False
        self.noFruit = False
        self.damage = 0
        self.pownage = False
        self.typeDisplay = None
        self.lionDamage = 0
        self.lionCollision = False
        self.timeIndex = 141
        self.hasEnemy = True
        self.randomVariable = 0
        self.tempCounter = 0
        
        
        
      

# Helper function that designates specific slot for grass

    def getGrass (self) :
        found = False
        while not found:
            block = random.randint (0, len (self.plantBlocks) - 1)
            up = True
            down = True
            right = True
            left = True
            yCoordinate = self.plantBlocks[block][0][1]
            xCoordinate = self.plantBlocks[block][0][0]
            for row in self.plantBlocks:
                col = row [0]
                # print (col)    
                if (yCoordinate - self.stepY) == col[1] and xCoordinate == col[0] or (yCoordinate - self.stepY < self.firstMargin):
                    # print ("up")
                    up = False
                if (yCoordinate + self.stepY) == col[1] and xCoordinate == col[0] or (yCoordinate + self.stepY) >= (self.height - self.endMargin):
                    # print ("Down")
                    down = False
                if (xCoordinate + self.stepX) == col[0] and yCoordinate == col[1] or (xCoordinate + self.stepX) >= self.boxes[-1][-1][0] :
                    # print ("right")
                    right = False
                if (xCoordinate - self.stepX == col [0]) and yCoordinate == col[1] or (xCoordinate - self.stepX < self.firstMargin) :
                    # print ("left")
                    left = False
            
        
            if xCoordinate < self.width / 2 :
                continue
            if up:
                self.direction = "up"
                self.grassSlot = (xCoordinate, yCoordinate - self.stepY)
                found = True
            elif down:
                self.direction = "down"
                self.grassSlot = (xCoordinate, yCoordinate + self.stepY)
                found = True
        
            elif left:
                self.direction = "left"
                self.grassSlot = (xCoordinate - self.stepX, yCoordinate)
                found = True
            elif right:
                self.direction = "right"
                self.grassSlot = (xCoordinate + self.stepX, yCoordinate)
                found = True
        
            else:
                continue
            

# Helper function that designates specific slot for fruit

    def getFruit (self) :
        found = False
        while not found:
            block = random.randint (0, len (self.plantBlocks) - 1)
            up = True
            down = True
            right = True
            left = True
            yCoordinate = self.plantBlocks[block][0][1]
            xCoordinate = self.plantBlocks[block][0][0]
            for row in self.plantBlocks:
                col = row [0]
                # print (col)    
                if (yCoordinate - self.stepY) == col[1] and xCoordinate == col[0] or (yCoordinate - self.stepY < self.firstMargin):
                    # print ("up")
                    up = False
                if (yCoordinate + self.stepY) == col[1] and xCoordinate == col[0] or (yCoordinate + self.stepY) >= (self.height - self.endMargin):
                    # print ("Down")
                    down = False
                if (xCoordinate + self.stepX) == col[0] and yCoordinate == col[1] or (xCoordinate + self.stepX) >= self.boxes[-1][-1][0] :
                    # print ("right")
                    right = False
                if (xCoordinate - self.stepX == col [0]) and yCoordinate == col[1] or (xCoordinate - self.stepX < self.firstMargin) :
                    # print ("left")
                    left = False
            
        
            if xCoordinate < self.width / 2 :
                continue
            if up:
                self.direction = "up"
                self.fruitSlot = (xCoordinate, yCoordinate - self.stepY)
                found = True
            elif down:
                self.direction = "down"
                self.fruitSlot = (xCoordinate, yCoordinate + self.stepY)
                found = True
        
            elif left:
                self.direction = "left"
                self.fruitSlot = (xCoordinate - self.stepX, yCoordinate)
                found = True
            elif right:
                self.direction = "right"
                self.fruitSlot = (xCoordinate + self.stepX, yCoordinate)
                found = True
        
            else:
                continue
            
            if self.fruitSlot == self.grassSlot: #final check to see if slot is the same as grass slot
                found = False
                continue
            
            
        
    
# Helper function that designates specific slot for barn

    def getBarn (self) :
        found = False
        while not found:
            block = random.randint (0, len (self.plantBlocks) - 1)
            up = True
            down = True
            right = True
            left = True
            yCoordinate = self.plantBlocks[block][0][1]
            xCoordinate = self.plantBlocks[block][0][0]
            for row in self.plantBlocks:
                col = row [0]
                # print (col)    
                if (yCoordinate - self.stepY) == col[1] and xCoordinate == col[0] or (yCoordinate - self.stepY < self.firstMargin):
                    # print ("up")
                    up = False
                if (yCoordinate + self.stepY) == col[1] and xCoordinate == col[0] or (yCoordinate + self.stepY) >= (self.height - self.endMargin):
                    # print ("Down")
                    down = False
                if (xCoordinate + self.stepX) == col[0] and yCoordinate == col[1] or (xCoordinate + self.stepX) >= self.boxes[-1][-1][0] :
                    # print ("right")
                    right = False
                if (xCoordinate - self.stepX == col [0]) and yCoordinate == col[1] or (xCoordinate - self.stepX < self.firstMargin) :
                    # print ("left")
                    left = False
            
        
            if xCoordinate < self.width / 2 :
                continue
            if up:
                self.direction = "up"
                self.barnSlot = (xCoordinate, yCoordinate - self.stepY)
                found = True
            elif down:
                self.direction = "down"
                self.barnSlot = (xCoordinate, yCoordinate + self.stepY)
                found = True
        
            elif left:
                self.direction = "left"
                self.barnSlot = (xCoordinate - self.stepX, yCoordinate)
                found = True
            elif right:
                self.direction = "right"
                self.barnSlot = (xCoordinate + self.stepX, yCoordinate)
                found = True
        
            else:
                continue
            
            if self.barnSlot == self.grassSlot or self.barnSlot == self.fruitSlot: #final check to see if slot is the same as grass slot
                found = False
                continue
    
    

# Helper funcion that makes various grids

    def makeVariousGrids (self) :
        self.boxes = [[]]
        self.plantBlocks = [[]]
        firstBox = [(self.firstMargin, self.firstMargin)] + [( self.firstMargin + self.stepX, self.firstMargin + self.stepY)]
        self.plantBlocks.append (firstBox)
        self.createDifferentGrids () #Helper functions
        self.createDifferentTracks(self.firstMargin, self.firstMargin)
        if self.level < 8 :
            index = random.randint (0,9)
            self.plantBlocks = self.getFirstPlantBlocks()[index]
        
        if [] in self.boxes:
            self.boxes.remove ([])
        if [] in self.plantBlocks: 
            self.plantBlocks.remove ([])
        self.availableSlots = copy.deepcopy (self.boxes)
        self.tempSlots = copy.deepcopy (self.availableSlots)
        for row in range (len (self.availableSlots)):
            for col in self.availableSlots[row] :
                for plantRow in self.plantBlocks:
                    if col == plantRow[0]:
                        self.tempSlots[row].remove (col)
        self.availableSlots = self.tempSlots
        self.getGrass()
        self.getFruit() 
        self.getBarn()
        self.grass = pygame.sprite.Group (Grass (self.grassSlot[0] + 35, self.grassSlot[1] + 20))
        self.fruit = pygame.sprite.Group (Fruit (self.fruitSlot[0] + 35, self.fruitSlot[1] + 20))
        self.barn = pygame.sprite.Group (Barn (self.barnSlot[0] + 35, self.barnSlot[1] + 20))
        
        

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
                
        

# Helper function that determines what type of animal the user will place on the board

    def getType (self, x, y) :
            self.chooseAnimal = False
            if x >= ((6 * self.firstMargin) - 29) and x<= (6 * self.firstMargin + 29) and y <= ((self.height - 0.75 * self.endMargin) + 29) and y >= ((self.height - 0.75 * self.endMargin) - 29) :
                if self.money >= self.dogPrice:
                    self.type = "dog"
                else:
                    self.chooseAnimal = True
                    return
            elif x >= ((24 * self.firstMargin) - (53/2)) and x <= ((24 * self.firstMargin) + (53/2)) and y >= ((self.height - 0.75 * self.endMargin) - (53/2)) and y <= ((self.height - 0.75 * self.endMargin) + (53/2)):
                if self.money >= self.goatPrice :
                    self.type = "goat"
                else :
                    self.chooseAnimal = True
                    return
            elif x >= ((42 * self.firstMargin) - (73/2)) and x <= ((42 * self.firstMargin) + (73/2)) and y >= ((self.height - 0.75 * self.endMargin) - (51/2)) and y <= ((self.height - 0.75 * self.endMargin) + (51/2)) :
                if self.money >= self.cowPrice:
                    self.type = "cow"
                else :
                    self.chooseAnimal = True
                    return
                
            elif x >= ((6 * self.firstMargin) - (55/2)) and x <= ((6 * self.firstMargin) + (55/2)) and y <= ((self.height - 0.2 * self.endMargin) + (57/2)) and y >= ((self.height - 0.2 * self.endMargin) - (57/2))  :
                if self.money >= self.alligatorPrice:
                    self.type = "alligator"
                else :
                    self.chooseAnimal = True
                    return
                
            elif x >= ((24 * self.firstMargin) - (39/2)) and x <= ((24 * self.firstMargin) + (39/2)) and y <= ((self.height - 0.2 * self.endMargin) + 25) and y >= ((self.height - 0.2 * self.endMargin) - 25) :
                if self.money >= self.gorillaPrice :
                    self.type = "gorilla"
                else:
                    self.chooseAnimal = True
                    return
                
            elif x >= ((42 * self.firstMargin) - 29) and x <= ((42 * self.firstMargin) + 29) and y <= ((self.height - 0.2 * self.endMargin) + 27) and y >= ((self.height - 0.2 * self.endMargin) - 27):
                if self.money >= self.lionPrice:
                    self.type = "lion"
                else :
                    self.chooseAnimal = True
                    return
                
            else :
                self.chooseAnimal = True

# MousePressed function allows you to highlight cells

    def mousePressed (self, x, y) :
        if self.level == 0:
            if (x >= self.width/2 - 75) and x <= (self.width/2 + 75) and y >= (self.height/2 + 100) and y <= (self.height/2 + 200):
                self.level += 1
                return
        if self.chooseAnimal:
            self.getType (x, y)
            
    
        else :
            self.placeAnimal (x, y)
            
            
            
# Helper function that places animal on board

    def placeAnimal (self, x, y) :
        valid = False
        endY = self.boxes[-1][-1][-1]
        if y >= endY :
            self.chooseAnimal = True
            return
            
        col = (x - self.firstMargin) // self.stepX
        row = (y - self.firstMargin) // self.stepY
        first = self.boxes[row][col]
        
        self.tempSlots = copy.deepcopy (self.availableSlots) 
        for row in range (len (self.availableSlots)) :
            for item in self.availableSlots[row]:
                if first == item:
                    valid = True
                    self.tempSlots[row].remove (item)
        
        
        if valid == False:
            self.chooseAnimal = True
            return 
                    
        self.availableSlots = self.tempSlots
        
        
        #Creates list of tuples of each box corner
        self.hasAnimal = True
        if self.type == "dog" :
            self.money -= self.dogPrice
            if self.firstAnimal:
                self.animals = pygame.sprite.Group(Dog(first[0] + self.stepX / 2, first[1] + self.stepY / 2)) 
                self.firstAnimal = False
            else :
                self.animals.add (pygame.sprite.Group(Dog(first[0] + self.stepX / 2, first[1] + self.stepY / 2)))
        elif self.type == "goat" :
            self.money -= self.goatPrice
            if self.firstAnimal:
                self.animals = pygame.sprite.Group(Goat(first[0] + self.stepX / 2, first[1] + self.stepY / 2)) 
                self.firstAnimal = False
            else :
                self.animals.add (pygame.sprite.Group(Goat(first[0] + self.stepX / 2, first[1] + self.stepY / 2)))
        elif self.type == "cow" :
            self.money -= self.cowPrice
            if self.firstAnimal :
                self.animals = pygame.sprite.Group(Cow(first[0] + self.stepX / 2, first[1] + self.stepY / 2)) 
                self.firstAnimal = False
            else :
                self.animals.add (pygame.sprite.Group(Cow(first[0] + self.stepX / 2, first[1] + self.stepY / 2)))
        elif self.type == "alligator":
            self.money -= self.alligatorPrice
            if self.firstAnimal:
                self.animals = pygame.sprite.Group(Alligator(first[0] + self.stepX / 2, first[1] + self.stepY / 2)) 
                self.firstAnimal = False
            else :
                self.animals.add (pygame.sprite.Group(Alligator(first[0] + self.stepX / 2, first[1] + self.stepY / 2)))
        elif self.type == "gorilla":
            self.money -= self.gorillaPrice
            if self.firstAnimal:
                self.animals = pygame.sprite.Group(Gorilla(first[0] + self.stepX / 2, first[1] + self.stepY / 2)) 
                self.firstAnimal = False
            else :
                self.animals.add (pygame.sprite.Group(Gorilla(first[0] + self.stepX / 2, first[1] + self.stepY / 2)))
        elif self.type == "lion":
            self.money -= self.lionPrice
            if self.firstAnimal:
                self.animals = pygame.sprite.Group(Lion(first[0] + self.stepX / 2, first[1] + self.stepY / 2)) 
                self.firstAnimal = False
            else :
                self.animals.add (pygame.sprite.Group(Lion(first[0] + self.stepX / 2, first[1] + self.stepY / 2)))
        self.chooseAnimal = True
  

# Helper funcion that deletes enemies off board

    def deleteEnemies (self) :
        for enemy in self.enemies:
            if enemy.x > (self.boxes[-1][-1][0]) :
                self.enemies.remove (enemy)
                

           
        
    

# Helper function that deletes weapons off board

    def deleteWeapons (self) :
        for weapon in self.weapons :
            if weapon.x > self.boxes[-1][-1][0] or weapon.x < self.firstMargin or weapon.y < self.firstMargin or weapon.y > self.boxes[-1][-1][1] :
                self.weapons.remove (weapon)
                
     

    

# Called approximately every 20 milliseconds and updates position of enemies

    def timerFired(self, dt):
        print (self.counter)
        self.tempCounter += 1
        counter = 0
        for enemy in self.enemies:
            if enemy.stopTheEnemy:
                counter += 1
        
        

        self.fruitHealth -= (self.fruitLength) * 0.02
        self.grassHealth -= (self.grassLength) * 0.02
        self.barnHealth -= (self.barnLength) * 0.02
        if self.grassHealth <= 0:
            self.grass = []
            self.grassSlot = (-200, -200)
            for enemy in self.enemies:
                if isinstance (enemy, Monster) :
                    enemy.stopTheEnemy = False
            self.noGrass = True
        if self.fruitHealth <= 0:
            self.fruit = []
            self.fruitSlot = (-200, -200)
            for enemy in self.enemies:
                if isinstance (enemy, Zombie) :
                    enemy.stopTheEnemy = False
            self.noFruit = True
        
        if self.barnHealth <= 0 :
            self.barn = []
            self.barnSlot = (-200, -200)
            for enemy in self.enemies:
                if isinstance (enemy, Ghost) :
                    enemy.stopTheEnemy = False
            self.noBarn = True
        
        
        if self.grassHealth <= 0 and self.fruitHealth <= 0 and self.barnHealth <= 0:
            self.gameOver = True
        
        
        
        if self.level < 5 or self.levelDisplay: #Doesn't increment various counters and create/move objects 
            
            return
        self.deleteEnemies()
        self.deleteWeapons()
        self.counter += 1
        self.weaponCounter += 1
        if self.counter % 1410 == 0: #Every 30 seconds, goes to next level
            self.firstStep = 0
            self.stopMoving = True
        
        noEnemyOnScreen = True
        
        if self.stopMoving:
            if self.firstStep == 0 :
                self.firstStep +=1
            elif self.firstStep == 1:
                self.counter -= 1
            for enemy in self.enemies:
                if enemy.x < self.width :
                    noEnemyOnScreen = False #False if there's still an enemy on the board
        
        if noEnemyOnScreen and self.stopMoving: #If there's no enemies on the screen and enemies aren't moving
            self.enemies = []
            self.level += 1
            self.stopMoving = False #Increment level and allow movement again
            self.levelDisplay = True
            if self.hasWeapon:
                for weapon in self.weapons: # Here
                    self.weapons.remove (weapon)
                    self.hasWeapon = False
                    
            self.makeVariousGrids()
          
            if self.hasAnimal:
               
                for animal in self.animals:
                    self.animals.remove(animal)
                    if isinstance (animal, Dog) :
                        self.money += self.dogPrice
                      
                    elif isinstance (animal, Goat) :
                        self.money += self.goatPrice
                       
                    elif isinstance (animal, Cow) :
                        self.money += self.cowPrice
                      
                    elif isinstance (animal, Alligator) :
                        self.money += self.alligatorPrice
                        
                    elif isinstance (animal, Gorilla) :
                        self.money += self.gorillaPrice
                    
                    else:
                        self.money += self.lionPrice
                    self.hasAnimal = False # Here
                    self.lionDamage = 0
                       
        if self.levelDisplay:
            self.hasEnemy = False
            return
        # Generates the first enemy of each level here
        if self.enemies == [] :
            if self.level == 5:
                self.enemies = pygame.sprite.Group(Monster(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.stepX, self.plantBlocks, self.grassSlot, self.direction, self.enemySpeed))
            elif self.level == 6:
                self.enemies = pygame.sprite.Group(Zombie(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.stepX, self.plantBlocks, self.grassSlot, self.direction, self.enemySpeed))
        
            elif self.level == 7:
                self.enemies = pygame.sprite.Group(Ghost(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.stepX, self.plantBlocks, self.grassSlot, self.direction, self.enemySpeed))
            else :
                whichEnemy = random.randint (1,3)
                if whichEnemy == 1:
                    self.enemies = pygame.sprite.Group(Monster(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.stepX, self.plantBlocks, self.grassSlot, self.direction, self.enemySpeed))
                elif whichEnemy == 2:
                    self.enemies = pygame.sprite.Group(Zombie(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.stepX, self.plantBlocks, self.grassSlot, self.direction, self.enemySpeed))
                else:
                    self.enemies = pygame.sprite.Group(Ghost(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.stepX, self.plantBlocks, self.grassSlot, self.direction, self.enemySpeed))
            self.counter += 1
            self.hasEnemy = True
                    
        
        if self.level == 5 or self.level == 6 or self.level == 7:
            if self.counter % 141 == 0 and not self.stopMoving: #Every 3 seconds generates an enemy
                y = random.randint (0, 7)
                if self.level == 5:
                    self.enemies.add (pygame.sprite.Group(Monster(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.stepX, self.plantBlocks, self.grassSlot, self.direction, self.enemySpeed))) 
                elif self.level == 6:
                    self.enemies.add (pygame.sprite.Group(Zombie(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.stepX, self.plantBlocks, self.grassSlot, self.direction, self.enemySpeed)))
                        
                elif self.level == 7:
                    self.enemies.add (pygame.sprite.Group(Ghost(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.stepX, self.plantBlocks, self.grassSlot, self.direction, self.enemySpeed)))
            
        else :
            if self.counter % self.timeIndex == 0 and not self.stopMoving:
                    whichEnemy = random.randint (1,3)
                    if whichEnemy == 1:
                        self.enemies.add(pygame.sprite.Group(Monster(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.stepX, self.plantBlocks, self.grassSlot, self.direction, self.enemySpeed)))
                    elif whichEnemy == 2:
                        self.enemies.add(pygame.sprite.Group(Zombie(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.stepX, self.plantBlocks, self.grassSlot, self.direction, self.enemySpeed)))
                    else:
                        self.enemies.add(pygame.sprite.Group(Ghost(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.stepX, self.plantBlocks, self.grassSlot,self.direction, self.enemySpeed)))
                    
                    
              
      
        self.enemies.update(self.width, self.height)
        
        if self.hasAnimal :
            for animal in self.animals:
                if isinstance (animal, Lion) :
                    animal.update()
        
        if self.hasAnimal and self.weaponCounter % 47 == 0:
            for animal in self.animals:
                if isinstance (animal, Lion) :
                    continue
                else :
                    if self.hasWeapon == False :
                        self.createInitialWeapons(animal)
                        self.hasWeapon = True
                    else: 
                        self.createLaterWeapons (animal)
                
        if self.hasWeapon:
            self.weapons.update ()
        self.updateCollisions() 
        
        if self.tempCounter % 47 == 0:
            if self.pownage == True:
                self.pownage = False
            self.damage = None
            
        
        if self.tempCounter % 100 == 0 :
            if not self.lionCollision:
                self.lionDamage = 0
            
        
# Helper function for creating later weapons

    def createLaterWeapons (self, animal) :
        if isinstance (animal, Dog) :
            self.weapons.add(pygame.sprite.Group(Bone(animal.x, animal.y, 3, 0)))
            self.weapons.add (pygame.sprite.Group(Bone(animal.x, animal.y, -3, 0)))
            self.weapons.add (pygame.sprite.Group(Bone(animal.x, animal.y, 0, 3)))
            self.weapons.add (pygame.sprite.Group(Bone(animal.x, animal.y, 0, -3)))
        elif isinstance (animal, Goat) :
            self.weapons.add (pygame.sprite.Group(Horn(animal.x, animal.y, 3, 0)))
            self.weapons.add (pygame.sprite.Group(Horn(animal.x, animal.y, -3, 0)))
            self.weapons.add (pygame.sprite.Group(Horn(animal.x, animal.y, 0, 3)))
            self.weapons.add (pygame.sprite.Group(Horn(animal.x, animal.y, 0, -3))) 
        elif isinstance (animal, Cow) :
            self.weapons.add (pygame.sprite.Group(Milk(animal.x, animal.y, 2.5, 0)))
            self.weapons.add (pygame.sprite.Group(Milk(animal.x, animal.y, -2.5, 0)))
            self.weapons.add (pygame.sprite.Group(Milk(animal.x, animal.y, 0, 2.5)))
            self.weapons.add (pygame.sprite.Group(Milk(animal.x, animal.y, 0, -2.5))) 
        elif isinstance (animal, Alligator) :
            self.weapons.add (pygame.sprite.Group(Water(animal.x, animal.y, 3, 3)))
            self.weapons.add (pygame.sprite.Group(Water(animal.x, animal.y, -3, -3)))
            self.weapons.add (pygame.sprite.Group(Water(animal.x, animal.y, 3, -3)))
            self.weapons.add (pygame.sprite.Group(Water(animal.x, animal.y, -3, 3))) 
        elif isinstance (animal, Gorilla) :
            self.weapons.add (pygame.sprite.Group(Banana(animal.x, animal.y, 3, 3)))
            self.weapons.add (pygame.sprite.Group(Banana(animal.x, animal.y, -3, -3)))
            self.weapons.add (pygame.sprite.Group(Banana(animal.x, animal.y, -3, 3)))
            self.weapons.add (pygame.sprite.Group(Banana(animal.x, animal.y, 3, -3)))
            self.weapons.add (pygame.sprite.Group(Banana(animal.x, animal.y, 0, -3)))
            self.weapons.add (pygame.sprite.Group(Banana(animal.x, animal.y, 0, 3)))
            self.weapons.add (pygame.sprite.Group(Banana(animal.x, animal.y, 3, 0))) 
            self.weapons.add (pygame.sprite.Group(Banana(animal.x, animal.y, -3, 0)))
        # else :
        #     self.moveLion (animal)
    
# Helper function for creating initial weapons

    def createInitialWeapons (self, animal) :
        if isinstance (animal, Dog) :
            self.weapons = pygame.sprite.Group(Bone(animal.x, animal.y, 3, 0))
            self.weapons.add (pygame.sprite.Group(Bone(animal.x, animal.y, -3, 0)))
            self.weapons.add (pygame.sprite.Group(Bone(animal.x, animal.y, 0, 3)))
            self.weapons.add (pygame.sprite.Group(Bone(animal.x, animal.y, 0, -3)))
        elif isinstance (animal, Goat) :
            self.weapons = pygame.sprite.Group(Horn(animal.x, animal.y, 3, 0))
            self.weapons.add (pygame.sprite.Group(Horn(animal.x, animal.y, -3, 0)))
            self.weapons.add (pygame.sprite.Group(Horn(animal.x, animal.y, 0, 3)))
            self.weapons.add (pygame.sprite.Group(Horn(animal.x, animal.y, 0, -3))) 
        elif isinstance (animal, Cow) :
            self.weapons = pygame.sprite.Group(Milk(animal.x, animal.y, 2.5, 0))
            self.weapons.add (pygame.sprite.Group(Milk(animal.x, animal.y, -2.5, 0)))
            self.weapons.add (pygame.sprite.Group(Milk(animal.x, animal.y, 0, 2.5)))
            self.weapons.add (pygame.sprite.Group(Milk(animal.x, animal.y, 0, -2.5))) 
        elif isinstance (animal, Alligator) :
            self.weapons = pygame.sprite.Group(Water(animal.x, animal.y, 3, 3))
            self.weapons.add (pygame.sprite.Group(Water(animal.x, animal.y, -3, 3)))
            self.weapons.add (pygame.sprite.Group(Water(animal.x, animal.y, -3, -3)))
            self.weapons.add (pygame.sprite.Group(Water(animal.x, animal.y, 3, -3))) 
        elif isinstance (animal, Gorilla) :
            self.weapons = pygame.sprite.Group(Banana(animal.x, animal.y, 3, 3))
            self.weapons.add (pygame.sprite.Group(Banana(animal.x, animal.y, -3, -3)))
            self.weapons.add (pygame.sprite.Group(Banana(animal.x, animal.y, -3, 3)))
            self.weapons.add (pygame.sprite.Group(Banana(animal.x, animal.y, 3, -3)))
            self.weapons.add (pygame.sprite.Group(Banana(animal.x, animal.y, 0, -3)))
            self.weapons.add (pygame.sprite.Group(Banana(animal.x, animal.y, 0, 3)))
            self.weapons.add (pygame.sprite.Group(Banana(animal.x, animal.y, 3, 0))) 
            self.weapons.add (pygame.sprite.Group(Banana(animal.x, animal.y, -3, 0)))
        # else :
        #     self.moveLion (animal, 
    
    
# Helper function that checks for collisions and updates the health/existence
# of the enemies

    def updateCollisions (self) :

        for weapon in self.weapons:
            for enemy in self.enemies:
                if pygame.sprite.collide_mask (weapon, enemy) :
                    enemy.health -= weapon.damage
                    self.damage = weapon.damage
                    self.randomVariable += 1
                 
                    
                    
                    if isinstance (weapon, Bone) :
                        self.typeDisplay = "bone"
                    elif isinstance (weapon, Horn) :
                        self.typeDisplay = "horn" 
                    elif isinstance (weapon, Milk) :
                        self.typeDisplay = "milk"
                    elif isinstance (weapon, Water) :
                        self.typeDisplay = "water"
                    elif isinstance (weapon, Banana) :
                        self.typeDisplay = "banana"
                    
                    
                    
                    
                    self.weapons.remove (weapon)
                    if enemy.health <= 0:
                        self.pownage = True
                        self.enemies.remove (enemy)
                        if enemy.stopTheEnemy:
                            
                            if isinstance (enemy, Monster) :
                                self.enemiesEatingGrass.remove (enemy)
                                self.grassLength -= 1
                            elif isinstance (enemy, Zombie) :
                                self.enemiesEatingFruit.remove (enemy)
                                self.fruitLength -= 1
                              
                            elif isinstance (enemy, Ghost) :
                                self.enemiesEatingBarn.remove (enemy)
                                self.barnLength -= 1
                        if isinstance (enemy, Monster) :
                            self.money += 1 #Added to amount of money for every monster killed
                
                        elif isinstance (enemy, Zombie) :
                            self.money += 5
                      
                        elif isinstance (enemy, Ghost) :
                            self.money += 10
        
        self.lionCollision = False
        if self.hasAnimal:
            for animal in self.animals:
                    if isinstance (animal, Lion) :
                        for enemy in self.enemies:
                            if pygame.sprite.collide_mask (enemy, animal) :
                                self.LionCollision = True
                                enemy.health -= animal.damage
                                self.lionDamage += animal.damage 
                                if enemy.health <= 0:
                                    self.pownage = True
                                    self.enemies.remove (enemy)
                                    if enemy.stopTheEnemy:
                                        if isinstance (enemy, Monster) :
                                            self.grassLength -= 1
                                        elif isinstance (enemy, Zombie) :
                                            self.fruitLength -= 1
                                        elif isinstance (enemy, Ghost) :
                                            self.barnLength -= 1
                                    if isinstance (enemy, Monster) :
                                        self.money += 1 #Added to amount of money for every monster killed
                                    elif isinstance (enemy, Zombie) :
                                        self.money += 5
                                    elif isinstance (enemy, Ghost) :
                                        self.money += 10
        if not self.lionCollision:
            self.lionCollision = 0
        
            
            
        for enemy in self.enemies:
            for grass in self.grass:
                if isinstance (enemy, Monster) :
                    if pygame.sprite.collide_mask (enemy, grass) :
                       
                        enemy.stopTheEnemy = True
                        if self.enemiesEatingGrass == [] :
                            self.enemiesEatingGrass = pygame.sprite.Group(enemy) 
                            self.firstGrass = True
                            self.grassLength += 1
                            self.tempTempGrass = [enemy]
                        elif self.firstGrass and not (enemy in self.tempTempGrass) : #and not (self.enemiesEatingGrass == pygame.sprite.Group(enemy)):
                            self.enemiesEatingGrass.add (enemy)
                            self.grassLength += 1
                            self.firstGrass = False
                        elif not self.firstGrass and enemy not in self.enemiesEatingGrass:
                            self.enemiesEatingGrass.add (enemy)
                            self.grassLength +=1
                            
                        
                        
                
            for fruit in self.fruit:
                if isinstance (enemy, Zombie) :
                    if pygame.sprite.collide_mask (enemy, fruit) :
                        
                        enemy.stopTheEnemy = True
                        if self.enemiesEatingFruit == [] :
                            self.enemiesEatingFruit = pygame.sprite.Group(enemy) 
                            self.firstFruit = True
                            self.fruitLength += 1
                            self.tempTempFruit = [enemy]
                        elif self.firstFruit and not (enemy in self.tempTempFruit) : #and not (self.enemiesEatingGrass == pygame.sprite.Group(enemy)):
                            self.enemiesEatingFruit.add (enemy)
                            self.fruitLength += 1
                            self.firstFruit = False
                        elif not self.firstFruit and enemy not in self.enemiesEatingFruit:
                            self.enemiesEatingFruit.add (enemy)
                            self.fruitLength +=1
            
            for barn in self.barn:
                if isinstance (enemy, Ghost) :
                    if pygame.sprite.collide_mask (enemy, barn) :
                        enemy.stopTheEnemy = True
                        if self.enemiesEatingBarn == [] :
                            self.enemiesEatingBarn = pygame.sprite.Group(enemy) 
                            self.firstBarn = True
                            self.barnLength += 1
                            self.tempTempBarn = [enemy]
                        elif self.firstBarn and not (enemy in self.tempTempBarn) : #and not (self.enemiesEatingGrass == pygame.sprite.Group(enemy)):
                            self.enemiesEatingBarn.add (enemy)
                            self.barnLength += 1
                            self.firstBarn = False
                        elif not self.firstBarn  and enemy not in self.enemiesEatingBarn:
                            self.enemiesEatingBarn.add (enemy)
                            self.barnLength +=1

    def getFirstPlantBlocks (self) :
        return [[[(10, 10), (82, 65)], [(82, 10), (154, 65)], [(82, 65), (154, 120)], [(82, 120), (154, 175)], [(82, 175), (154, 230)], [(10, 175), (82, 230)], [(10, 230), (82, 285)], [(10, 285), (82,         340)], [(10, 340), (82, 395)], [(82, 340), (154, 395)], [(154, 340), (226, 395)], [(154, 395), (226, 450)], [(226, 395), (298, 450)], [(298, 395), (370, 450)], [(298, 340), (370, 395)], [(370, 340), (442, 395)], [(370, 285), (442, 340)], [(370, 230), (442, 285)], [(298, 230), (370, 285)], [(226, 230), (298, 285)], [(226, 175), (298, 230)], [(226, 120), (298, 175)], [(298, 120), (370, 175)], [(298, 65), (370, 120)], [(370, 65), (442, 120)], [(370, 10), (442, 65)], [(442, 10), (514, 65)], [(514, 10), (586, 65)]], [[(10, 10), (82, 65)], [(10, 65), (82, 120)], [(10, 120), (82, 175)], [(82, 120), (154, 175)], [(82, 175), (154, 230)], [(82, 230), (154, 285)], [(10, 230), (82, 285)], [(10, 285), (82, 340)], [(10, 340), (82, 395)], [(10, 395), (82, 450)], [(82, 395), (154, 450)], [(154, 395), (226, 450)], [(154, 340), (226, 395)], [(226, 340), (298, 395)], [(226, 285), (298, 340)], [(226, 230), (298, 285)], [(298, 230), (370, 285)], [(370, 230), (442, 285)], [(442, 230), (514, 285)], [(514, 230), (586, 285)]], [[(10, 10), (82, 65)], [(10, 65), (82, 120)], [(82, 65), (154, 120)], [(82, 120), (154, 175)], [(154, 120), (226, 175)], [(226, 120), (298, 175)], [(226, 65), (298, 120)], [(298, 65), (370, 120)], [(370, 65), (442, 120)], [(442, 65), (514, 120)], [(442, 120), (514, 175)], [(442, 175), (514, 230)], [(370, 175), (442, 230)], [(298, 175), (370, 230)], [(298, 230), (370, 285)], [(226, 230), (298, 285)], [(154, 230), (226, 285)], [(82, 230), (154, 285)], [(10, 230), (82, 285)], [(10, 285), (82, 340)], [(10, 340), (82, 395)], [(82, 340), (154, 395)], [(82, 395), (154, 450)], [(154, 395), (226, 450)], [(226, 395), (298, 450)], [(298, 395), (370, 450)], [(298, 340), (370, 395)], [(370, 340), (442, 395)], [(442, 340), (514, 395)], [(514, 340), (586, 395)]], [[(10, 10), (82, 65)], [(82, 10), (154, 65)], [(82, 65), (154, 120)], [(82, 120), (154, 175)], [(82, 175), (154, 230)], [(10, 175), (82, 230)], [(10, 230), (82, 285)], [(10, 285), (82, 340)], [(10, 340), (82, 395)], [(82, 340), (154, 395)], [(82, 395), (154, 450)], [(154, 395), (226, 450)], [(226, 395), (298, 450)], [(298, 395), (370, 450)], [(370, 395), (442, 450)], [(442, 395), (514, 450)], [(514, 395), (586, 450)]], [[(10, 10), (82, 65)], [(82, 10), (154, 65)], [(82, 65), (154, 120)], [(82, 120), (154, 175)], [(10, 120), (82, 175)], [(10, 175), (82, 230)], [(10, 230), (82, 285)], [(10, 285), (82, 340)], [(82, 285), (154, 340)], [(82, 340), (154, 395)], [(154, 340), (226, 395)], [(226, 340), (298, 395)], [(226, 395), (298, 450)], [(298, 395), (370, 450)], [(370, 395), (442, 450)], [(442, 395), (514, 450)], [(514, 395), (586, 450)]], [[(10, 10), (82, 65)], [(10, 65), (82, 120)], [(10, 120), (82, 175)], [(10, 175), (82, 230)], [(10, 230), (82, 285)], [(82, 230), (154, 285)], [(82, 285), (154, 340)], [(82, 340), (154, 395)], [(154, 340), (226, 395)], [(154, 395), (226, 450)], [(226, 395), (298, 450)], [(298, 395), (370, 450)], [(298, 340), (370, 395)], [(298, 285), (370, 340)], [(226, 285), (298, 340)], [(226, 230), (298, 285)], [(226, 175), (298, 230)], [(154, 175), (226, 230)], [(154, 120), (226, 175)], [(154, 65), (226, 120)], [(226, 65), (298, 120)], [(226, 10), (298, 65)], [(298, 10), (370, 65)], [(370, 10), (442, 65)], [(442, 10), (514, 65)], [(514, 10), (586, 65)]], [[(10, 10), (82, 65)], [(10, 65), (82, 120)], [(82, 65), (154, 120)], [(154, 65), (226, 120)], [(154, 120), (226, 175)], [(154, 175), (226, 230)], [(82, 175), (154, 230)], [(10, 175), (82, 230)], [(10, 230), (82, 285)], [(10, 285), (82, 340)], [(82, 285), (154, 340)], [(154, 285), (226, 340)], [(154, 340), (226, 395)], [(154, 395), (226, 450)], [(226, 395), (298, 450)], [(298, 395), (370, 450)], [(370, 395), (442, 450)], [(370, 340), (442, 395)], [(370, 285), (442, 340)], [(370, 230), (442, 285)], [(442, 230), (514, 285)], [(442, 175), (514, 230)], [(514, 175), (586, 230)]], [[(10, 10), (82, 65)], [(82, 10), (154, 65)], [(82, 65), (154, 120)], [(82, 120), (154, 175)], [(82, 175), (154, 230)], [(82, 230), (154, 285)], [(82, 285), (154, 340)], [(82, 340), (154, 395)], [(154, 340), (226, 395)], [(154, 395), (226, 450)], [(226, 395), (298, 450)], [(298, 395), (370, 450)], [(298, 340), (370, 395)], [(370, 340), (442, 395)], [(370, 285), (442, 340)], [(442, 285), (514, 340)], [(514, 285), (586, 340)]], [[(10, 10), (82, 65)], [(10, 65), (82, 120)], [(10, 120), (82, 175)], [(82, 120), (154, 175)], [(154, 120), (226, 175)], [(226, 120), (298, 175)], [(226, 175), (298, 230)], [(226, 230), (298, 285)], [(154, 230), (226, 285)], [(82, 230), (154, 285)], [(82, 285), (154, 340)], [(82, 340), (154, 395)], [(82, 395), (154, 450)], [(154, 395), (226, 450)], [(226, 395), (298, 450)], [(298, 395), (370, 450)], [(298, 340), (370, 395)], [(298, 285), (370, 340)], [(370, 285), (442, 340)], [(442, 285), (514, 340)], [(442, 230), (514, 285)], [(514, 230), (586, 285)]], [[(10, 10), (82, 65)], [(10, 65), (82, 120)], [(10, 120), (82, 175)], [(82, 120), (154, 175)], [(82, 175), (154, 230)], [(154, 175), (226, 230)], [(226, 175), (298, 230)], [(298, 175), (370, 230)], [(298, 230), (370, 285)], [(298, 285), (370, 340)], [(226, 285), (298, 340)], [(154, 285), (226, 340)], [(154, 340), (226, 395)], [(154, 395), (226, 450)], [(226, 395), (298, 450)], [(298, 395), (370, 450)], [(370, 395), (442, 450)], [(370, 340), (442, 395)], [(442, 340), (514, 395)], [(442, 285), (514, 340)], [(442, 230), (514, 285)], [(442, 175), (514, 230)], [(514, 175), (586, 230)]]]




# Helper function that displays introduction screen

    def createInitialScreen (self, screen) :
        screen.fill (self.lightSalmon)
        pygame.font.init() 
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render("Welcome to Animal Survival!", False, (0,0,0))
        screen.blit(textsurface,(100, self.height/2 - 100))
        
        textsurface2 = myfont.render("Click the 'Go!' Button to Begin!", False, (0,0,0))
        screen.blit (textsurface2, (100, self.height/2))
        pygame.draw.polygon (screen, (102, 255, 102), [(self.width/2 - 75, self.height/2 + 100), (self.width/2 + 75, self.height/2 + 100), (self.width/2 + 75, self.height/2 + 200), (self.width/2 - 75, self.height/2 + 200)], 0)
        
        myfont = pygame.font.SysFont ('Comic Sans MS', 50)
        textsurface3 = myfont.render ("Go!", False, (0,0,0))
        screen.blit (textsurface3, (self.width/2 - 32, self.height/2 + 107))
        
    
# Helper function that displays game over screen

    def gameOverScreen (self, screen) :
        screen.fill (self.black) 
        pygame.font.init() 
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render("Game Over!", False, (255,255,255))
        screen.blit(textsurface,(self.width/2 - 70, self.height/2 - 100))
        
        textsurface2 = myfont.render ("Press Spacebar to Try Again", False, (255, 255, 255))
        screen.blit (textsurface2, (self.width/2 - 170, self.height/2 + 100))



# Helper functions that displays tutorial screens

    def createFirstScreen (self, screen) :
        screen.fill (self.lightBlue)
        myfont = pygame.font.SysFont ('Comic Sans MS', 30)
        intro = myfont.render ("Monsters, Zombies, and Ghosts", False, (0,0,0))
        screen.blit (intro, (self.width/2 - 200, self.height/2 - 200))
        intro2 = myfont.render ("Have Taken Over the Planet!", False, (0,0,0))
        screen.blit (intro2, (self.width/2 - 180, self.height/2 - 130))
        
        
        myfont = pygame.font.SysFont ('Comic Sans MS', 22)
        intro3 = myfont.render ("Press Spacebar to Continue", False, (self.purple))
        screen.blit (intro3, (self.width/2 - 130, self.height/2 + 250))
        
        earthImage = pygame.sprite.Group (Earth (300, 350))
        earthImage.draw (screen)
        
        
        
    def createSecondScreen (self, screen) :
        screen.fill (self.lightBlue) 
        myfont = pygame.font.SysFont ('Comic Sans MS', 22)
        intro = myfont.render ("Monsters Are the Weakest Enemies. They Consume Grass.", False, (0,0,0))
        intro2 = myfont.render ("Zombies Are Slightly Stronger. They Consume Fruit.", False, (0,0,0))
        intro3 = myfont.render ("Ghosts Are the Strongest Enemy. They Haunt the Barn.", False, (0,0,0))
        intro4 = myfont.render ("Press Spacebar to Continue", False, (self.purple))
        
        
        
        
        screen.blit (intro4, (self.width/2 - 130, self.height/2 + 270))
        
        screen.blit (intro, (self.width/2 - 300, self.height/2 - 250))
        screen.blit (intro2, (self.width/2 - 260, self.height/2-50))
        screen.blit (intro3, (self.width/2 - 285, self.height/2 + 150))
        
        self.displayEnemies = pygame.sprite.Group(Monster(200, 125,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.stepX, self.plantBlocks, self.grassSlot, self.direction, self.enemySpeed))
                        
        self.displayEnemies.add (Zombie(200, 325,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.stepX, self.plantBlocks, self.grassSlot, self.direction, self.enemySpeed))
        
        self.displayEnemies.add (Ghost(200, 525,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.stepX, self.plantBlocks, self.grassSlot, self.direction, self.enemySpeed))
                        
        self.displayEnemies.add ((Grass (400, 125)))
        self.displayEnemies.add ((Barn (400, 525)))
        self.displayEnemies.add ((Fruit (400, 325)))
                        
                        
        
        self.displayEnemies.draw (screen)
        
        
    
    def createThirdScreen (self, screen) :
        screen.fill (self.lightBlue) 
        myfont = pygame.font.SysFont ('Comic Sans MS', 22)
        intro = myfont.render ("Six Species of Animals Remain to Save the World", False, (0,0,0))
        intro2 = myfont.render ("and Protect These Three Vital Sources!", False, (0,0,0))
        intro3 = myfont.render ("Every Animal's Weapon Varies in Power and Speed", False, (0,0,0))
        intro4 = myfont.render ("Press Spacebar to Continue", False, (self.purple))
        screen.blit (intro4, (self.width/2 - 130, self.height/2 + 250))
        
        screen.blit (intro, (45, 100))
        screen.blit (intro2, (100, 150))
        screen.blit (intro3, (45, 230))
        
        
        
        intro5 = myfont.render ("Damage: 1/10", False, (255,0,0))
        intro6 = myfont.render ("Speed: 5/10", False, (0,0,102))
        
        intro7 = myfont.render ("Damage: 3/10", False, (255,0,0))
        intro8 = myfont.render ("Speed: 5/10", False, (0,0,102))
        
        intro9 = myfont.render ("Damage: 5/10", False, (255,0,0))
        intro10 = myfont.render ("Speed: 4/10", False, (0,0,102))
        
        intro11 = myfont.render ("Damage: 7/10", False, (255,0,0))
        intro12 = myfont.render ("Speed: 7/10", False, (0,0,102))
        
        intro13 = myfont.render ("Damage: 9/10", False, (255,0,0))
        intro14 = myfont.render ("Speed: 7/10", False, (0,0,102))
        
        intro15 = myfont.render ("Damage: 10/10", False, (255,0,0))
        intro16 = myfont.render ("Speed: 10/10", False, (0,0,102))
        
        self.tutorialAnimals = pygame.sprite.Group(Dog(6 * self.firstMargin + 15, self.height - 0.75 * self.endMargin - 100))
        self.tutorialAnimals.add ((Bone (6 * self.firstMargin + 60 + 15, self.height - 0.75 * self.endMargin - 100, 0, 0)))
        screen.blit (intro5, (6 * self.firstMargin -35, self.height - 0.75 * self.endMargin - 100 - 90))
        screen.blit (intro6, (6 * self.firstMargin-35, self.height - 0.75 * self.endMargin - 100 - 60))
        
        self.tutorialAnimals.add ((Goat (24 * self.firstMargin + 15, self.height - 0.75 * self.endMargin - 100)))
        self.tutorialAnimals.add ((Horn (24 * self.firstMargin + 60 + 15, self.height - 0.75 * self.endMargin - 100, 0, 0)))
        screen.blit (intro7, (24 * self.firstMargin-35, self.height - 0.75 * self.endMargin - 100 - 90))
        screen.blit (intro8, (24 * self.firstMargin-35, self.height - 0.75 * self.endMargin - 100 - 60))
        
        
        self.tutorialAnimals.add ((Cow (42 * self.firstMargin + 15, self.height - 0.75 * self.endMargin - 100)))
        self.tutorialAnimals.add ((Milk (42 * self.firstMargin + 60 + 15, self.height - 0.75 * self.endMargin - 100, 0, 0)))
        screen.blit (intro9, (42 * self.firstMargin-35, self.height - 0.75 * self.endMargin - 100 - 90))
        screen.blit (intro10, (42 * self.firstMargin-35  , self.height - 0.75 * self.endMargin - 100 - 60))
        
        
        self.tutorialAnimals.add ((Alligator (6 * self.firstMargin + 15, self.height - 0.2 * self.endMargin - 50)))
        self.tutorialAnimals.add ((Water (6 * self.firstMargin + 60 + 15, self.height - 0.2 * self.endMargin - 50, 0, 0)))
        screen.blit (intro11, (6 * self.firstMargin-35, self.height - 0.2 * self.endMargin - 50 - 90))
        screen.blit (intro12, (6 * self.firstMargin-35, self.height - 0.2 * self.endMargin - 50 - 60))
        
        self.tutorialAnimals.add ((Gorilla (24 * self.firstMargin + 15, self.height - 0.2 * self.endMargin - 50)))
        self.tutorialAnimals.add ((Banana (24 * self.firstMargin + 60 + 15, self.height - 0.2 * self.endMargin - 50, 0, 0)))
        screen.blit (intro13, (24 * self.firstMargin-35, self.height - 0.2 * self.endMargin - 50 - 90 ))
        screen.blit (intro14, (24 * self.firstMargin-35, self.height - 0.2 * self.endMargin - 50 - 60 ))
        
        self.tutorialAnimals.add ((Lion (42 * self.firstMargin + 15, self.height - 0.2 * self.endMargin - 50)))
        screen.blit (intro15, (42 * self.firstMargin-35, self.height - 0.2 * self.endMargin - 50 - 90))
        screen.blit (intro16, (42 * self.firstMargin-35, self.height - 0.2 * self.endMargin - 50 - 60))
    
        self.tutorialAnimals.draw (screen)
    
    def createFourthScreen (self, screen) :
        screen.fill (self.lightBlue) 
        myfont = pygame.font.SysFont ('Comic Sans MS', 22)
        intro = myfont.render ("Every Time You Kill an Enemy, You Get Coins Based on", False, (0,0,0))
        intro2 = myfont.render ("the Strength of the Enemy.", False, (0,0,0))
        intro3 = myfont.render ('Use Coins to Buy Animals!', False, (0,0,0))
        intro4 = myfont.render ('Ready?', False, (0,204,0))
        intro6 = myfont.render ("Press Spacebar to Start", False, (self.purple))
        screen.blit (intro6, (self.width/2 - 130, self.height/2 + 250))
        
        
        
        screen.blit (intro, (30, 50))
        screen.blit (intro2, (170, 100))
        screen.blit (intro3, (170, 200))
        screen.blit (intro4, (260, 450))
  

        self.displayAnimals = pygame.sprite.Group(Dog(6 * self.firstMargin+ 30, self.height - 0.75 * self.endMargin - 200))
        self.displayAnimals.add (pygame.sprite.Group (SmallCoin (6 * self.firstMargin + 60 + 30, self.height - 0.75 * self.endMargin- 200)))
        
        self.displayAnimals.add (pygame.sprite.Group (Goat (24 * self.firstMargin+ 30, self.height - 0.75 * self.endMargin- 200)))
        self.displayAnimals.add (pygame.sprite.Group (SmallCoin (24 * self.firstMargin + 60+ 30, self.height - 0.75 * self.endMargin- 200)))
        
        self.displayAnimals.add (pygame.sprite.Group (Cow (42 * self.firstMargin+ 30, self.height - 0.75 * self.endMargin- 200)))
        self.displayAnimals.add (pygame.sprite.Group (SmallCoin (42 * self.firstMargin + 60+ 30, self.height - 0.75 * self.endMargin- 200)))
        
        self.displayAnimals.add (pygame.sprite.Group (Alligator (6 * self.firstMargin+ 30, self.height - 0.2 * self.endMargin- 200)))
        self.displayAnimals.add (pygame.sprite.Group (SmallCoin (6 * self.firstMargin + 60+ 30, self.height - 0.2 * self.endMargin- 200)))
        
        self.displayAnimals.add (pygame.sprite.Group (Gorilla (24 * self.firstMargin+ 30, self.height - 0.2 * self.endMargin- 200)))
        self.displayAnimals.add (pygame.sprite.Group (SmallCoin (24 * self.firstMargin + 60+ 30, self.height - 0.2 * self.endMargin- 200)))
        
        self.displayAnimals.add (pygame.sprite.Group (Lion (42 * self.firstMargin+ 30, self.height - 0.2 * self.endMargin- 200)))
        self.displayAnimals.add (pygame.sprite.Group (SmallCoin (42 * self.firstMargin + 60+ 30, self.height - 0.2 * self.endMargin- 200)))

        self.displayAnimals.draw (screen)
        
        dog = myfont.render(str (self.dogPrice), False, (0, 0, 0))
        screen.blit(dog,(6 * self.firstMargin + 60 - 8 + 30, self.height - 0.75 * self.endMargin - 17 - 200))
        
        goat = myfont.render (str (self.goatPrice), False, (0,0,0))
        screen.blit (goat, (24 * self.firstMargin + 60 -15+ 30, self.height - 0.75 * self.endMargin -17- 200))
        
        cow = myfont.render (str (self.cowPrice), False, (0,0,0)) 
        screen.blit (cow, (42 * self.firstMargin + 60 - 15+ 30, self.height - 0.75 * self.endMargin - 17- 200))
        
        alligator = myfont.render (str (self.alligatorPrice), False, (0,0,0))
        screen.blit (alligator, (6 * self.firstMargin + 60-15+ 30, self.height - 0.2 * self.endMargin-17- 200))
        
        gorilla = myfont.render (str (self.gorillaPrice), False, (0,0,0))
        screen.blit (gorilla, (24 * self.firstMargin + 60-22+ 30, self.height - 0.2 * self.endMargin-17- 200))
        
        lion = myfont.render (str (self.lionPrice), False, (0,0,0))
        screen.blit (lion, (42 * self.firstMargin + 60-22+ 30, self.height - 0.2 * self.endMargin-17- 200))
        

# Function that displays next level 

    def displayNextLevel (self, screen) :
        screen.fill (self.black) 
        # pygame.font.init() 
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render("Welcome to Level " + str (self.level-3) + "!", False, (255,255,255))
        screen.blit(textsurface,(self.width/2 - 135, self.height/2 - 100))
        
        textsurface2 = myfont.render ("Press Space Bar to Continue", False, (255, 255, 255))
        screen.blit (textsurface2, (self.width/2 - 170, self.height/2 + 100))
        
        
# Keypressed function to switch between levels

    def keyPressed(self, keyCode, modifier):
       
        if keyCode == 32: #This is the value associated with the space bar
            if self.level == 1 or self.level == 2 or self.level == 3 or self.level == 4:
                self.level += 1
            if self.levelDisplay:
                self.levelDisplay = False
                self.weaponCounter -= 1
                if self.levelDisplay > 7 :
                    self.timeIndex -= 10
                    self.enemySpeed += 0.1
            
            elif self.gameOver :
                self.gameOver = False
                self.init() 
                
            
                
# View function that first generates grid and then the monsters
    def redrawAll(self, screen):
        
        if self.gameOver:
            self.gameOverScreen (screen)
            return
        
        if self.level == 0:
            self.createInitialScreen (screen)
            return
            
        if self.levelDisplay:
            self.displayNextLevel(screen)
            return
            
            
        if self.level == 1:
            self.createFirstScreen (screen) 
            return
        elif self.level == 2:
            self.createSecondScreen (screen)
            return
        elif self.level == 3:
            self.createThirdScreen (screen)
            return
        
        elif self.level == 4:
            self.createFourthScreen (screen)
            return
        
        screen.fill(self.lightPurple)
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
                                                    
        
        
        
        if not self.noGrass:
            self.grass.draw (screen)
        if not self.noFruit :
            self.fruit.draw (screen)
        if not self.noBarn :
            self.barn.draw (screen)
          
        self.createAnimalDisplay (screen)
        self.createCoin(screen)
        if self.hasEnemy:    
            self.enemies.draw(screen)
        
        
# Helper function that creates coin in bottom right corner

    def createCoin (self, screen) :
     
        self.coin = pygame.sprite.Group(Coin(self.width - 5 * self.firstMargin,\
                                            self.height - 0.5 * self.endMargin))
        self.coin.draw (screen)
        # pygame.font.init() 
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(str (self.money), False, (0, 0, 0))
        length = len (str (self.money))
        screen.blit(textsurface,(self.width - (6 + 0.8 * (length - 1)) * self.firstMargin, \
                                self.height - 0.66 * self.endMargin))
                                
                                
           
        myfont = pygame.font.SysFont ('Comic Sans MS', 24)   
        
        dog = myfont.render(str (self.dogPrice), False, (0, 0, 0))
        screen.blit(dog,(6 * self.firstMargin + 60 - 8, self.height - 0.75 * self.endMargin - 17))
        
        
        
        goat = myfont.render (str (self.goatPrice), False, (0,0,0))
        screen.blit (goat, (24 * self.firstMargin + 60 -15, self.height - 0.75 * self.endMargin -17))
        
        cow = myfont.render (str (self.cowPrice), False, (0,0,0)) 
        screen.blit (cow, (42 * self.firstMargin + 60 - 15, self.height - 0.75 * self.endMargin - 17))
        
        alligator = myfont.render (str (self.alligatorPrice), False, (0,0,0))
        screen.blit (alligator, (6 * self.firstMargin + 60-15, self.height - 0.2 * self.endMargin-17))
        
        gorilla = myfont.render (str (self.gorillaPrice), False, (0,0,0))
        screen.blit (gorilla, (24 * self.firstMargin + 60-22, self.height - 0.2 * self.endMargin-17))
        
        lion = myfont.render (str (self.lionPrice), False, (0,0,0))
        screen.blit (lion, (42 * self.firstMargin + 60-22, self.height - 0.2 * self.endMargin-17))
        
    
        myfont = pygame.font.SysFont ("Comic Sans MS", 30) 
        myfont.set_bold (True)
        displayGrassHealth = myfont.render (str (math.ceil(self.grassHealth)), False, (0,0,204))
        screen.blit (displayGrassHealth, (self.grassSlot[0] + 12, self.grassSlot[1]))
        
        displayFruitHealth = myfont.render (str (math.ceil (self.fruitHealth)), False, (0,0,204))
        screen.blit (displayFruitHealth, (self.fruitSlot[0] + 17, self.fruitSlot[1]))
        
        displayBarnHealth = myfont.render (str (math.ceil (self.barnHealth)), False, (0,0,204))
        screen.blit (displayBarnHealth, (self.barnSlot[0] + 17, self.barnSlot[1] + 22))
       
       
        if self.damage == None or self.damage == 0 :
            if self.lionDamage == None or self.lionDamage == 0:
                return
        
      
        
        if not self.damage == None and not self.damage == 0:
            damage = myfont.render ( str (self.damage), False, (255,0,0))
        
            if self.typeDisplay == "bone":
                screen.blit (damage, (6 * self.firstMargin + 60 - 40, self.height - 0.75 * self.endMargin -40)) 
            
            elif self.typeDisplay == "horn":
                screen.blit (damage, (24 * self.firstMargin + 60 -40, self.height - 0.75 * self.endMargin - 40))
            elif self.typeDisplay == "milk" :
                screen.blit (damage, (42 * self.firstMargin + 60 - 42, self.height - 0.75 * self.endMargin - 43))
            elif self.typeDisplay == "water" :
                screen.blit (damage, (6 * self.firstMargin + 60 - 44, self.height - 0.2 * self.endMargin-46))
            elif self.typeDisplay == "banana":
                screen.blit (damage, (24 * self.firstMargin + 60-47, self.height - 0.2 * self.endMargin-43))
            
                
            
        else :
            lionDamage = myfont.render (str (int(self.lionDamage)), False, (255,0,0))
            screen.blit (lionDamage, (42 * self.firstMargin + 60 - 42, self.height - 0.2 * self.endMargin - 50))
        
        if self.pownage:
            killedEnemy = myfont.render ("Annihilated", False, (0, 153,0))
            screen.blit (killedEnemy, (self.width/2 - 90, self.height * (6/7) - 15))

# Helper function that displays animals and prices at the bottom of the screen

    def createAnimalDisplay (self, screen) :
        self.displayAnimals = pygame.sprite.Group(Dog(6 * self.firstMargin, self.height - 0.75 * self.endMargin))
        self.displayAnimals.add (pygame.sprite.Group (SmallCoin (6 * self.firstMargin + 60, self.height - 0.75 * self.endMargin)))
        
        self.displayAnimals.add (pygame.sprite.Group (Goat (24 * self.firstMargin, self.height - 0.75 * self.endMargin)))
        self.displayAnimals.add (pygame.sprite.Group (SmallCoin (24 * self.firstMargin + 60, self.height - 0.75 * self.endMargin)))
        
        self.displayAnimals.add (pygame.sprite.Group (Cow (42 * self.firstMargin, self.height - 0.75 * self.endMargin)))
        self.displayAnimals.add (pygame.sprite.Group (SmallCoin (42 * self.firstMargin + 60, self.height - 0.75 * self.endMargin)))
        
        self.displayAnimals.add (pygame.sprite.Group (Alligator (6 * self.firstMargin, self.height - 0.2 * self.endMargin)))
        self.displayAnimals.add (pygame.sprite.Group (SmallCoin (6 * self.firstMargin + 60, self.height - 0.2 * self.endMargin)))
        
        self.displayAnimals.add (pygame.sprite.Group (Gorilla (24 * self.firstMargin, self.height - 0.2 * self.endMargin)))
        self.displayAnimals.add (pygame.sprite.Group (SmallCoin (24 * self.firstMargin + 60, self.height - 0.2 * self.endMargin)))
        
        self.displayAnimals.add (pygame.sprite.Group (Lion (42 * self.firstMargin, self.height - 0.2 * self.endMargin)))
        self.displayAnimals.add (pygame.sprite.Group (SmallCoin (42 * self.firstMargin + 60, self.height - 0.2 * self.endMargin)))

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

