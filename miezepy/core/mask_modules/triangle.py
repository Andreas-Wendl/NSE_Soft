#  -*- coding: utf-8 -*-
# *****************************************************************************
# Copyright (c) 2017 by the NSE analysis contributors (see AUTHORS)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Module authors:
#   Alexander Schober <alex.schober@mac.com>
#
# *****************************************************************************

#############################
#import general components
import numpy as np
from .mask_shape import MaskShape

class Triangle(MaskShape):

    def __init__(self):
        '''
        This class will contain all the
        informations and routines to build
        a square over a certain 2D grid.
        '''
        MaskShape.__init__(self)
        self.initialize()

    def initialize(self):
        '''
        This routine will edit the inherited 
        dictionary of parameters.
        '''
        self.parameters['type']     = 'triangle'
        self.parameters['base']     = 10
        self.parameters['height']   = 10

    def generate(self, size_x, size_y):
        '''
        This will generate the mask element 
        onto a canvas of a given dimension
        '''
        polygon_edges = []
        polygon_edges.append([
            self.parameters['position'][0] - self.parameters['base'] / 2.,
            self.parameters['position'][1] - self.parameters['height'] / 3.])
        polygon_edges.append([
            self.parameters['position'][0] + self.parameters['base'] / 2.,
            self.parameters['position'][1] - self.parameters['height'] / 3.])
        polygon_edges.append([
            self.parameters['position'][0] ,
            self.parameters['position'][1] + self.parameters['height'] * 2 / 3.])

        for i, element in enumerate(polygon_edges):
            polygon_edges[i] = self.rotatePoint(
                self.parameters['position'],
                polygon_edges[i] , 
                self.parameters['angle'])


        self.mask = self.processPolygon(polygon_edges, size_x, size_y)