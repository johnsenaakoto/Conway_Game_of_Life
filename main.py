# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 23:22:51 2021

@author: Chico
"""

import pygame
import time
import random
import numpy as np
import os
import grid

os.environ["SDL_VIDEO_CENTERED"]='1'

#width, height = 1920,1080
width, height = 1280, 720
size = (width, height)

pygame.init()
pygame.display.set_caption("Conway Game of Life")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0,14,71)
white = (255, 255, 255)

scaler = 20
offset = 1

Grid = grid.Grid(width, height, scaler, offset)
Grid.random2d_arr()

run = True

while run:
    clock.tick(fps)
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #random_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
    Grid.Conway(off_color = white, on_color = blue1, surface = screen)
    pygame.display.update()

pygame.quit()
