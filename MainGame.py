import pygame
from Player import *

pygame.init() #start the pygame engine

#game variables
gameOver = False
x = 100
y = 100
FPS = 60 #60 Frames Per Second
fpsClock = pygame.time.Clock()
p1 = Player(100, 100, (255,0,0))

#set the game screen size to be 800x600 pixels
screen = pygame.display.set_mode((800,600))


def checkForPlayerInput():
    global p1
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]:
        p1.moveRight()
    if pressed[pygame.K_a]:
        p1.moveLeft()
    if pressed[pygame.K_w]:
        p1.moveUp()
    if pressed[pygame.K_s]:
        p1.moveDown()

while not gameOver:
    # loop through and empty the event queue, key presses, button clicks, etc.
    for event in pygame.event.get():

        # if the event is a click on the "X" close button
        if event.type == pygame.QUIT:
            gameOver = True

    # clear the screen
    pygame.draw.rect(screen, (0,0,0), (0,0,800,600))

    # update player(s)
    checkForPlayerInput()

    # update enemies

    # check for collisions

    # draw everything
    p1.draw(screen)

    # puts all the graphics onto the screen, should be last
    # line of game code
    pygame.display.flip()

    fpsClock.tick(FPS) #Slow the program to 60 loops per second


