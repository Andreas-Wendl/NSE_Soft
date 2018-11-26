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
#import main components
from .core.core_handler             import Handler as CORE_Manager
from .gui.py_gui.window_handlers    import WindowHandler


class Mieze (CORE_Manager, WindowHandler):

    '''
    ##############################################
    Here lies the main NSE tool manager class. It can be
    accessed in the python terminal through: 
    "from NSE.Main import Manager as NSE"
    ##############################################
    '''

    def __init__(self, GUI = False):

        ##############################################
        #initiate the core manager  
        CORE_Manager.__init__(self)

        ##############################################
        #initiate the GUI manager if need be
        if GUI == True:

            WindowHandler.__init__(self)
