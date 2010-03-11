# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../forms/freeseer_ui_qt.ui'
#
# Created: Thu Mar 11 18:42:20 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_FreeseerMainWindow(object):
    def setupUi(self, FreeseerMainWindow):
        FreeseerMainWindow.setObjectName("FreeseerMainWindow")
        FreeseerMainWindow.resize(463, 509)
        self.centralwidget = QtGui.QWidget(FreeseerMainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.main = QtGui.QWidget()
        self.main.setObjectName("main")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.main)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.recordButton = QtGui.QPushButton(self.main)
        self.recordButton.setCheckable(True)
        self.recordButton.setObjectName("recordButton")
        self.verticalLayout_2.addWidget(self.recordButton)
        self.optionsLayout = QtGui.QVBoxLayout()
        self.optionsLayout.setObjectName("optionsLayout")
        self.deviceOptionsLayout = QtGui.QHBoxLayout()
        self.deviceOptionsLayout.setObjectName("deviceOptionsLayout")
        self.deviceLabel = QtGui.QLabel(self.main)
        self.deviceLabel.setMaximumSize(QtCore.QSize(40, 16777215))
        self.deviceLabel.setObjectName("deviceLabel")
        self.deviceOptionsLayout.addWidget(self.deviceLabel)
        self.videoDeviceList = QtGui.QComboBox(self.main)
        self.videoDeviceList.setObjectName("videoDeviceList")
        self.deviceOptionsLayout.addWidget(self.videoDeviceList)
        self.videoSourceList = QtGui.QComboBox(self.main)
        self.videoSourceList.setObjectName("videoSourceList")
        self.deviceOptionsLayout.addWidget(self.videoSourceList)
        self.audioSourceList = QtGui.QComboBox(self.main)
        self.audioSourceList.setObjectName("audioSourceList")
        self.deviceOptionsLayout.addWidget(self.audioSourceList)
        self.optionsLayout.addLayout(self.deviceOptionsLayout)
        self.talkListLayout = QtGui.QHBoxLayout()
        self.talkListLayout.setObjectName("talkListLayout")
        self.talkLabel = QtGui.QLabel(self.main)
        self.talkLabel.setMaximumSize(QtCore.QSize(40, 24))
        self.talkLabel.setObjectName("talkLabel")
        self.talkListLayout.addWidget(self.talkLabel)
        self.talkList = QtGui.QComboBox(self.main)
        self.talkList.setObjectName("talkList")
        self.talkListLayout.addWidget(self.talkList)
        self.optionsLayout.addLayout(self.talkListLayout)
        self.verticalLayout_2.addLayout(self.optionsLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.previewWidget = QtGui.QWidget(self.main)
        self.previewWidget.setObjectName("previewWidget")
        self.gridLayout.addWidget(self.previewWidget, 0, 0, 2, 1)
        self.audioFeedbackSlider = QtGui.QSlider(self.main)
        self.audioFeedbackSlider.setOrientation(QtCore.Qt.Vertical)
        self.audioFeedbackSlider.setObjectName("audioFeedbackSlider")
        self.gridLayout.addWidget(self.audioFeedbackSlider, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.audioFeedbackCheckbox = QtGui.QCheckBox(self.main)
        self.audioFeedbackCheckbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.audioFeedbackCheckbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.audioFeedbackCheckbox.setObjectName("audioFeedbackCheckbox")
        self.verticalLayout_2.addWidget(self.audioFeedbackCheckbox)
        self.tabWidget.addTab(self.main, "")
        self.editTalksPage = QtGui.QWidget()
        self.editTalksPage.setObjectName("editTalksPage")
        self.verticalLayout = QtGui.QVBoxLayout(self.editTalksPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(self.editTalksPage)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.roomEdit = QtGui.QLineEdit(self.groupBox)
        self.roomEdit.setEnabled(False)
        self.roomEdit.setObjectName("roomEdit")
        self.gridLayout_2.addWidget(self.roomEdit, 2, 1, 1, 1)
        self.timeEdit = QtGui.QTimeEdit(self.groupBox)
        self.timeEdit.setEnabled(False)
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(9, 0, 0)))
        self.timeEdit.setTime(QtCore.QTime(9, 0, 0))
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_2.addWidget(self.timeEdit, 0, 1, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 2, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.titleEdit = QtGui.QLineEdit(self.groupBox)
        self.titleEdit.setObjectName("titleEdit")
        self.gridLayout_2.addWidget(self.titleEdit, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.presenterEdit = QtGui.QLineEdit(self.groupBox)
        self.presenterEdit.setEnabled(False)
        self.presenterEdit.setObjectName("presenterEdit")
        self.gridLayout_2.addWidget(self.presenterEdit, 3, 1, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_2.addWidget(self.checkBox_3, 3, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.addTalkButton = QtGui.QPushButton(self.groupBox)
        self.addTalkButton.setObjectName("addTalkButton")
        self.verticalLayout_3.addWidget(self.addTalkButton)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.editTalksPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.editTalkList = QtGui.QListWidget(self.groupBox_2)
        self.editTalkList.setObjectName("editTalkList")
        self.horizontalLayout_2.addWidget(self.editTalkList)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.removeTalkButton = QtGui.QPushButton(self.groupBox_2)
        self.removeTalkButton.setObjectName("removeTalkButton")
        self.verticalLayout_4.addWidget(self.removeTalkButton)
        self.saveButton = QtGui.QPushButton(self.groupBox_2)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout_4.addWidget(self.saveButton)
        self.resetButton = QtGui.QPushButton(self.groupBox_2)
        self.resetButton.setObjectName("resetButton")
        self.verticalLayout_4.addWidget(self.resetButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.editTalksPage, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)
        FreeseerMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FreeseerMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 463, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        FreeseerMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FreeseerMainWindow)
        self.statusbar.setObjectName("statusbar")
        FreeseerMainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(FreeseerMainWindow)
        self.actionExit.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtGui.QAction(FreeseerMainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.talkLabel.setBuddy(self.talkList)
        self.label.setBuddy(self.roomEdit)
        self.label_2.setBuddy(self.timeEdit)
        self.label_3.setBuddy(self.titleEdit)
        self.label_4.setBuddy(self.presenterEdit)

        self.retranslateUi(FreeseerMainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("toggled(bool)"), self.timeEdit.setEnabled)
        QtCore.QObject.connect(self.checkBox_2, QtCore.SIGNAL("toggled(bool)"), self.roomEdit.setEnabled)
        QtCore.QObject.connect(self.checkBox_3, QtCore.SIGNAL("toggled(bool)"), self.presenterEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(FreeseerMainWindow)
        FreeseerMainWindow.setTabOrder(self.timeEdit, self.roomEdit)
        FreeseerMainWindow.setTabOrder(self.roomEdit, self.presenterEdit)
        FreeseerMainWindow.setTabOrder(self.presenterEdit, self.titleEdit)
        FreeseerMainWindow.setTabOrder(self.titleEdit, self.addTalkButton)
        FreeseerMainWindow.setTabOrder(self.addTalkButton, self.editTalkList)
        FreeseerMainWindow.setTabOrder(self.editTalkList, self.checkBox)
        FreeseerMainWindow.setTabOrder(self.checkBox, self.checkBox_2)
        FreeseerMainWindow.setTabOrder(self.checkBox_2, self.checkBox_3)
        FreeseerMainWindow.setTabOrder(self.checkBox_3, self.recordButton)
        FreeseerMainWindow.setTabOrder(self.recordButton, self.videoDeviceList)
        FreeseerMainWindow.setTabOrder(self.videoDeviceList, self.videoSourceList)
        FreeseerMainWindow.setTabOrder(self.videoSourceList, self.audioSourceList)
        FreeseerMainWindow.setTabOrder(self.audioSourceList, self.talkList)
        FreeseerMainWindow.setTabOrder(self.talkList, self.audioFeedbackCheckbox)
        FreeseerMainWindow.setTabOrder(self.audioFeedbackCheckbox, self.audioFeedbackSlider)
        FreeseerMainWindow.setTabOrder(self.audioFeedbackSlider, self.tabWidget)

    def retranslateUi(self, FreeseerMainWindow):
        FreeseerMainWindow.setWindowTitle(QtGui.QApplication.translate("FreeseerMainWindow", "freeseer - video studio in a backpack", None, QtGui.QApplication.UnicodeUTF8))
        self.recordButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Record", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceLabel.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Device:", None, QtGui.QApplication.UnicodeUTF8))
        self.videoDeviceList.setToolTip(QtGui.QApplication.translate("FreeseerMainWindow", "Device to use when recording.  This is ignored if xvimagesrc is used.", None, QtGui.QApplication.UnicodeUTF8))
        self.videoSourceList.setToolTip(QtGui.QApplication.translate("FreeseerMainWindow", "Video Source to use when recording.", None, QtGui.QApplication.UnicodeUTF8))
        self.audioSourceList.setToolTip(QtGui.QApplication.translate("FreeseerMainWindow", "Audio Source to use when recording.", None, QtGui.QApplication.UnicodeUTF8))
        self.talkLabel.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.talkList.setToolTip(QtGui.QApplication.translate("FreeseerMainWindow", "Title of the presentation being recorded.  For example \"Thanh Ha - Introduction to Freeseer\"", None, QtGui.QApplication.UnicodeUTF8))
        self.audioFeedbackCheckbox.setToolTip(QtGui.QApplication.translate("FreeseerMainWindow", "Enable audio feedback (plays back recording audio to speakers)", None, QtGui.QApplication.UnicodeUTF8))
        self.audioFeedbackCheckbox.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Enable audio feedback", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), QtGui.QApplication.translate("FreeseerMainWindow", "main", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("FreeseerMainWindow", "Add Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Room", None, QtGui.QApplication.UnicodeUTF8))
        self.timeEdit.setDisplayFormat(QtGui.QApplication.translate("FreeseerMainWindow", "hh:mm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Presenter", None, QtGui.QApplication.UnicodeUTF8))
        self.addTalkButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "add", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("FreeseerMainWindow", "Titles", None, QtGui.QApplication.UnicodeUTF8))
        self.editTalkList.setSortingEnabled(True)
        self.removeTalkButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "remove", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.resetButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.editTalksPage), QtGui.QApplication.translate("FreeseerMainWindow", "edit talks", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("FreeseerMainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("FreeseerMainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("FreeseerMainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("FreeseerMainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("FreeseerMainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

