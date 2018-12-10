# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_script.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_script_widget(object):
    def setupUi(self, script_widget):
        script_widget.setObjectName("script_widget")
        script_widget.resize(954, 692)
        script_widget.setStyleSheet("#script_widget{background-color: rgb(179, 179, 179);}")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(script_widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrip_tab = QtWidgets.QTabWidget(script_widget)
        self.scrip_tab.setStyleSheet("")
        self.scrip_tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.scrip_tab.setObjectName("scrip_tab")
        self.script_tab_import = QtWidgets.QWidget()
        self.script_tab_import.setObjectName("script_tab_import")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.script_tab_import)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.script_text_import = QtWidgets.QTextEdit(self.script_tab_import)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.script_text_import.sizePolicy().hasHeightForWidth())
        self.script_text_import.setSizePolicy(sizePolicy)
        self.script_text_import.setObjectName("script_text_import")
        self.verticalLayout_2.addWidget(self.script_text_import)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.script_button_import_reset = QtWidgets.QPushButton(self.script_tab_import)
        self.script_button_import_reset.setObjectName("script_button_import_reset")
        self.horizontalLayout_2.addWidget(self.script_button_import_reset)
        self.script_button_import_run = QtWidgets.QPushButton(self.script_tab_import)
        self.script_button_import_run.setDefault(True)
        self.script_button_import_run.setObjectName("script_button_import_run")
        self.horizontalLayout_2.addWidget(self.script_button_import_run)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.scrip_tab.addTab(self.script_tab_import, "")
        self.script_tab_phase = QtWidgets.QWidget()
        self.script_tab_phase.setObjectName("script_tab_phase")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.script_tab_phase)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.script_text_phase = QtWidgets.QTextEdit(self.script_tab_phase)
        self.script_text_phase.setObjectName("script_text_phase")
        self.verticalLayout_3.addWidget(self.script_text_phase)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.script_button_phase_reset = QtWidgets.QPushButton(self.script_tab_phase)
        self.script_button_phase_reset.setObjectName("script_button_phase_reset")
        self.horizontalLayout_5.addWidget(self.script_button_phase_reset)
        self.script_button_phase_run = QtWidgets.QPushButton(self.script_tab_phase)
        self.script_button_phase_run.setDefault(True)
        self.script_button_phase_run.setObjectName("script_button_phase_run")
        self.horizontalLayout_5.addWidget(self.script_button_phase_run)
        self.script_button_phase_view = QtWidgets.QPushButton(self.script_tab_phase)
        self.script_button_phase_view.setObjectName("script_button_phase_view")
        self.horizontalLayout_5.addWidget(self.script_button_phase_view)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.scrip_tab.addTab(self.script_tab_phase, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.para_group = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.para_group.sizePolicy().hasHeightForWidth())
        self.para_group.setSizePolicy(sizePolicy)
        self.para_group.setMinimumSize(QtCore.QSize(200, 0))
        self.para_group.setMaximumSize(QtCore.QSize(200, 16777215))
        self.para_group.setBaseSize(QtCore.QSize(200, 0))
        self.para_group.setObjectName("para_group")
        self.verticalLayout.addWidget(self.para_group)
        self.mask_group = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mask_group.sizePolicy().hasHeightForWidth())
        self.mask_group.setSizePolicy(sizePolicy)
        self.mask_group.setMinimumSize(QtCore.QSize(200, 0))
        self.mask_group.setMaximumSize(QtCore.QSize(200, 16777215))
        self.mask_group.setBaseSize(QtCore.QSize(200, 0))
        self.mask_group.setObjectName("mask_group")
        self.verticalLayout.addWidget(self.mask_group)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.panel_widget = QtWidgets.QWidget(self.groupBox_2)
        self.panel_widget.setObjectName("panel_widget")
        self.horizontalLayout_8.addWidget(self.panel_widget)
        self.verticalLayout_9.addWidget(self.groupBox_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.scrip_tab.addTab(self.tab_2, "")
        self.script_tab_reduction = QtWidgets.QWidget()
        self.script_tab_reduction.setObjectName("script_tab_reduction")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.script_tab_reduction)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.script_text_reduction = QtWidgets.QTextEdit(self.script_tab_reduction)
        self.script_text_reduction.setObjectName("script_text_reduction")
        self.verticalLayout_4.addWidget(self.script_text_reduction)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.script_button_reduction_reset = QtWidgets.QPushButton(self.script_tab_reduction)
        self.script_button_reduction_reset.setObjectName("script_button_reduction_reset")
        self.horizontalLayout_6.addWidget(self.script_button_reduction_reset)
        self.script_button_reduction_run = QtWidgets.QPushButton(self.script_tab_reduction)
        self.script_button_reduction_run.setDefault(True)
        self.script_button_reduction_run.setObjectName("script_button_reduction_run")
        self.horizontalLayout_6.addWidget(self.script_button_reduction_run)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.scrip_tab.addTab(self.script_tab_reduction, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.script_text_post = QtWidgets.QTextEdit(self.tab)
        self.script_text_post.setObjectName("script_text_post")
        self.verticalLayout_8.addWidget(self.script_text_post)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.script_button_post_reset = QtWidgets.QPushButton(self.tab)
        self.script_button_post_reset.setObjectName("script_button_post_reset")
        self.horizontalLayout_7.addWidget(self.script_button_post_reset)
        self.script_button_post_run = QtWidgets.QPushButton(self.tab)
        self.script_button_post_run.setDefault(True)
        self.script_button_post_run.setObjectName("script_button_post_run")
        self.horizontalLayout_7.addWidget(self.script_button_post_run)
        self.script_button_post_view = QtWidgets.QPushButton(self.tab)
        self.script_button_post_view.setObjectName("script_button_post_view")
        self.horizontalLayout_7.addWidget(self.script_button_post_view)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.scrip_tab.addTab(self.tab, "")
        self.verticalLayout_5.addWidget(self.scrip_tab)

        self.retranslateUi(script_widget)
        self.scrip_tab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(script_widget)

    def retranslateUi(self, script_widget):
        _translate = QtCore.QCoreApplication.translate
        script_widget.setWindowTitle(_translate("script_widget", "Form"))
        self.script_button_import_reset.setText(_translate("script_widget", "Reset"))
        self.script_button_import_run.setText(_translate("script_widget", "Run"))
        self.scrip_tab.setTabText(self.scrip_tab.indexOf(self.script_tab_import), _translate("script_widget", "Data import"))
        self.script_button_phase_reset.setText(_translate("script_widget", "Reset"))
        self.script_button_phase_run.setText(_translate("script_widget", "Run"))
        self.script_button_phase_view.setText(_translate("script_widget", "View"))
        self.scrip_tab.setTabText(self.scrip_tab.indexOf(self.script_tab_phase), _translate("script_widget", "Phase correction"))
        self.para_group.setTitle(_translate("script_widget", "Parameters"))
        self.mask_group.setTitle(_translate("script_widget", "Mask"))
        self.groupBox_2.setTitle(_translate("script_widget", "GroupBox"))
        self.scrip_tab.setTabText(self.scrip_tab.indexOf(self.tab_2), _translate("script_widget", "Panel"))
        self.script_button_reduction_reset.setText(_translate("script_widget", "Reset"))
        self.script_button_reduction_run.setText(_translate("script_widget", "Run"))
        self.scrip_tab.setTabText(self.scrip_tab.indexOf(self.script_tab_reduction), _translate("script_widget", "Reduction"))
        self.script_button_post_reset.setText(_translate("script_widget", "Reset"))
        self.script_button_post_run.setText(_translate("script_widget", "Run"))
        self.script_button_post_view.setText(_translate("script_widget", "View"))
        self.scrip_tab.setTabText(self.scrip_tab.indexOf(self.tab), _translate("script_widget", "Post process"))

