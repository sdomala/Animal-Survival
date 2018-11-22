# Zombie class for Term Project
# Name: Saisiddarth Domala
# andrewID: sdomala
# Section: O
# Last modified 11/21/18


from Enemy import *

# Zombie class that inherits and overrides Enemy properties/methods

class Zombie (Enemy) :
    def __init__(self, x, y, rows, cols, margin, width, height, stepY):
        super().__init__ (x, y, rows, cols, margin, width, height, stepY)
        print (3)
        self.image = pygame.image.load ('GreenZombie4.png').convert_alpha()        
        self.width = self.image.get_width()
        self.height = self.image.get_height()