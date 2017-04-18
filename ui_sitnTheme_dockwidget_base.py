# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projets\sitnThemes\sitnTheme_dockwidget_base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_sitnThemesDockWidgetBase(object):
    def setupUi(self, sitnThemesDockWidgetBase):
        sitnThemesDockWidgetBase.setObjectName(_fromUtf8("sitnThemesDockWidgetBase"))
        sitnThemesDockWidgetBase.resize(123, 484)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sitnThemesDockWidgetBase.sizePolicy().hasHeightForWidth())
        sitnThemesDockWidgetBase.setSizePolicy(sizePolicy)
        self.dockWidgetContents = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listThemes = QtGui.QListWidget(self.dockWidgetContents)
        self.listThemes.setAutoFillBackground(False)
        self.listThemes.setIconSize(QtCore.QSize(110, 60))
        self.listThemes.setObjectName(_fromUtf8("listThemes"))
        self.gridLayout.addWidget(self.listThemes, 0, 1, 1, 1)
        sitnThemesDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(sitnThemesDockWidgetBase)
        QtCore.QMetaObject.connectSlotsByName(sitnThemesDockWidgetBase)

    def retranslateUi(self, sitnThemesDockWidgetBase):
        sitnThemesDockWidgetBase.setWindowTitle(_translate("sitnThemesDockWidgetBase", "Thèmes du SITN", None))

