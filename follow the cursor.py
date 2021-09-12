"""
Follow the cursor, delete the last chunk of code and use 'a', and 'd', to go through the shapes 1-by-1
(you can also change the "plus_amount" (the amount of change in the angle))

This project does use the print statement
"""

import pygame
import math

clock = pygame.time.Clock()

angle = 0  # don't really worry about this one its for the function
radius = 50
angle_plus = 0  # where the angle starts (can be anything you want)
plus_amount = .01

screen_x, screen_y = 1000, 700
win = pygame.display.set_mode((screen_x, screen_y))


def point_to_point(origin):  # draws the pretty lines
    new_point_X, new_point_Y = (math.sin(angle) * radius) + cursor_x, (math.cos(angle) * radius) + cursor_y
    pygame.draw.line(win, (0, 255, 200), (origin[0], origin[1]), (new_point_X, new_point_Y))
    return new_point_X, new_point_Y



while True:

    clock.tick(120)  # FPS or speed of the change of the angle (how fast the circle changes shape)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                angle_plus += plus_amount

            if event.key == pygame.K_a:
                angle_plus -= plus_amount
        if event.type == pygame.KEYUP:
            print(angle_plus)
            continue

    # ------------------------------------------------------------------------ #
    # important code
    cursor_x, cursor_y = pygame.mouse.get_pos()

    if angle <= 360:
        angle += angle_plus
    if angle > 360:
        angle = 0

    end_x1, end_y1 = (math.sin(angle) * radius) + cursor_x, (math.cos(angle) * radius) + cursor_y

    new_1, new_2 = point_to_point((end_x1, end_y1))
    if angle <= 360:
        angle += angle_plus
    if angle > 360:
        angle = 0
    new_3, new_4 = point_to_point((new_1, new_2))
    if angle <= 360:
        angle += angle_plus
    if angle > 360:
        angle = 0
    new_5, new_6 = point_to_point((new_3, new_4))
    if angle <= 360:
        angle += angle_plus
    if angle > 360:
        angle = 0
    new_7, new_8 = point_to_point((new_5, new_6))
    if angle <= 360:
        angle += angle_plus
    if angle > 360:
        angle = 0
    new_9, new_10 = point_to_point((new_7, new_8))
    # ------------------------------------------------------------------------ #



    # ------------------------------------------------------------------------ #
    # that chunk of code I talked about at the top

    if angle_plus <= 180:
        angle_plus += plus_amount
    elif angle_plus > 180:
        angle_plus = 0
    print(angle_plus)

    # ------------------------------------------------------------------------ #



    pygame.display.update()
    win.fill((50, 0, 0))  # color of the screen (in RGB)
