#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:10:36 2017

@author: thinkpad

defining the Ant Colony
"""
from ant import Ant
import params

class Colony:
    """ Definig the Colony class
        The colony is a list of ants
    """
    def __init__(self, grid):

        self.ants_count = params.ants_count
        self.colony = [Ant(grid) for _ in range(self.ants_count)]

    def work(self):
        """ Make all ants works !
        """
        for ant in self.colony:
            ant.work()
