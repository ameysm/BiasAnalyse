'''
Created on Sep 16, 2013

@author: Incalza Dario
'''
from PyQt4 import QtGui,QtCore
from bias_analyse import Ui_MainWindow
from Data import BiasPacket
from Controllers import PlotController,StatisticsController
from threading import Thread
'''
Main program class. 
'''
class BiasAnalyse(QtGui.QMainWindow):
    
    #default values
    CURR_V_ON = "1e-11"
    VOL_I_ON = "19.8"
    
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()    #note: instance, not the class
        self.ui.setupUi(self)
        self.filePath = None
        self.pathRoot = QtCore.QDir.rootPath()
        modfilter=["*.bias"]
        self.model = QtGui.QFileSystemModel(self)
        self.model.setNameFilters(modfilter)
        self.model.setRootPath("C:\\BIAS_DATA")
        self.indexRoot = self.model.index(self.model.rootPath())
        self.treeView = self.ui.treeView
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.indexRoot)
        #self.treeView.clicked.connect(self.on_treeView_clicked)
        self.treeView.doubleClicked.connect(self.on_treeView_clicked)
        self.ui.resetStatConst.clicked.connect(self.initStatistics)
        self.ui.calcStat.clicked.connect(self.calculatedata)
        self.__plotController = PlotController(self.ui.plotwidget,self.ui.statPlot)
        self.__statController = StatisticsController(self.ui)
        self.initStatistics()
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())
        self.filePath = str(self.model.filePath(indexItem))

        if self.filePath.endswith(".bias"):
            plot_msg = QtCore.QString("Do you want to plot the data from : "+self.filePath)
            reply = QtGui.QMessageBox.question(None, QtCore.QString("Plot data"), plot_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.calculatedata()
            else:
                return
    
    def clearStatTable(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
            
    def initStatistics(self):
        self.ui.current_v_on.setText(BiasAnalyse.CURR_V_ON)
        self.ui.voltage_i_on.setText(BiasAnalyse.VOL_I_ON)
        
    def calculatedata(self):
        self.clearStatTable()
        if self.filePath == None:
            QtGui.QMessageBox.warning(None, QtCore.QString("No bias file"), QtCore.QString("No bias file was selected, so there is nothing to calculate."), QtGui.QMessageBox.Ok)
            return
        delta_i = []
        delta_v = []
        delta_t = []
        self.__plotController.clearBiasPlot()
        self.__plotController.clearDeltaPlot()
        datadict = self.parseBiasFile(self.filePath)
        if datadict == None:
            return
        try:
            t_0 = self.__statController.calculateStatistics(datadict[0].getDrainList(),datadict[0].getVoltageList(),str(self.ui.current_v_on.text()),str(self.ui.voltage_i_on.text())) 
        except ValueError:
            QtGui.QMessageBox.warning(None, QtCore.QString("ValueError"), QtCore.QString("Please make sure Current V_on and Voltage I_on are numerical values."), QtGui.QMessageBox.Ok)
            return
        del datadict[0]
        for key in sorted(datadict):
            Id = datadict[key].getDrainList()
            v = datadict[key].getVoltageList()
            thread = Thread(target=self.__plotController.plotIV_bias,args=(Id, v))
            thread.start()
            t= self.__statController.calculateStatistics(Id,v,str(self.ui.current_v_on.text()),str(self.ui.voltage_i_on.text()))
            delta_i.append(t[0]-t_0[0])
            delta_v.append(t[1]-t_0[1])
            delta_t.append(key)
            self.insertStatinTable(key, t[0]-t_0[0], t[1]-t_0[1])
            
        thread2 = Thread(target=self.__plotController.plotDeltaStat,args=(delta_i, delta_v, delta_t))
        thread2.start()
        self.addToOverview(t[0]-t_0[0], t[1]-t_0[1])
    
    def addToOverview(self,i_on,v_on):
        lastrow = self.ui.statTable.rowCount()
        self.ui.statTable.insertRow(lastrow)
        path = QtGui.QTableWidgetItem(self.filePath)
        i__on = QtGui.QTableWidgetItem(str(i_on))
        v__on = QtGui.QTableWidgetItem(str(v_on))
        self.ui.statTable.setItem(lastrow,0,path)
        self.ui.statTable.setItem(lastrow,1,v__on)
        self.ui.statTable.setItem(lastrow,2,i__on)      
        
    def insertStatinTable(self,timestamp,delta_i,delta_v):
        lastrow = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(lastrow)
        timestamp = QtGui.QTableWidgetItem("[0-"+str(timestamp)+"]")
        delta_i = QtGui.QTableWidgetItem(str(delta_i))
        delta_v = QtGui.QTableWidgetItem(str(delta_v))
        # .setItem(row, column, item)
        self.ui.tableWidget.setItem(lastrow, 0, timestamp)
        self.ui.tableWidget.setItem(lastrow, 1, delta_i)
        self.ui.tableWidget.setItem(lastrow, 2, delta_v)
        
    def parseBiasFile(self,filepath):
        myfile = open(filepath,'r')
        file_content = myfile.readlines()
        datadict = dict()
        boolInSweep = False
        tempSweep = None
        temp_Ig_list = []
        temp_Id_list = []
        temp_V_list = []
        
        for line in file_content:
            if "SWEEP ON T" in line:
                tempSweep = [int(s) for s in line.split() if s.isdigit()][0] #get the sweep timestamp from i.e : [SWEEP ON T = 31 ], tempSweep will hold integer 31
                boolInSweep = True
            elif "SWEEP END" in line:
                datadict[tempSweep]=BiasPacket(temp_Ig_list,temp_Id_list,temp_V_list)
                tempSweep = None
                boolInSweep = False
                temp_Ig_list = []
                temp_Id_list = []
                temp_V_list = []
            elif boolInSweep == True:
                values = line.split("\t")
                try:
                    temp_Id_list.append(float(values[0]))
                    temp_Ig_list.append(float(values[1]))
                    temp_V_list.append(float(values[2]))
                except IndexError:
                    print "index error : "+line
        myfile.close()
        if len(datadict.keys()) == 0:
            QtGui.QMessageBox.warning(None, QtCore.QString("DataError"), QtCore.QString("Seems like the data file is corrupt or misses sweep data. "), QtGui.QMessageBox.Ok)
            return None
        return datadict
                