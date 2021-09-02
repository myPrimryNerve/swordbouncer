import math
import pygame

pygame.init()

displayWidth = 1280
displayHeight = 720

display = pygame.display.set_mode((displayWidth, displayHeight))

posSwordX = 620 #636
posSwordY = 440 #504
startAngle = 0

pygame.display.set_caption('Sword bouncer')
sword = pygame.image.load('sword.png')

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
    new_rect = sword.get_rect(center=sword.get_rect(center=(int(posSwordX)+16, int(posSwordY)+64)).center)
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

def drawEnemy():
    global enemyX, enemyY, enemyWidth, enemyHeight

    if enemyX >= -enemyWidth:
        pygame.draw.rect(display, (0, 255, 255), (enemyX, enemyY, enemyWidth, enemyHeight))
        enemyX -= 4
    else:
        enemyX = displayWidth - 50

runGame()
