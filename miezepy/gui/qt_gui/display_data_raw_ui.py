# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display_data_raw.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_raw_display(object):
    def setupUi(self, raw_display):
        raw_display.setObjectName("raw_display")
        raw_display.resize(800, 600)
        raw_display.setStyleSheet("#main_widget{\n"
"background-color: rgb(64, 66, 68);}")
        self.main_widget = QtWidgets.QWidget(raw_display)
        self.main_widget.setObjectName("main_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.echo_label = QtWidgets.QLabel(self.main_widget)
        self.echo_label.setStyleSheet("#echo_label{color: rgb(179, 179, 179);}")
        self.echo_label.setObjectName("echo_label")
        self.horizontalLayout.addWidget(self.echo_label)
        self.echo_drop = QtWidgets.QComboBox(self.main_widget)
        self.echo_drop.setObjectName("echo_drop")
        self.horizontalLayout.addWidget(self.echo_drop)
        self.foil_label = QtWidgets.QLabel(self.main_widget)
        self.foil_label.setStyleSheet("#foil_label{color: rgb(179, 179, 179);}")
        self.foil_label.setObjectName("foil_label")
        self.horizontalLayout.addWidget(self.foil_label)
        self.foil_spin = QtWidgets.QSpinBox(self.main_widget)
        self.foil_spin.setObjectName("foil_spin")
        self.horizontalLayout.addWidget(self.foil_spin)
        self.time_label = QtWidgets.QLabel(self.main_widget)
        self.time_label.setStyleSheet("#time_label{color: rgb(179, 179, 179);}")
        self.time_label.setObjectName("time_label")
        self.horizontalLayout.addWidget(self.time_label)
        self.time_spin = QtWidgets.QSpinBox(self.main_widget)
        self.time_spin.setObjectName("time_spin")
        self.horizontalLayout.addWidget(self.time_spin)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.graph_widget = QtWidgets.QWidget(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_widget.sizePolicy().hasHeightForWidth())
        self.graph_widget.setSizePolicy(sizePolicy)
        self.graph_widget.setStyleSheet("#graph_widget{background-color: rgb(179, 179, 179);}")
        self.graph_widget.setObjectName("graph_widget")
        self.verticalLayout.addWidget(self.graph_widget)
        raw_display.setCentralWidget(self.main_widget)
        self.menubar = QtWidgets.QMenuBar(raw_display)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        raw_display.setMenuBar(self.menubar)

        self.retranslateUi(raw_display)
        QtCore.QMetaObject.connectSlotsByName(raw_display)

    def retranslateUi(self, raw_display):
        _translate = QtCore.QCoreApplication.translate
        raw_display.setWindowTitle(_translate("raw_display", "MainWindow"))
        self.echo_label.setText(_translate("raw_display", "Echo"))
        self.foil_label.setText(_translate("raw_display", "Foil"))
        self.time_label.setText(_translate("raw_display", "Time channel"))

