# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bias_analyse.ui'
#
# Created: Thu Sep 19 13:38:16 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1291, 806)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 10, 451, 741))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(470, 490, 811, 261))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.overviewTab = QtGui.QWidget()
        self.overviewTab.setObjectName(_fromUtf8("overviewTab"))
        self.statTable = QtGui.QTableWidget(self.overviewTab)
        self.statTable.setGeometry(QtCore.QRect(10, 10, 781, 221))
        self.statTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.statTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.statTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.statTable.setObjectName(_fromUtf8("statTable"))
        self.statTable.setColumnCount(3)
        self.statTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.statTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.statTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.statTable.setHorizontalHeaderItem(2, item)
        self.tabWidget.addTab(self.overviewTab, _fromUtf8(""))
        self.runstatTab = QtGui.QWidget()
        self.runstatTab.setObjectName(_fromUtf8("runstatTab"))
        self.tableWidget = QtGui.QTableWidget(self.runstatTab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 361, 221))
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayoutWidget = QtGui.QWidget(self.runstatTab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(430, 20, 231, 141))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.current_v_on = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.current_v_on.setObjectName(_fromUtf8("current_v_on"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.current_v_on)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.voltage_i_on = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.voltage_i_on.setObjectName(_fromUtf8("voltage_i_on"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.voltage_i_on)
        self.calcStat = QtGui.QPushButton(self.verticalLayoutWidget)
        self.calcStat.setObjectName(_fromUtf8("calcStat"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.calcStat)
        self.resetStatConst = QtGui.QPushButton(self.verticalLayoutWidget)
        self.resetStatConst.setObjectName(_fromUtf8("resetStatConst"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.resetStatConst)
        self.verticalLayout.addLayout(self.formLayout)
        self.tabWidget.addTab(self.runstatTab, _fromUtf8(""))
        self.tabWidget_2 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(470, 10, 811, 471))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.plotwidget = matplotlibWidget(self.tab)
        self.plotwidget.setGeometry(QtCore.QRect(10, 10, 781, 431))
        self.plotwidget.setObjectName(_fromUtf8("plotwidget"))
        self.tabWidget_2.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.statPlot = statplotlibWidget(self.tab_2)
        self.statPlot.setGeometry(QtCore.QRect(10, 10, 791, 421))
        self.statPlot.setObjectName(_fromUtf8("statPlot"))
        self.tabWidget_2.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1291, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Bias Analyse", None))
        item = self.statTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "FILENAME", None))
        item = self.statTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "V_ON", None))
        item = self.statTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "I_ON", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.overviewTab), _translate("MainWindow", "Overview", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "SWEEP INTERVAL", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DELTA I_ON", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DELTA V_ON", None))
        self.label.setText(_translate("MainWindow", "Current V_On [A]", None))
        self.label_2.setText(_translate("MainWindow", "Voltage I_On [V]", None))
        self.calcStat.setText(_translate("MainWindow", "Calculate statistics", None))
        self.resetStatConst.setText(_translate("MainWindow", "Reset Defaults", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.runstatTab), _translate("MainWindow", "Run Statistics", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "BIAS PLOT", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "DELTA I_on and  V_on", None))

from matplotlibWidgetFile import matplotlibWidget
from statplotlibWidgetFile import statplotlibWidget
