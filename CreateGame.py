# Main game class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 11/20/18


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
        self.peach = (255, 229, 153)
        self.lightPink = (255, 204, 204)
        self.lightYellow = (250, 250, 210)
        self.turquoise = (64, 224, 208)
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
        self.enemies = pygame.sprite.Group(Monster(self.boxes[0][0][0] +  \
                        self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.plantBlocks)) 
        self.highlighted = (-1, -1)
        self.firstAnimal = True
        self.hasAnimal = False
        self.weapons = []
        self.hasWeapon = False
        self.money = 10
        self.chooseAnimal = True
        self.type = "dog"
        self.availableSlots = copy.deepcopy (self.boxes)
        self.tempSlots = copy.deepcopy (self.availableSlots)
        for row in range (len (self.availableSlots)):
            for col in self.availableSlots[row] :
                for plantRow in self.plantBlocks:
                    if col == plantRow[0]:
                        self.tempSlots[row].remove (col)
        self.availableSlots = self.tempSlots
        
        self.dogPrice = 5
        self.goatPrice = 10
        self.cowPrice = 20
        self.alligatorPrice =50
        self.gorillaPrice = 75
        self.lionPrice = 100
        self.level = 0
        self.stopMoving = False
        self.weaponCounter = 0
        self.levelDisplay = False
        
        
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
  

            

# Called approximately every 20 milliseconds and updates position of enemies

    def timerFired(self, dt):
        if self.level == 0:
            return
        self.counter += 1
        self.weaponCounter += 1
        if self.counter % 1410 == 0: #Every 30 seconds, goes to next level
            self.stopMoving = True
        
        noEnemyOnScreen = True
        
        if self.stopMoving:
            self.counter -= 1
            for enemy in self.enemies:
                if enemy.x < self.width :
                    noEnemyOnScreen = False #False if there's still an enemy on the board
        
        if noEnemyOnScreen and self.stopMoving: #If there's no enemies on the screen and enemies aren't moving
            self.enemies = []
            self.level += 1
            self.stopMoving = False #Increment level and allow movement again
            self.levelDisplay = True
        
        
        # Generates the first enemy of each level here
        if self.level == 1:
            if self.enemies == [] :
                self.enemies = pygame.sprite.Group(Monster(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.plantBlocks))
        elif self.level == 2:
            if self.enemies == [] :
                self.enemies = pygame.sprite.Group(Zombie(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.plantBlocks))
        
        elif self.level == 3:
            if self.enemies == [] :
                self.enemies = pygame.sprite.Group(Ghost(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.plantBlocks))
        
            
        if self.counter % 141 == 0 and not self.stopMoving: #Every 3 seconds generates an enemy
            y = random.randint (0, 7)
            if self.level == 1:
                self.enemies.add (pygame.sprite.Group(Monster(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.plantBlocks))) 
            elif self.level == 2:
                self.enemies.add (pygame.sprite.Group(Zombie(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.plantBlocks)))
                        
            elif self.level == 3:
                self.enemies.add (pygame.sprite.Group(Ghost(self.boxes[0][0][0]\
                        + self.stepX / 2, self.boxes[0][0][1] + self.stepY / 2,
                        self.numRows, self.numCols, self.firstMargin, self.width, 
                        self.height, self.stepY, self.plantBlocks)))
      
        self.enemies.update(self.width, self.height)
        
        
        if self.hasAnimal and self.weaponCounter % 47 == 0:
            for animal in self.animals:
                if self.hasWeapon == False :
                    self.createInitialWeapons(animal)
                    self.hasWeapon = True
                else: 
                    self.createLaterWeapons (animal)
        if self.hasWeapon:
            self.weapons.update ()
        self.updateCollisions() 

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
        else :
            self.moveLion (animal)
    
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
        else :
            self.moveLion (animal)
    
    
# Helper function that checks for collisions and updates the health/existence
# of the enemies

    def updateCollisions (self) :
        for weapon in self.weapons:
            for enemy in self.enemies:
                if pygame.sprite.collide_mask (weapon, enemy) :
                    enemy.health -= weapon.damage
                    self.weapons.remove (weapon)
                    if enemy.health <= 0:
                        self.enemies.remove (enemy)

    
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



# Function that displays next level 

    def displayNextLevel (self, screen) :
        print ("displaying level")
        screen.fill (self.black) 
        pygame.font.init() 
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render("Welcome to Level " + str (self.level) + "!", False, (255,255,255))
        screen.blit(textsurface,(100, self.height/2 - 100))
        
        

# View function that first generates grid and then the monsters
    def redrawAll(self, screen):
        if self.level == 0:
            self.createInitialScreen (screen)
            return
            
        if self.levelDisplay:
            self.displayNextLevel(screen)
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

