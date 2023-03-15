import math
import pygame as py
from pygame import mixer as mi
import random

# initialize the python game
py.init()
screen = py.display.set_mode((800, 600))

sokem = [1, '1we']

# Title and Icon
py.display.set_caption("Space Invaders")
icon = py.image.load('images/spaceship.png')
py.display.set_icon(icon)

# Place Background Image
backgroundImg = py.image.load('images/background.png')
backgroundX = 0
backgroundY = 0

# Start music in background
mi.music.load('sounds/background.wav')
mi.music.play(-1)  # -1 is to be played on loop

# Place Spaceship
playerImg = py.image.load('images/spaceship.png')
playerX = 368
playerY = 480
playerX_move = 5
playerX_change = 0

# Place Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_move = 3
enemyY_move = 50
enemyX_change = []
num_enemies = 6

for i in range(num_enemies):
    enemyImg.append(py.image.load(f'images/alien{str(i)}.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(12, 150))
    enemyX_change.append(random.choice([-3, 3]))

# Set Bullet Ready means bullet not displayed on screen
bulletImg = py.image.load('images/bullet.png')
bulletX = 0
bulletY = 480
bullet_state = "ready"
bulletY_move = 6
score_value = 0
font = py.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10


def player(x, y):
    screen.blit(playerImg, (x, y))


over_font = py.font.Font('freesansbold.ttf', 64)


def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y))


def display_score(textX, textY):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (textX, textY))


def isCollision(enX, bulletX, enY, bulletY, i):
    one = enX[i] - bulletX
    two = enY[i] - bulletY
    podKoren = math.pow(one, 2) + math.pow(two, 2)
    distance = math.sqrt(podKoren)
    if distance < 35:
        return True

    return False


# Game loop
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(backgroundImg, (backgroundX, backgroundY))
    player(playerX, playerY)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False  # break ?

        playerX_change = 0
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                playerX_change = -playerX_move
            if event.key == py.K_RIGHT:
                playerX_change = playerX_move
            if event.key == py.K_SPACE or event.key == py.K_UP:

                if bullet_state == 'ready':
                    bullet_sound = mi.Sound('sounds/laser.wav')
                    bullet_sound.play()

                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

    playerX += playerX_change
    if playerX < -28:
        playerX = -28
    elif playerX > 764:
        playerX = 764

    for i in range(num_enemies):

        if enemyY[i] > 480:
            for j in range(num_enemies):
                enemyY[j] += 1000

            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] > 736:
            enemyX_change[i] = -enemyX_change[i]
            enemyY[i] += enemyY_move
        elif enemyX[i] < 0:
            enemyX_change[i] = -enemyX_change[i]
            enemyY[i] += enemyY_move

        collision = isCollision(enemyX, bulletX, enemyY, bulletY, i)
        if collision:
            coll_sound = mi.Sound('sounds/explosion.wav')
            coll_sound.play()

            bullet_state = 'ready'
            bulletY = 480
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(12, 150)

        enemy(enemyX[i], enemyY[i], i)

    if bulletY < -32:
        bullet_state = 'ready'
        bulletY = 480
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_move

    display_score(textX, textY)

    py.display.update()
