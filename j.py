import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
bg = pygame.image.load('ScreenshotStarfield.png')
bg_y = 0
bg_y2 = bg.get_height()
pygame.display.set_caption('Space Invaders')  # set caption
icon = pygame.image.load('spaceship.png')  # set icon
pygame.display.set_icon(icon)
# player
player_img = pygame.image.load('player.png')
player_x = 370
player_y = 480
delta_x = 0
# enemy
num = 6
enemy_img = []
enemy_x = []
enemy_y = []
delta1_x = []
for i in range(num):
    enemy_img.append(pygame.image.load('boom.png'))
    enemy_x.append(random.randint(0, 800))
    enemy_y.append(random.randint(20, 110))
    delta1_x.append(2.5)
# bullet
bullet_img = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
delta2_y = 2
bullet_state = 'ready'  # ready is that you cannot see the bullet
score = 0
run = True


def window():
    screen.blit(bg, (0, bg_y))
    screen.blit(bg, (0, bg_y2))


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i1):
    screen.blit(enemy_img[i1], (x, y))


def fire(x, y):
    screen.blit(bullet_img, (x + 16, y + 10))
    global bullet_state
    bullet_state = 'fire'


def collision(x1, y1, x2, y2):
    dist = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    if dist < 27:
        return True
    else:
        return False


# gameloop
font = pygame.font.SysFont('comicsans', 30, True)
while run:
    window()
    bg_y += 3
    bg_y2 += 3
    if bg_y > 150:
        bg_y = 150
    if bg_y2 > 150:
        bg_y2 = 0
    # screen.blit(bg, (0, 0))
    text = font.render('Score :' + str(score), 1, (255, 0, 0))
    screen.blit(text, (680, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # checking keystrokes
        elif event.type == pygame.KEYDOWN:  # KEYDOWN is the pressing on the key
            if event.key == pygame.K_LEFT:
                delta_x = -3
            elif event.key == pygame.K_RIGHT:
                delta_x = 3
            elif event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_x = player_x
                    fire(bullet_x, bullet_y)
        elif event.type == pygame.KEYUP:  # KEYUP is releasing the key
            if event.key == pygame.K_LEFT:
                delta_x = 0
            elif event.key == pygame.K_RIGHT:
                delta_x = 0

    player_x += delta_x
    # checking for boundaries
    if player_x > 736:
        player_x = 736
    elif player_x < 0:
        player_x = 0
    #  enemy movement
    for i in range(num):
        enemy_x[i] += delta1_x[i]
        if enemy_x[i] > 736:
            delta1_x[i] = 0.5
            # enemy_x[i] += delta1_x[i]
            enemy_y[i] += 40
        elif enemy_x[i] < 0:
            delta1_x[i] = 0.5
            # enemy_x[i] += delta1_x[i]
            enemy_y[i] += 40
        # collision
        col = collision(bullet_x, bullet_y, enemy_x[i], enemy_y[i])
        if col is True:
            bullet_y = 480
            bullet_state = 'ready'
            score += 1
            # print(score)
            enemy_x[i] = random.randint(0, 800)
            enemy_y[i] = random.randint(20, 110)
        enemy(enemy_x[i], enemy_y[i], i)
    #  bullet movement
    if bullet_y <= 0:
        bullet_state = 'ready'
        bullet_y = 480
    if bullet_state is 'fire':
        fire(bullet_x, bullet_y)
        bullet_y -= delta2_y
        fire(bullet_x, bullet_y)
    player(player_x, player_y)
    pygame.display.update()
    # clock.tick(30)
pygame.quit()
# top-left corner is origin
