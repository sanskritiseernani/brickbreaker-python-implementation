# Sanskriti Seernani
# Section 062

import pygame
import sys

from Ball import Ball
from Block import Block
from Text import Text


def intersect(rect1 ,rect2):
    if rect1.x < rect2.x + rect2.width and \
    rect1.x + rect1.width > rect2.x and \
    rect1 .y < rect2 .y + rect2 . height and \
    rect1 . height + rect1 .y > rect2 .y:
        return True
    return False


pygame.init()
width = 500
height = 500

ball = Ball(20,400)
text = Text(0, 0)

block_list = []
for x in range(0,3):
    for y in range(0,3):
        block_list.append(Block(400+x*20, 400-y*20-20))

surface = pygame.display.set_mode((width, height))

dt = 0.1
g = 6.67
R = 0.7
eta = 0.5
xv = 0
yv = 0
score = text.getScore()

while True:
    surface.fill((255, 255, 255))
    text.draw(surface)
    pygame.draw.line(surface, (0, 0, 0), (0, 400), (500, 400), 2)
    ball.draw(surface)

    for s in block_list:
        if s.getVisible():
            s.draw(surface)

    ball_location = ball.getLoc()
    new_x = ball_location[0] + (dt*xv)
    new_y = ball_location[1] - (dt*yv)

    new_loc = (new_x, new_y)
    ball.setLoc(new_loc)

    if ball_location[1] > 400:
        ball.setLoc((ball.getLoc()[0], 400))
        yv = -R * yv
        xv = eta * xv

    elif xv < 0.1 and abs(yv) < 0.1:
        xv = 0
        ball.setLoc((ball.getLoc()[0], 400))

    else:
        yv = yv - g*dt

    for event in pygame.event.get():

        if (event.type == pygame.QUIT) or \
                (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.__dict__["key"] == pygame.K_r:
            ball.setLoc((20,400))
            xv = 0
            yv = 0

        elif event.type == pygame.MOUSEBUTTONDOWN:
            positiondep_mouse = pygame.mouse.get_pos()

        elif event.type == pygame.MOUSEBUTTONUP:
            position_mouse = pygame.mouse.get_pos()
            xv = position_mouse[0] - positiondep_mouse[0]
            yv = -1*(position_mouse[1] - positiondep_mouse[1])

    for i in range(len(block_list)):
        if intersect(ball.get_rect(),block_list[i].get_rect()):
            if block_list[i].getVisible():
                score += 1
                text.setScore(score)
            block_list[i].setVisible(False)

    pygame.display.update()


