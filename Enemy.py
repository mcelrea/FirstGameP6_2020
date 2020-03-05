import pygame
import random

class Enemy:

    #besides color, what is an Enemy
    speed = 3
    size = 10
    xvel = 0
    yvel = 0
    debug = True #if debug is True, show collision boxes

    #how to create an new Enemy
    def __init__(self, color):
        self.color = color
        self.x = 0
        self.y = 0

        choice = random.randint(1,4)

        # spawn on left wall
        if choice == 1:
            self.x = 0
            self.y = random.randint(0, 599 - self.size)
            self.xvel = random.randint(3,7)
        # spawn on top wall
        elif choice == 2:
            self.x = random.randint(0, 799 - self.size)
            self.y = 0
            self.yvel = random.randint(3, 7)
        # spawn on right wall
        elif choice == 3:
            self.x = 799 - self.size
            self.y = random.randint(0, 599 - self.size)
            self.xvel = random.randint(-7, -3)
        # spawn on bottom wall
        elif choice == 4:
            self.x = random.randint(0, 799 - self.size)
            self.y = 599 - self.size
            self.yvel = random.randint(-7, -3)

    def act(self):
        self.x += self.xvel
        self.y += self.yvel

        if self.x < 0: #off left side of screen
            self.x = 799 - self.size
        if self.y < 0: #off top of screen
            self.y = 599 - self.size
        if self.x > 799 - self.size: #right side of screen
            self.x = 0
        if self.y > 599 - self.size: #off bottom of screen
            self.y = 0

    def getCollisionRectangle(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen,self.color,(self.x, self.y, self.size, self.size))
        if self.debug == True:
            pygame.draw.rect(screen,(252,15,192), (self.x,self.y,self.size,self.size), 1)