import pygame
import sys,time

from pygame.locals import *

a=10
b=120
rocketx=15
rockety=80

a1=450
b1=120
rocketx1=15
rockety1=80

x=240
y=160
dx=-4
dy=4

pygame.init()
screen = pygame.display.set_mode((480, 320))
pygame.display.set_caption("Hello")
while True:
    pressed_key = pygame.key.get_pressed()
    if pressed_key[K_UP] and b > 0:
        b-=10
    if pressed_key[K_DOWN] and b < 240:
        b+=10
    if x == 40:
        if y > b and y < b + rockety:
            dx=-dx
    if x < 15:
        pygame.quit()
        sys.exit()
    if y < b1 + rockety1:
        b1 -= 10
    if y > b1:
        b1 += 10
    if x == 440:
        if y > b1 and y < b1 + rockety1:
            dx=-dx
    if x > 465:
        pygame.quit()
        sys.exit()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (a, b, rocketx, rockety))
    pygame.draw.rect(screen, (0, 255, 0), (a1, b1, rocketx1, rockety1))
    pygame.draw.circle(screen, (0, 255, 0), (x, y), 15, 15)
    pygame.display.update()

    y += dy
    if y + 15 > 320 or y < 15:
        dy = -dy
    time.sleep(0.01)
    x += dx
    if x + 15 > 480:
        dx = -dx
    time.sleep(0.01)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()