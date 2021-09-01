import math
import pygame

pygame.init()

displayWidth = 1280
displayHeight = 720

display = pygame.display.set_mode((displayWidth, displayHeight))

posSwordX = 640
posSwordY = 560
startAngle = 0

pygame.display.set_caption('Sword bouncer')

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

def rotCenter(image, rect, angle):
        rotImage = pygame.transform.rotate(image, angle)
        rotRect = rotImage.get_rect(center=rect.center)
        return rotImage,rotRect

def angles():
    global posSwordX, posSwordY, startAngle
    angle = startAngle * 3.14 / 180
    posSwordX = (150 * math.cos(angle)) + 620  # 640 < начальная точка по x
    posSwordY = (250 * math.sin(angle)) + 500  # 560 < начальная точка по у

def runGame():
    global posSwordX, posSwordY, startAngle

    bg = pygame.image.load('bg.png')
    land = pygame.image.load('land.png')
    sword = pygame.image.load('sword.png')
    mc = pygame.image.load('mc.png')

    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            angles()
            rect = sword.get_rect(center=(int(posSwordX), int(posSwordY)))
            surf, r = rotCenter(sword, rect, -4)
            display.blit(surf, r)
            startAngle -= 4
        elif keys[pygame.K_d]:
            angles()
            rect = sword.get_rect(center=(int(posSwordX), int(posSwordY)))
            surf, r = rotCenter(sword, rect, 4)
            display.blit(surf, r)
            startAngle += 4

        display.blit(bg, (0, 0))
        drawEnemy()
        display.blit(mc, (576, 400))
        display.blit(sword, (int(posSwordX), int(posSwordY)))
        display.blit(land, (0, 592))

        pygame.display.update()
        fpsLimiter.tick(60)

def drawEnemy():
    global enemyX, enemyY, enemyWidth, enemyHeight

    if enemyX >= -enemyWidth:
        pygame.draw.rect(display, (0, 255, 255), (enemyX, enemyY, enemyWidth, enemyHeight))
        enemyX -= 4
    else:
        enemyX = displayWidth - 50

runGame()
