import math
import pygame
import random

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

spritesBossFight = [pygame.image.load('boss1.png'), pygame.image.load('boss2.png'), pygame.image.load('boss3.png'),
                    pygame.image.load('boss4.png'), pygame.image.load('boss5.png'), pygame.image.load('boss6.png'),
                    pygame.image.load('boss7.png')]

spritesLightning = [pygame.image.load('lightning1.png'), pygame.image.load('lightning2.png'), pygame.image.load('lightning3.png'),
                    pygame.image.load('lightning4.png'), pygame.image.load('lightning5.png'), pygame.image.load('lightning6.png'),
                    pygame.image.load('lightning7.png'), pygame.image.load('lightning8.png'), pygame.image.load('lightning9.png'),
                    pygame.image.load('lightning10.png'), pygame.image.load('lightning11.png'), pygame.image.load('lightning12.png'),
                    pygame.image.load('lightning13.png'), pygame.image.load('lightning14.png'), pygame.image.load('lightning15.png')]

spritesDeath = [pygame.image.load('enemyDeath1.png'), pygame.image.load('enemyDeath2.png'), pygame.image.load('enemyDeath3.png'),
                pygame.image.load('enemyDeath4.png'), pygame.image.load('enemyDeath5.png'), pygame.image.load('enemyDeath6.png'),
                pygame.image.load('enemyDeath7.png')]

rattle = pygame.mixer.Sound('boss1.mp3')
swipe = pygame.mixer.Sound('boss2.mp3')
pygame.mixer.music.load('bg.mp3')
gameOver = pygame.image.load('gameover.png')

imgCounter = 0
imgCounterMc = 0
imgCounterBoss = 0
imgCounterLight = 0
imgCounterDeath = 0
mainTempF = 0
startAngle3 = -272
jumpCounter = 0
jump = True
something = 0
overGame = False

abilitySpeed = 0
abilitySpin = 0
randomTemp = 0
gameOverTemp = 0

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

mcX = 576
mcY = 400
bX = 212
bY = 721
deathPosX = -300
deathPosY = 408

enemyWidth = 128
enemyHeight = 184
enemyX = displayWidth - 50
enemyY = 408

fpsLimiter = pygame.time.Clock()

def gameOverNotFunc():
    global gameOverTemp, overGame
    display.blit(gameOver, (128, 200))
    if gameOverTemp >= 10:
        overGame = True
    else:
        gameOverTemp += 1
    pygame.mixer.music.pause()
    while overGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def pause():
    paused = True
    pygame.mixer.music.pause()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            pygame.mixer.music.unpause()
            paused = False

def bossFight():
    global bY, jumpCounter, bX, imgCounterBoss, jump, imgCounterLight
    if jump:
        if jumpCounter >= -50:
            bY += jumpCounter / 2.5
            jumpCounter -= 1
        if jumpCounter < -50:
            jumpCounter -= (1 / 50)
            if jumpCounter <= -52:
                jumpCounter = 50
        if jumpCounter == 1:
            jump = False
            imgCounterLight = 0

        if imgCounterBoss == 30:
            imgCounterBoss = 0
        display.blit(spritesBossFight[imgCounterBoss // 5], (int(bX), int(bY)))
        imgCounterBoss += 1
        if imgCounterLight >= 42:
            imgCounterLight = 40
        display.blit(spritesLightning[imgCounterLight // 3], (384, 64))
        imgCounterLight += 1

def checkKill():
    global deathPosX, imgCounterDeath, deathPosY
    if int(posSwordY) + 32 >= enemyY:
        if enemyX <= int(posSwordX) <= enemyX + 128:
            deathPosX = int(posSwordX)
            deathPosY = 408
            imgCounterDeath = 0
            return True
        if enemyX <= int(posSwordX) + 32 <= enemyX + 128:
            deathPosX = int(posSwordX)
            deathPosY = 408
            imgCounterDeath = 0
            return True
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

def runGame():
    global posSwordX, posSwordY, startAngle, startAngle2, mainTempF, imgCounterMc,\
        startAngle3, mcX, enemyX, imgCounterMc, jump, bY, bX, imgCounterDeath, deathPosX, deathPosY, something,\
        randomTemp, abilitySpeed, abilitySpin

    pygame.mixer.music.play(-1)

    bg = pygame.image.load('bg.png')
    land = pygame.image.load('land.png')
    sword = pygame.image.load('sword.png')

    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if -208 < startAngle < 28:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pause()
            if keys[pygame.K_q]:
                anglesForSword()
                startAngle -= 4
            if keys[pygame.K_e]:
                anglesForSword()
                startAngle += 4
        if -208 > startAngle > -212:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                anglesForSword()
                startAngle += 4
        if 28 < startAngle < 32:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                anglesForSword()
                startAngle -= 4
        if 128 < mcX < 1024:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                mcX -= 4
                posSwordX -= 4
            if keys[pygame.K_d]:
                mcX += 4
                posSwordX += 4
        if mcX <= 128:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                mcX += 4
                posSwordX += 4
        if mcX >= 1024:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                mcX -= 4
                posSwordX -= 4




        display.blit(bg, (0, 0))
        if imgCounterMc == 30:
            imgCounterMc = 0
        display.blit(spritesMc[imgCounterMc // 5], (int(mcX), int(mcY)))
        imgCounterMc += 1
        display.blit(sword, (int(posSwordX), int(posSwordY)))
        display.blit(land, (0, 592))
        drawEnemy()

        if checkKill() == True:
            enemyX = 1400
            mainTempF += 1
        if imgCounterDeath >= 28:
            imgCounterDeath = 28
            deathPosY += 5
        display.blit(spritesDeath[imgCounterDeath // 5], (deathPosX, deathPosY))
        imgCounterDeath += 1
        if mainTempF > 10 and jump == True:
            bossFight()
            if something == 0:
                pygame.mixer.Sound.play(swipe)
                something = 1
            if jump == False:
                mainTempF = 0
                something = 0
        if mainTempF <= 1 and jump == False:
            pygame.mixer.Sound.play(rattle)
            jump = True
        if checkGameOver() == True:
            display.blit(gameOver, (128, 200))
            gameOverNotFunc()


        pygame.display.update()
        fpsLimiter.tick(60)

runGame()
