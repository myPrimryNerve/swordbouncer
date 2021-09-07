import math
import time
import pygame

pygame.init()

displayWidth = 1280
displayHeight = 720

display = pygame.display.set_mode((displayWidth, displayHeight))

posSwordX = 620
posSwordY = 440
startAngle = 0

pygame.display.set_caption('Sword bouncer')

sprites = [pygame.image.load('enemySprite1.png'), pygame.image.load('enemySprite2.png'), pygame.image.load('enemySprite3.png'),
           pygame.image.load('enemySprite4.png'), pygame.image.load('enemySprite5.png'), pygame.image.load('enemySprite6.png'),
           pygame.image.load('enemySprite7.png'), pygame.image.load('enemySprite8.png'), pygame.image.load('enemySprite9.png'),
           pygame.image.load('enemySprite10.png'), pygame.image.load('enemySprite11.png'), pygame.image.load('enemySprite12.png')]

imgCounter = 11

def drawEnemy():
    global imgCounter, enemyX, enemyY, enemyWidth, enemyHeight
    if enemyX >= -enemyWidth:
        enemyX -= 2
    else:
        enemyX = displayWidth - 50
    if imgCounter == 55:
        imgCounter = 0

    display.blit(sprites[imgCounter // 5], (enemyX, enemyY))
    imgCounter += 1

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

mcWidth = 40
mcHeight = 60
mcX = displayWidth / 2
mcY = displayHeight / 1.35

enemyWidth = 128
enemyHeight = 184
enemyX = displayWidth - 50
enemyY = 408

fpsLimiter = pygame.time.Clock()

def angles():
    global posSwordX, posSwordY, startAngle
    angle = startAngle * 3.14 / 180
    posSwordX = (150 * math.cos(angle)) + 620  # 620 < начальная точка по x
    posSwordY = (150 * math.sin(angle)) + 480  # 540 < начальная точка по у

def runGame():
    global posSwordX, posSwordY, startAngle

    bg = pygame.image.load('bg.png')
    land = pygame.image.load('land.png')
    mc = pygame.image.load('mc.png')
    sword = pygame.image.load('sword.png')

    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            angles()
            startAngle -= 4
        elif keys[pygame.K_d]:
            angles()
            startAngle += 4

        display.blit(bg, (0, 0))
        display.blit(mc, (576, 400))
        display.blit(sword, (int(posSwordX), int(posSwordY)))
        display.blit(land, (0, 592))
        drawEnemy()
        pygame.display.update()
        fpsLimiter.tick(600)

runGame()
