# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:20:14 2017

@author: thinkpad

App parameters
"""

global grid_size, block_size
grid_size = (125,125)    
block_size = 4 # display size : resolution*blockSize    


global quantity,evaporate,phero_min,phero_max
evaporate = 0.98
step = 5
phero_min = 1 # phero minimal
phero_max = 40 # pheromone maximale

global alpha,beta,ants_count,life_span    
ants_count = 100 # pour chaque colonie (colonie1 noir,colonie2 : vert)
alpha = 0.5 # importance de pheromone pour colonie1,colonie2
beta = -8 # importance de direction lineaire, negatif pr aller en diagonale, (colonie1,colonie2)
life_span = 100