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
directions = {i:directions_vect[i] for i in range(8)}


class Ant(object):
    """ Ant Class
    """
    def __init__(self, grid):
        """ Initializing the ants
        """

        self.grid = grid
        self.x, self.y = random.choice(self.grid.nests)

        self.has_food = False
        self.distance = 500

        self.weights = np.zeros(8)
        self.direction = random.randint(0, 7)

    def reset(self):
        """ The ant restarts from a random nest
        """
        self.has_food = False
        self.distance = 500

        self.weights = np.zeros(8)
        self.direction = random.randint(0, 7)

        self.x, self.y = random.choice(self.grid.nests)

    def when_has_food(self):
        """ Returns the pheromone quantity to scatter if the ant carries food
        """
        return 1

    def when_no_food(self):
        """ Returns the pheromone quantity to scatter when ant doesn't has food
        """
        return 1

    def scatter_phero(self):
        """ Add the pheromone to the current cell
        """
        
        self.grid[self.x, self.y].phero += 1


    def choose_direction(self):
        """ Updates the self.direction based on radom choice of weighted directions
            Weights using the weights self.weights
        """
        self.direction = random.randint(0,7)


    def work(self): # the brain
        """ The algorithm of the ant movment
        """
        # Scatter pheromone in the current cell
        self.scatter_phero()

        # If a direction has been chosen
        
        # decrement the ants count in the current cell
        self.grid[self.x, self.y].count -= 1
        self.choose_direction()
        # destination is the direction in vector form
        destination = directions[self.direction]

        # Move to next cell
        self.x += destination[0]
        self.y += destination[1]

        # Increment ants count in new cell
        reward = 0
        try:
            if self.grid[self.x, self.y].type =="FOOD":
                reward = 1
        except:
            self.x -= destination[0]
            self.y -= destination[1]
            reward = -1
        self.grid[self.x, self.y].count += 1
        #decrmetn distance runned
        self.distance -= 1
        
        return reward
        # If no direction has been returned : blocked path
        

        # If new cell has food :
        #       mark ant as has food and intialize distance
        #       do a 180° turn
        

        # If the new cell is the nest : reset ant and decrement ants count

