import math
import pygame
import time

pygame.init()

displayWidth = 1280
displayHeight = 720

display = pygame.display.set_mode((displayWidth, displayHeight))

posSwordX = 620 #636
posSwordY = 440 #504
startAngle = 0

pygame.display.set_caption('Sword bouncer')
sword = pygame.image.load('sword.png')
enemySkeletonSprite1 = pygame.image.load('enemySprite1.png')
enemySkeletonSprite2 = pygame.image.load('enemySprite2.png')
enemySkeletonSprite3 = pygame.image.load('enemySprite3.png')
enemySkeletonSprite4 = pygame.image.load('enemySprite4.png')
enemySkeletonSprite5 = pygame.image.load('enemySprite5.png')
enemySkeletonSprite6 = pygame.image.load('enemySprite6.png')
enemySkeletonSprite7 = pygame.image.load('enemySprite7.png')
enemySkeletonSprite8 = pygame.image.load('enemySprite8.png')
enemySkeletonSprite9 = pygame.image.load('enemySprite9.png')
enemySkeletonSprite10 = pygame.image.load('enemySprite10.png')
enemySkeletonSprite11 = pygame.image.load('enemySprite11.png')
enemySkeletonSprite12 = pygame.image.load('enemySprite12.png')

sprites = [enemySkeletonSprite1, enemySkeletonSprite2, enemySkeletonSprite3, enemySkeletonSprite4, enemySkeletonSprite5, enemySkeletonSprite6,
           enemySkeletonSprite7, enemySkeletonSprite8, enemySkeletonSprite9, enemySkeletonSprite10, enemySkeletonSprite11, enemySkeletonSprite12]

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

def rotate(angle):
    global sword
    sword = pygame.transform.rotate(sword, angle)
    rotated_image = pygame.transform.rotate(sword, angle)
    new_rect = rotated_image.get_rect(center=sword.get_rect(topleft=(int(posSwordX)-32, int(posSwordY)-128)).center)
    display.blit(sword, new_rect.topleft)

    return sword, new_rect

def angles():
    global posSwordX, posSwordY, startAngle
    angle = startAngle * 3.14 / 180
    posSwordX = (150 * math.cos(angle)) + 620  # 620 < начальная точка по x
    posSwordY = (250 * math.sin(angle)) + 440  # 540 < начальная точка по у

def runGame():
    global posSwordX, posSwordY, startAngle

    bg = pygame.image.load('bg.png')
    land = pygame.image.load('land.png')
    mc = pygame.image.load('mc.png')

    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            rotate(-4)
            angles()
            startAngle -= 4
        elif keys[pygame.K_d]:
            rotate(4)
            angles()
            startAngle += 4

        display.blit(bg, (0, 0))
        drawEnemy()
        display.blit(mc, (576, 400))
        display.blit(sword, (int(posSwordX), int(posSwordY)))
        display.blit(land, (0, 592))

        pygame.display.update()
        fpsLimiter.tick(60)
def animate():
    global skeletonAnimated
    skeletonAnimated = sprites[0]
    time.sleep(0.1)
    skeletonAnimated = sprites[1]
    time.sleep(0.1)
    skeletonAnimated = sprites[2]
    time.sleep(0.1)
    skeletonAnimated = sprites[3]
    time.sleep(0.1)
    skeletonAnimated = sprites[4]
    time.sleep(0.1)
    skeletonAnimated = sprites[5]
    time.sleep(0.1)
    skeletonAnimated = sprites[6]
    time.sleep(0.1)
    skeletonAnimated = sprites[7]
    time.sleep(0.1)
    skeletonAnimated = sprites[8]
    time.sleep(0.1)
    skeletonAnimated = sprites[9]
    time.sleep(0.1)
    skeletonAnimated = sprites[10]
    time.sleep(0.1)
    skeletonAnimated = sprites[11]
    time.sleep(0.1)
    return skeletonAnimated


def drawEnemy():
    global enemyX, enemyY, enemyWidth, enemyHeight

    if enemyX >= -enemyWidth:
        while True:
            display.blit(animate(), (enemyX, enemyY, enemyWidth, enemyHeight))
        enemyX -= 4
    else:
        enemyX = displayWidth - 50

runGame()
