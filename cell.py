# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:57:32 2017

@author: thinkpad

Defining the Cell Class

The Cell class has the atrributes:
    x, y : coordinates
    ant_count : number of ants in the cell
    phero_min, phero_max : bounding values of pheromone
    evaporation : 1-evaporation rate
    type :  ROAD, WALL, FOOD, NEST
    color : chosen to reflect the type (see Colors dictionary)
    intensity : parameter used for the transpency of the pheromone traces
"""
import pygame
import params


BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PHERO = (255, 70, 0)
RED = (255, 0, 0)
WALL = (50, 70, 15)
WHITE = (255, 255, 255)

COLORS = {"FOOD":GREEN, "WALL" : WALL, "NEST" : BLUE, "ROAD" : WHITE}

class Cell(object):
    """ Defining the Cell object
    """
    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.count = 0
        self.phero = params.phero_min
        self.phero_max = params.phero_max
        self.evaporate = params.evaporate

        self.type = "ROAD"
        self.color = WHITE
        self.intensity = 0

    ###########################################################################
    # refresh the cell stats :
    #            evaporate the pheromone
    #            the food cells are set to pharo_max"""
    def update(self):
        """ Update the cell by evaporating the pheromone traces and
            update the intensity variable
            Intensity reflects the alpha of the pheromone color

        """
        if self.type == "FOOD":
            self.phero = self.phero_max
        elif self.type == "ROAD":
            self.intensity = min((1-self.evaporate)*self.phero,self.phero_max)

    def draw(self, display, block_size):
        """ Draw the cell on the PyGame display
            Black if contains ant
            Blue for Nest
            Green for food
            Orange for pheromone

        """
        if self.count > 0:
            self.color = BLACK
        else:
            self.color = COLORS[self.type]

        pygame.draw.rect(display, self.color,
                         [self.x*block_size, self.y*block_size, block_size, block_size])

        if self.type == "ROAD":
            temp_surf = pygame.Surface((block_size, block_size), pygame.SRCALPHA)
            temp_surf.fill((PHERO[0], PHERO[1], PHERO[2], self.intensity))
            display.blit(temp_surf, (self.x*block_size, self.y*block_size))
