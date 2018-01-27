# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:57:32 2017

@author: thinkpad

Defining the Cell Class
"""
import sys
import numpy as np
import pygame
import params


class Application(object):
    """ Defining the PyGame interface that displays the grid,ants and pheromones traces
"""
    def __init__(self):

        self.block_size = params.block_size
        self.grid_size = params.grid_size
        self.disp_size = list(np.array(self.grid_size)*self.block_size)
        self.display = None

    def begin_draw(self, grid):
        """ Displays the empty grid to add/remove walls if needeed
            You can also edit walls when the ants are working
            """
        pygame.init()
        self.display = pygame.display.set_mode(self.disp_size)
        pygame.display.set_caption('Map Editing')
        font = pygame.font.SysFont("arial", 15)
        strings = ["Press ESC to Start Drawing Obstacles",
                   "Click Left to Draw & Right to Erase",
                   "To finish Drawing,press Escape ",
                   "During search, Escape or Close to Quit",
                   "you can also draw during the search, but it won't ba saved"]
        texts = [font.render(s, True, (255, 255, 255)) for s in strings]
        for i, text in enumerate(texts):
            self.display.blit(text, (self.disp_size[0]//20, i*20+self.disp_size[1]//20))
        pygame.display.update()
        main_screen = True
        while main_screen:
            print("Waiting for start")
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_screen = False
        self.display.fill([255, 255, 255])
        grid.draw(self.display)
        pygame.display.update()
        print("Now painting")
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
            pos = list((np.array(pygame.mouse.get_pos())/self.block_size).astype(int))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                print("Add wall at", pos)
                grid[pos].type = "WALL"
                grid[pos].draw(self.display, self.block_size)
            elif pygame.mouse.get_pressed() == (0, 0, 1):
                print("remove wall from", pos)
                grid[pos].type = "ROAD"
                grid[pos].draw(self.display, self.block_size)
            pygame.display.update()

    def start_app(self, grid, colony):
        """ Start the colony algorithm and displays the changes on the grid
        """
        pygame.init()
        pygame.display.set_caption('Ant Colony')
        while True:
            # Start iterations
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pos = list((np.array(pygame.mouse.get_pos())/self.block_size).astype(int))
                    print("Add wall at", pos)
                    grid[pos].type = "WALL"
                    grid[pos].draw(self.display, self.block_size)
                elif pygame.mouse.get_pressed() == (0, 0, 1):
                    pos = list((np.array(pygame.mouse.get_pos())/self.block_size).astype(int))
                    print("remove wall from", pos)
                    grid[pos].type = "ROAD"
                    grid[pos].draw(self.display, self.block_size)
            self.display = pygame.display.set_mode(self.disp_size)
            self.display.fill([255, 255, 255])
            # The core
            colony.work()
            grid.update()
            grid.draw(self.display)
            pygame.display.update()
