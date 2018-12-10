# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'env_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_env_widget(object):
    def setupUi(self, env_widget):
        env_widget.setObjectName("env_widget")
        env_widget.resize(544, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(env_widget.sizePolicy().hasHeightForWidth())
        env_widget.setSizePolicy(sizePolicy)
        env_widget.setMinimumSize(QtCore.QSize(0, 250))
        env_widget.setMaximumSize(QtCore.QSize(16777215, 250))
        env_widget.setBaseSize(QtCore.QSize(0, 250))
        env_widget.setStyleSheet("#env_widget{\n"
"background-color: rgb(255, 255, 255);}\n"
"\n"
"#env_widget:focus{\n"
"background-color: rgb(220, 220, 220);\n"
"\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(env_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(env_widget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.env_label_name = QtWidgets.QLabel(self.groupBox)
        self.env_label_name.setObjectName("env_label_name")
        self.horizontalLayout_3.addWidget(self.env_label_name)
        self.env_input_name = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.env_input_name.sizePolicy().hasHeightForWidth())
        self.env_input_name.setSizePolicy(sizePolicy)
        self.env_input_name.setObjectName("env_input_name")
        self.horizontalLayout_3.addWidget(self.env_input_name)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.env_label_status_load = QtWidgets.QLabel(self.groupBox)
        self.env_label_status_load.setAlignment(QtCore.Qt.AlignCenter)
        self.env_label_status_load.setObjectName("env_label_status_load")
        self.verticalLayout.addWidget(self.env_label_status_load)
        self.env_label_status_mask = QtWidgets.QLabel(self.groupBox)
        self.env_label_status_mask.setAlignment(QtCore.Qt.AlignCenter)
        self.env_label_status_mask.setObjectName("env_label_status_mask")
        self.verticalLayout.addWidget(self.env_label_status_mask)
        self.env_label_status_phase = QtWidgets.QLabel(self.groupBox)
        self.env_label_status_phase.setAlignment(QtCore.Qt.AlignCenter)
        self.env_label_status_phase.setObjectName("env_label_status_phase")
        self.verticalLayout.addWidget(self.env_label_status_phase)
        self.env_label_status_computed = QtWidgets.QLabel(self.groupBox)
        self.env_label_status_computed.setAlignment(QtCore.Qt.AlignCenter)
        self.env_label_status_computed.setObjectName("env_label_status_computed")
        self.verticalLayout.addWidget(self.env_label_status_computed)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.env_text_data_print = QtWidgets.QTextBrowser(self.groupBox)
        self.env_text_data_print.setObjectName("env_text_data_print")
        self.horizontalLayout_2.addWidget(self.env_text_data_print)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.env_button_load = QtWidgets.QPushButton(self.groupBox)
        self.env_button_load.setObjectName("env_button_load")
        self.verticalLayout_2.addWidget(self.env_button_load)
        self.env_button_mask = QtWidgets.QPushButton(self.groupBox)
        self.env_button_mask.setObjectName("env_button_mask")
        self.verticalLayout_2.addWidget(self.env_button_mask)
        self.env_button_scripts = QtWidgets.QPushButton(self.groupBox)
        self.env_button_scripts.setObjectName("env_button_scripts")
        self.verticalLayout_2.addWidget(self.env_button_scripts)
        self.env_button_result = QtWidgets.QPushButton(self.groupBox)
        self.env_button_result.setObjectName("env_button_result")
        self.verticalLayout_2.addWidget(self.env_button_result)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(env_widget)
        QtCore.QMetaObject.connectSlotsByName(env_widget)

    def retranslateUi(self, env_widget):
        _translate = QtCore.QCoreApplication.translate
        env_widget.setWindowTitle(_translate("env_widget", "Form"))
        self.env_label_name.setText(_translate("env_widget", "Name:"))
        self.env_label_status_load.setText(_translate("env_widget", "Data loaded"))
        self.env_label_status_mask.setText(_translate("env_widget", "Mask set"))
        self.env_label_status_phase.setText(_translate("env_widget", "Phase proc."))
        self.env_label_status_computed.setText(_translate("env_widget", "Computed"))
        self.env_button_load.setText(_translate("env_widget", "Load"))
        self.env_button_mask.setText(_translate("env_widget", "Mask"))
        self.env_button_scripts.setText(_translate("env_widget", "Scripts"))
        self.env_button_result.setText(_translate("env_widget", "Results"))
