# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:51:50 2017

@author: Ayoub


Defining the Ant class
"""
###############################################################################
import random
import numpy as np


directions_vect = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


class Ant(object):
    """ Ant Class
    """
    def __init__(self, grid):
        """ Initializing the ants
        """
        
        self.grid = grid
        self.pos = random.choice(self.grid.nests)
        self.has_food = False
        self.states = [self.get_state()]
        self.rewards = []
        self.action_dists = []
        
        self.distance = 0


    def reset(self):
        """ The ant restarts from a random nest
        """
        self.has_food = False
        self.distance = 0

        self.pos = random.choice(self.grid.nests)

    def scatter_phero(self):
        """ Add the pheromone to the current cell
        """
        
        self.grid[self.pos[0],self.pos[1]].phero += 1


    def choose_direction(self):
        """ Updates the self.direction based on radom choice of weighted directions
            Weights using the weights self.weights
        """
        self.direction = random.randint(0,7)

    def get_state(self):
        return self.grid.get_state(self.pos,self.has_food)
    def act(self): # the brain
        """ The algorithm of the ant movment
        """
        # Scatter pheromone in the current cell
        self.scatter_phero()

        # If a direction has been chosen
        
        # decrement the ants count in the current cell
        self.choose_direction()
        # destination is the direction in vector form
        destination = directions_vect[self.direction]

        # Move to next cell
        new_pos = (self.pos[0]+destination[0],self.pos[1]+destination[1])

        self.pos,reward = self.grid.access(self.pos,new_pos,self.has_food)
        
        
        #decrmetn distance runned
        
        self.distance += 1
        
        return reward
        