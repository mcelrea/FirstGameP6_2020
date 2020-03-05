import pygame
from Player import *
from Enemy import *

pygame.init() #start the pygame engine

#game variables
gameOver = False
x = 100
y = 100
FPS = 60 #60 Frames Per Second
fpsClock = pygame.time.Clock()
p1 = Player(100, 100, (255,0,0))
enemies = [] #a list of enemies
timeFont = pygame.font.SysFont("Arial", 30)
timeStarted = 0
addEnemiesSwitch = False


#set the game screen size to be 800x600 pixels
screen = pygame.display.set_mode((800,600))

def initEnemies():
    global enemies
    enemies.append(Enemy((0, 255, 0)))
    enemies.append(Enemy((0, 255, 0)))
    enemies.append(Enemy((0, 255, 0)))
    enemies.append(Enemy((0, 255, 0)))
    enemies.append(Enemy((0, 255, 0)))
    enemies.append(Enemy((0, 255, 0)))
    enemies.append(Enemy((0, 255, 0)))

def drawEnemies():
    global enemies
    global screen
    for e in enemies:
        e.draw(screen)

def updateEnemies():
    global enemies
    global p1
    for e in enemies:
        e.act()
        if p1.checkCollisionWithRect(e.getCollisionRectangle()):
            pygame.quit()

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

def drawUI():
    global timeFont
    global screen
    global timeStarted
    textSurface = timeFont.render("Time: " + str((pygame.time.get_ticks()-timeStarted)/1000), True, (255,255,255))
    screen.blit(textSurface, (390, 10))

def addEnemies(num):
    global enemies
    for n in range(0,num,1):#loop num times
        enemies.append(Enemy((0,255,0)))

def spawnNewEnemies():
    #if current time is evenly division by 5 (every 5 seconds)
    global timeStarted
    global addEnemiesSwitch
    if ((pygame.time.get_ticks()-timeStarted)/1000) % 5 == 0:
        #if I should add enemies (look at the switch)
        if addEnemiesSwitch == True:
            addEnemiesSwitch = False
            addEnemies(5) #need to add some enemies
    else: #the time is not evenly divisible by 5
        addEnemiesSwitch = True

initEnemies()
timeStarted = pygame.time.get_ticks() #time stamping the start of the game
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
    updateEnemies()
    spawnNewEnemies()

    # check for collisions

    # draw everything
    p1.draw(screen)
    drawEnemies()
    drawUI();

    # puts all the graphics onto the screen, should be last
    # line of game code
    pygame.display.flip()

    fpsClock.tick(FPS) #Slow the program to 60 loops per second


