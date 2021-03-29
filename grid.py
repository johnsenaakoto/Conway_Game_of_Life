# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 23:26:38 2021

@author: Chico
"""

import pygame
import numpy as np
import random

class Grid:
    def __init__(self, width, height, scale, offset):
        self.scale = scale
        
        self.columns = int(height/scale)
        self.rows = int(width/scale)
        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape = (self.size))
        self.offset = offset
        
    def random2d_arr(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.grid_array[i][j] = random.randint(0,1)
                
    def Conway(self, off_color, on_color, surface):
        for i in range(self.rows):
            for j in range(self.columns):
                i_pos = i * self.scale
                j_pos = j * self.scale
                
                random_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
                if self.grid_array[i][j] == 1:
                    pygame.draw.rect(surface, random_color, [i_pos, j_pos, self.scale-self.offset, self.scale-self.offset])
                else:
                    pygame.draw.rect(surface, off_color, [i_pos, j_pos, self.scale-self.offset, self.scale-self.offset])
        
        next1 = np.ndarray(shape=(self.size))
        for i in range(self.rows):
            for j in range(self.columns):
                state = self.grid_array[i][j]
                neighbors = self. get_neighbors(i, j)
                
                if state == 0 and neighbors == 3:
                    next1[i][j] = 1
                elif state == 1 and (neighbors < 2 or neighbors > 3):
                    next1[i][j] = 0
                else:
                    next1[i][j] = state
        self.grid_array = next1
        
    def get_neighbors(self, i, j):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                i_edge = (i+n+self.rows) % self.rows
                j_edge = (j+m+self.columns) % self.columns
                total += self.grid_array[i_edge][j_edge]

        total -= self.grid_array[i][j]
        return total