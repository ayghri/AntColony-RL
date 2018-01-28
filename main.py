#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 20:37:01 2017

@author: thinkpad
"""
from grid import Grid
from colony import Colony
from application import Application
#import multiprocessing


# Creating the grid
grid_map = Grid()

# Loading the grid from the file map.txt
grid_map.load_grid("map.txt")

# Create the Colony moving in grid_map
ants_colony = Colony(grid_map)

# Start the interface
app = Application(grid_map)

# Start adding walls, if necessary
#app.begin_draw(grid_map)

# Uncomment if you want to kepe the modified grid
# grid_map.save_grid("map2.txt")
# Start the colony
#multiprocessing.Process(target=app.start_app,args=[]).start()
        # The core
        
print("Starting the work")
while True:
    app.draw_app()
    ants_colony.work()
    grid_map.update()
