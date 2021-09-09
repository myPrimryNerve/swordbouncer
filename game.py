import math
import pygame

pygame.init()

displayWidth = 1280
displayHeight = 720

display = pygame.display.set_mode((displayWidth, displayHeight))

posSwordX = 620
posSwordY = 440
startAngle = 0
startAngle2 = 0
startAngle3 = 0

pygame.display.set_caption('Sword bouncer')

sprites = [pygame.image.load('enemySprite1.png'), pygame.image.load('enemySprite2.png'), pygame.image.load('enemySprite3.png'),
           pygame.image.load('enemySprite4.png'), pygame.image.load('enemySprite5.png'), pygame.image.load('enemySprite6.png'),
           pygame.image.load('enemySprite7.png'), pygame.image.load('enemySprite8.png'), pygame.image.load('enemySprite9.png'),
           pygame.image.load('enemySprite10.png'), pygame.image.load('enemySprite11.png'), pygame.image.load('enemySprite12.png')]

imgCounter = 11
mainTemp = 0

def checkMc():
    if mainTemp != 2:
        if int(mcY) > 399:
            return True
        else:
            return False
    elif mainTemp == 2:
        return False

def checkKill():
    if int(posSwordY) + 32 >= enemyY:
        if enemyX <= int(posSwordX) <= enemyX + 128:
            return True
        elif enemyX <= int(posSwordX) + 32 <= enemyX + 128:
            return True
    return False

def checkLand():
    if mainTemp != 1:
        if int(posSwordY) + 32 >= displayHeight - 128:
            return True
        else:
            return False
    elif mainTemp == 1:
        return False

def checkGameOver():
    if int(mcY) + 184 >= enemyY:
        if enemyX <= int(mcX) <= enemyX + 128:
            return True
        elif enemyX <= int(mcX) + 96 <= enemyX + 128:
            return True
    return False

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
mcX = 576
mcY = 400

enemyWidth = 128
enemyHeight = 184
enemyX = displayWidth - 50
enemyY = 408

fpsLimiter = pygame.time.Clock()

def anglesForSword():
    global posSwordX, posSwordY, startAngle
    angle = startAngle * 3.14 / 180
    posSwordX = (170 * math.cos(angle)) + mcX + 44  # 620 < начальная точка по x
    posSwordY = (170 * math.sin(angle)) + mcY + 80  # 480 < начальная точка по у

def anglesForMc(n):
    global mcX, mcY, startAngle2
    angle = startAngle2 * 3.14 / 180
    mcX = (150 * math.cos(angle)) + posSwordX - n  # 620 < начальная точка по x
    mcY = (150 * math.sin(angle)) + 400            # 540 < начальная точка по у

def anglesForMc2(n):
    global mcX, mcY, startAngle3
    angle = startAngle2 * 3.14 / 180
    mcX = (150 * math.sin(-angle)) + posSwordX - n  # 620 < начальная точка по x
    mcY = (150 * math.cos(-angle)) + 400            # 540 < начальная точка по у

def runGame():
    global posSwordX, posSwordY, startAngle, startAngle2, startAngle3, mainTemp

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
        if checkMc() == True and checkLand() == True:
            if checkMc() == False:
                mainTemp = 1
        if checkLand() == False:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                anglesForSword()
                startAngle -= 4
            elif keys[pygame.K_d]:
                anglesForSword()
                startAngle += 4
        if checkLand() == True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                anglesForMc(49)
                startAngle2 -= 4
            elif keys[pygame.K_d]:
                anglesForMc(49)
                startAngle2 += 4

        display.blit(bg, (0, 0))
        display.blit(mc, (int(mcX), int(mcY)))
        display.blit(sword, (int(posSwordX), int(posSwordY)))
        display.blit(land, (0, 592))
        drawEnemy()

        if checkKill() == True:
           pygame.draw.rect(display, (255, 0, 255), (500, 500, 100, 100))

        if checkGameOver() == True:
            pass

        pygame.display.update()
        fpsLimiter.tick(60)

runGame()
