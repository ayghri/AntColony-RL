#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 18:26:13 2017

@author: thinkpad

Defining the Grid class that contains all the cells
"""
import params
from cell import Cell


class Grid(object):
    """ Definig the Grid object
        The Grid is basically a matrix of Cells
    """
    def __init__(self):
        self.grid_size = params.grid_size

        self.grid = [[Cell(i, j) for j in range(params.grid_size[0])] \
                     for i in range(params.grid_size[1])]

        self.nests = []
        self.update_time = 0
        self.step = params.step

    def __getitem__(self, pos):
        """
        Returns the cell in pos
        """
        i, j = pos
        if (i*(i-self.grid_size[0]) > 0) or (j*(j-self.grid_size[1]) > 0):
            print("coordinates out of bound, grid size :", (i, j), "out of", self.grid_size)
            raise NameError("Cell not found")
            return None
        return self.grid[i][j]

    def load_grid(self, filename):
        """Loads the grid from filename
        the file contains lines in the format : int x, int y,cell_type
        """
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for i in lines:
            i = i.replace("\n", "").split(",")
            self.grid[int(i[0])][int(i[1])].type = i[2].upper()
            if i[2] == "NEST":
                self.nests.append([int(n) for n in i[:2]])

    def save_grid(self, filename):
        """ Saves the grid from to memory to filename
        """
        file = open(filename, "w")
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                if self.grid[i][j].type != "ROAD":
                    file.write(str(i)+","+str(j)+","+self.grid[i][j].type+"\n")
        file.close()

    def update(self):
        """ Iterates through all cells and updates them
        """
        self.update_time = (self.update_time+1)%self.step
        if self.update_time == 0:
            for row in self.grid:
                for cell in row:
                    cell.update()

    def draw(self, display):
        """ Draw all the grid's cells
        """
        for row in self.grid:
            for cell in row:
                cell.draw(display, params.block_size)
