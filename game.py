import math
import pygame

pygame.init()

displayWidth = 1280
displayHeight = 720

display = pygame.display.set_mode((displayWidth, displayHeight))

posSwordX = 620
posSwordY = 440
startAngle = -90
startAngle2 = 0

pygame.display.set_caption('Sword bouncer')

spritesEnemy = [pygame.image.load('enemySprite1.png'), pygame.image.load('enemySprite2.png'), pygame.image.load('enemySprite3.png'),
           pygame.image.load('enemySprite4.png'), pygame.image.load('enemySprite5.png'), pygame.image.load('enemySprite6.png'),
           pygame.image.load('enemySprite7.png'), pygame.image.load('enemySprite8.png'), pygame.image.load('enemySprite9.png'),
           pygame.image.load('enemySprite10.png'), pygame.image.load('enemySprite11.png'), pygame.image.load('enemySprite12.png')]

spritesMc = [pygame.image.load('mc.png'), pygame.image.load('mc1.png'), pygame.image.load('mc2.png'),
             pygame.image.load('mc3.png'), pygame.image.load('mc4.png'), pygame.image.load('mc5.png'), pygame.image.load('mc6.png')]

imgCounter = 11
imgCounterMc = 6
mainTemp = 0
startAngle3 = -272

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

def checkMc():
    if mainTemp != 1:
        if 409 > int(mcY) > 399:
            return True
        else:
            return False
    if mainTemp == 1:
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

    display.blit(spritesEnemy[imgCounter // 5], (enemyX, enemyY))
    imgCounter += 1

def anglesForSword():
    global posSwordX, posSwordY, startAngle
    angle = startAngle * 3.14 / 180
    posSwordX = (170 * math.cos(angle)) + mcX + 44  # 620 < начальная точка по x  # -208 начальный угол для лева
    posSwordY = (170 * math.sin(angle)) + mcY + 80  # 480 < начальная точка по у  # -332 начальный угол для права

def anglesForMc(range):
    global mcX, mcY, startAngle2
    angle = startAngle2 * 3.14 / 180
    mcX = (150 * math.cos(angle)) + posSwordX - range
    mcY = (150 * math.sin(angle)) + 400

def anglesForMc2(range):
    global mcX, mcY, startAngle3
    angle = startAngle3 * 3.14 / 180
    mcX = (150 * math.sin(-angle)) + posSwordX - range          # -272 начальный угол лева
    mcY = (150 * math.cos(-angle)) + 400                        #

def runGame():
    global posSwordX, posSwordY, startAngle, startAngle2, mainTemp, imgCounterMc, startAngle3

    bg = pygame.image.load('bg.png')
    land = pygame.image.load('land.png')
    sword = pygame.image.load('sword.png')

    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if 408 > mcY > 0 and mainTemp == 0:
            if -208 < startAngle < 28:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    anglesForSword()
                    startAngle -= 4
                if keys[pygame.K_d]:
                    anglesForSword()
                    startAngle += 4
            if -208 > startAngle > -212:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    anglesForMc(41)
                    startAngle2 -= 4
                if keys[pygame.K_d]:
                    if mcY > 399:
                        anglesForSword()
                        startAngle += 4
                if keys[pygame.K_d]:
                    if mcY < 399:
                        anglesForMc(41)
                        startAngle2 += 4
            if 28 < startAngle < 32:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    if mcY > 399:
                        anglesForSword()
                        startAngle -= 4
                if keys[pygame.K_a]:
                    if mcY < 399:
                        anglesForMc2(49)
                        startAngle3 -= 4
                if keys[pygame.K_d]:
                    anglesForMc2(49)
                    startAngle3 += 4
        if mcX < 277:
            mainTemp = 5
        if mainTemp == 5:


        display.blit(bg, (0, 0))
        if imgCounterMc == 30:
            imgCounterMc = 0
        display.blit(spritesMc[imgCounterMc // 5], (int(mcX), int(mcY)))
        imgCounterMc += 1
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
