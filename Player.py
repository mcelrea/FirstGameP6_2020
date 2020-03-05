import pygame

class Player:

    # What are classes
    #   - reusable code
    #   - describes an object (in our game)

    # How to a make a class
    #  (1) declare what it is (variables)
    #        - (x,y)
    #        - color
    #        - speed
    #        - size
    #  (2) how to you make new versions of it
    #  (3) what actions can it take
    #        - move up, down, left, right
    #        - am I off the screen
    #        - check collisions with other game objects
    #        - draw myself to the screen

    # global variables
    size = 10
    speed = 3
    debug = True #if debug is True, show collision rectangle

    # special method: defines how to make new Players
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
        if self.debug == True:
            pygame.draw.rect(screen, (252,15,192), (self.x, self.y, self.size, self.size), 1)

    def checkCollisionWithRect(self, otherRect):
        myRect = pygame.Rect(self.x,self.y,self.size,self.size)
        return myRect.colliderect(otherRect)

    def moveRight(self):
        self.x += self.speed

        #collide with screen
        #if self.x > 799 - self.size:
        #    self.x = 799 - self.size

        #wrap around screen
        if self.x > 799 - self.size:
            self.x = 0


    def moveLeft(self):
        self.x -= self.speed
        #collide with screen
        #if self.x < 0:
        #    self.x = 0

        #wrap around screen
        if self.x < 0:
            self.x = 799 - self.size

    def moveDown(self):
        self.y += self.speed

        #collide with screen
        #if self.y > 599 - self.size:
        #    self.y = 599 - self.size

        #wrap around screen
        if self.y > 599 - self.size:
            self.y = 0

    def moveUp(self):
        self.y -= self.speed

        #collide with screen
        #if self.y < 0:
        #    self.y = 0

        #wrap around screen
        if self.y < 0:
            self.y = 599 - self.size