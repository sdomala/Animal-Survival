# Monster class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 11/21/18

from Enemy import *

# Monster class that inherits all Enemy properties/methods

class Monster (Enemy) :
    def __init__(self, x, y, rows, cols, margin, width, height, stepY, stepX, plantBlocks, grassSlot, direction):
        super().__init__ (x, y, rows, cols, margin, width, height, stepY, stepX, plantBlocks, grassSlot, direction)
       

       