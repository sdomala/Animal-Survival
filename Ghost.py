# Ghost class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 11/27/18

# Citation, got image from 
# https://techflourish.com/categories/halloween-zombie-clipart.html


from Enemy import *

# Ghost class that inherits and overrides Enemy properties/methods

class Ghost (Enemy) :
    def __init__(self, x, y, rows, cols, margin, width, height, stepY, stepX, plantBlocks, grassSlot, direction):
        super().__init__ (x, y, rows, cols, margin, width, height, stepY, stepX, plantBlocks, grassSlot, direction)
        self.image = pygame.image.load ('Ghost.png').convert_alpha()        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.health = 100