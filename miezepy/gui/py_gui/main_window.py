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


from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import optparse
from functools import partial

from ..qt_gui.mainwindow_ui         import Ui_MIEZETool 

from ..py_gui.page_data_widget      import PageDataWidget
from ..py_gui.page_env_widget       import PageEnvWidget
from ..py_gui.page_script_widget    import PageScriptWidget
from ..py_gui.page_io_widget        import PageIOWidget

class MainWindowLayout(Ui_MIEZETool):
    '''
    ##############################################
    This is the main window element that will later
    be the item managin the rest of the system. 
    Note that at a later point we will feature
    drag and drop onto this window.
    ———————
    Input: -
    ———————
    Output: -
    ———————
    status: active
    ##############################################
    '''
    def __init__(self, window, window_manager):

        #set up the window
        Ui_MIEZETool.__init__(self)
        self.window = window
        self.window_manager = window_manager
        self.setupUi(window)
        self.initialize()
        self.connect()
        self.revertAllButtons()
        self.selectButton(0)
        self.hideActivity()

    def connect(self):
        '''
        ##############################################
        connect the actions to their respective buttons
        ———————
        Input: -
        ———————
        Output: -
        ———————
        status: active
        ##############################################
        '''

        #button actions
        self.env_button.clicked.connect(self.refreshChecked)
        self.data_button.clicked.connect(self.refreshChecked)
        self.script_button.clicked.connect(self.refreshChecked)
        self.save_button.clicked.connect(self.refreshChecked)

        #Menu actions
        self.actionAddEnv.triggered.connect(
            partial(self.actionDispatcher, 0, self.widgetClasses[0].addEnvironment))
        self.actionRemoveEnv.triggered.connect(
            partial(self.actionDispatcher, 0, self.widgetClasses[0].deleteEnvironment))

        self.actionAdd_element.triggered.connect(
            partial(self.actionDispatcher, 1, self.widgetClasses[1].addElement))
        self.actionRemove_element.triggered.connect(
            partial(self.actionDispatcher, 1, self.widgetClasses[1].removeElement))
        self.actionGenerate.triggered.connect(
            partial(self.actionDispatcher, 1, self.widgetClasses[1].generateDataset))
        self.actionSave_to_file.triggered.connect(
            partial(self.actionDispatcher, 1, self.widgetClasses[1].save))
        self.actionLoad_from_file.triggered.connect(
            partial(self.actionDispatcher, 1, self.widgetClasses[1].load))

        self.actionSaveScript.triggered.connect(
            partial(self.actionDispatcher, 2, self.widgetClasses[2].saveScripts))
        self.actionLoadScript.triggered.connect(
            partial(self.actionDispatcher, 2, self.widgetClasses[2].loadScripts))
        self.actionImport.triggered.connect(
            partial(self.actionDispatcher, 2, partial(self.widgetClasses[2].run,0)))
        self.actionPhase.triggered.connect(
            partial(self.actionDispatcher, 2, partial(self.widgetClasses[2].run,1)))
        self.actionReduction.triggered.connect(
            partial(self.actionDispatcher, 2, partial(self.widgetClasses[2].run,2)))
        self.actionVisual.triggered.connect(
            partial(self.actionDispatcher, 2, partial(self.widgetClasses[2].run,3)))
        self.actionAll.triggered.connect(
            partial(self.actionDispatcher, 2, self.widgetClasses[2].runAll))

        self.actionLoad_Session.triggered.connect(
            partial(self.actionDispatcher, 3, partial(self.widgetClasses[3].getLoadPath, True)))
        self.actionSave_Session.triggered.connect(
            partial(self.actionDispatcher, 3, partial(self.widgetClasses[3].getSavePath, True)))

    def actionDispatcher(self,index, method = None):
        '''
        ##############################################
        This will dispatch the actions to the right 
        function but still try to check if the page is
        the right one.

        ———————
        Input: 
        - meta_class is the metadata class from the io
        ———————
        Output: -
        ———————
        status: active
        ##############################################
        '''
        if not self.stack.currentIndex() == index:
            if index == 0:
                self.refreshChecked(0)
            if index == 1:
                if not self.widgetClasses[1].io_core == self.handler.current_env.io:
                    self.widgetClasses[1].link(self.handler.current_env.io)
                self.refreshChecked(1)
            elif index == 2:
                if not self.widgetClasses[2].env == self.handler.current_env:
                    self.widgetClasses[2].link(self.handler.current_env)
                self.refreshChecked(2)
            elif index == 3:
                self.refreshChecked(3)

        if not method == None:
            method()

    def link(self, handler):
        '''
        ##############################################
        link the class that will manage the current 
        input output.
        ———————
        Input: 
        - meta_class is the metadata class from the io
        ———————
        Output: -
        ———————
        status: active
        ##############################################
        '''
        self.setActivity(
            'Linking',0,3)
        
        self.setProgress('Linking handler',0)
        self.handler = handler 

        self.setProgress('Linking script view',1)
        self.widgetClasses[0].link(self.handler)

        self.setProgress('Linking script view',3)
        self.widgetClasses[3].link(self.handler)

        self.fadeActivity()
        
    def initialize(self):
        '''
        ##############################################
        This method checks if the data has been set
        in a previous instance.
        ———————
        Input: -
        ———————
        Output: -
        ———————
        status: active
        ##############################################
        '''
        self.stack = QtWidgets.QStackedWidget()

        self.widgetClasses = [
            PageEnvWidget(self.stack, self),
            PageDataWidget(self.stack, self),
            PageScriptWidget(self.stack, self),
            PageIOWidget(self.stack, self)]

        self.stack.addWidget(self.widgetClasses[1].local_widget)

        for element in self.widgetClasses:
            self.stack.addWidget(element.local_widget)

        self.main_layout.addWidget(self.stack)

    def refreshChecked(self, index = None):
        '''
        ##############################################
        This method will determine the button that the
        user selected and perform the appropriate 
        measures.
        ———————
        Input: -
        ———————
        Output: -
        ———————
        status: active
        ##############################################
        '''
        if index == None or isinstance(index, bool):

            pointers = [
                self.env_button,
                self.data_button,
                self.script_button,
                self.save_button
            ]
            
            checked = [ element.isChecked() for element in pointers]

            for i in range(len(pointers)):
                if not checked[i] == self.checked[i]:
                    to_check = i
                    break
        else:
            to_check = index

        self.revertAllButtons()
        self.selectButton(to_check)

    def revertAllButtons(self):
        '''
        ##############################################
        This method will revert all button to their 
        unchecked state.
        ———————
        Input: -
        ———————
        Output: -
        ———————
        status: active
        ##############################################
        '''
        pointers = [
            self.env_button,
            self.data_button,
            self.script_button,
            self.save_button
        ]

        for element in pointers:
            element.setChecked(False)

        self.checked = [element.isChecked() for element in pointers]

    def selectButton(self, i):
        '''
        ##############################################
        This method will set one button to checked
        ———————
        Input: 
        - index of the button to check
        ———————
        Output: -
        ———————
        status: active
        ##############################################
        '''
        pointers = [
            self.env_button,
            self.data_button,
            self.script_button,
            self.save_button
        ]

        pointers[i].setChecked(True)
        self.checked = [element.isChecked() for element in pointers]
        self.stack.setCurrentIndex(i)

    def setActivity(self, label_0, min_val, max_val):
        '''
        ##############################################
        This method will set all activity parts active
        and then set label0
        ———————
        Input: 
        - index of the button to check
        ———————
        Output: -
        ———————
        status: active
        ##############################################
        '''
        #make it visible in case it was hidden
        self.main_label_progress_0.show()
        self.main_label_progress_1.show()
        self.main_bar_progress.show()
        self.main_line_progress_0.show()
        self.main_line_progress_1.show()

        #in case it was faded
        self.unfade(self.main_label_progress_0)
        self.unfade(self.main_label_progress_1)
        self.unfade(self.main_bar_progress)
        self.unfade(self.main_line_progress_0)
        self.unfade(self.main_line_progress_1)

        #set the initial content
        self.main_label_progress_0.setText(label_0)
        self.main_bar_progress.setMinimum(min_val)
        self.main_bar_progress.setMaximum(max_val)

    def hideActivity(self):
        '''
        ##############################################
        This method will set all activity parts active
        and then set label0
        ———————
        Input: 
        - index of the button to check
        ———————
        Output: -
        ———————
        status: active
        ##############################################
        '''
        self.main_label_progress_0.hide()
        self.main_label_progress_1.hide()
        self.main_bar_progress.hide()
        self.main_line_progress_0.hide()
        self.main_line_progress_1.hide()

    def fadeActivity(self):
        '''
        ##############################################
        This method will set all activity parts active
        and then set label0
        ———————
        Input: 
        - index of the button to check
        ———————
        Output: -
        ———————
        status: active
        ##############################################
        '''
        self.fade(self.main_label_progress_0)
        self.fade(self.main_label_progress_1)
        self.fade(self.main_bar_progress)
        self.fade(self.main_line_progress_0)
        self.fade(self.main_line_progress_1)

    def unfade(self, widget):
        '''
        ##############################################
        This method will fade out the widget that it
        is assigned to.
        ———————
        Input: 
        - widget (QtWidget)
        ———————
        Output: -
        ———————
        status: active
        ##############################################
        '''
        effect = QtWidgets.QGraphicsOpacityEffect()
        effect.setOpacity(1)
        widget.setGraphicsEffect(effect)

    def fade(self, widget):
        '''
        ##############################################
        This method will fade out the widget that it
        is assigned to.
        ———————
        Input: 
        - widget (QtWidget)
        ———————
        Output: -
        ———————
        status: active
        ##############################################
        '''
        widget.effect = QtWidgets.QGraphicsOpacityEffect()
        widget.setGraphicsEffect(widget.effect)

        widget.animation = QtCore.QPropertyAnimation(widget.effect, b"opacity")
        widget.animation.setDuration(1000)
        widget.animation.setStartValue(1)
        widget.animation.setEndValue(0)
        widget.animation.start()

    def setProgress(self, label, val):
        '''
        ##############################################
        This method will set all activity parts active
        and then set label0
        ———————
        Input: 
        - index of the button to check
        ———————
        Output: -
        ———————
        status: active
        ##############################################
        '''
        self.main_bar_progress.setValue(val)
        self.main_label_progress_1.setText(label)
        self.window_manager.app.processEvents()