'''
Created on Sep 17, 2013

@author: Incalza Dario
'''
'''
This class is capable of plotting data in the plotwidget
''' 
from collections import OrderedDict
class PlotController(object):

    def __init__(self,plotWidget,statPlot):
        self.__plotWidget = plotWidget
        self.__statPlot = statPlot
    def clearBiasPlot(self):
        self.__plotWidget.canvas.ax.cla()
    def clearDeltaPlot(self):
        self.__statPlot.canvas.getAx_i().cla()
        self.__statPlot.canvas.getAx_v().cla()
    def plotIV_bias(self,Id,V,direction):
        Id = [abs(float(x)) for x in Id]
        self.__plotWidget.canvas.ax.set_title("Bias I-V Curve")
        self.__plotWidget.canvas.ax.set_xlabel("Vgs [V]")
        self.__plotWidget.canvas.ax.set_ylabel("Ids [A]")
        self.__plotWidget.canvas.ax.set_yscale('log')
        self.__plotWidget.canvas.ax.grid(True)
        
        if direction == "positive":
            self.__plotWidget.canvas.ax.plot(V,Id,'b',label='+1 MV/cm')
        else:
            self.__plotWidget.canvas.ax.plot(V,Id,'r',label='-1 MV/cm')
        self.__plotWidget.canvas.draw()
        
    def setBiasLegend(self):
        handles, labels = self.__plotWidget.canvas.ax.get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        self.__plotWidget.canvas.ax.legend(by_label.values(), by_label.keys(),loc='upper left')
        self.__plotWidget.canvas.draw()
        
    def setDeltaLegend(self):
        handles1, labels1 = self.__statPlot.canvas.getAx_i().get_legend_handles_labels()
        by_label1 = OrderedDict(zip(labels1, handles1))
        self.__statPlot.canvas.getAx_i().legend(by_label1.values(), by_label1.keys(),loc='lower left',scatterpoints=1)
        
        handles2, labels2 = self.__statPlot.canvas.getAx_v().get_legend_handles_labels()
        by_label2 = OrderedDict(zip(labels2, handles2))
        self.__statPlot.canvas.getAx_v().legend(by_label2.values(), by_label2.keys(),loc='lower left',scatterpoints=1)
        
        self.__statPlot.canvas.draw()
        
    def saveCurrentPlot(self,savepath):
        self.__plotWidget.canvas.getFig().savefig(savepath,dpi=150)
    
    def plotDeltaStat(self,delta_i,delta_v,delta_t,direction):
       
        delta_i = [float(i)*1e6 for i in delta_i] #transform values to the micro unit
        
        self.__statPlot.canvas.getAx_i().set_title("$\Delta  I_{on}$")
        self.__statPlot.canvas.getAx_i().set_ylabel("$\Delta  I_{on}$ [uA]")
        self.__statPlot.canvas.getAx_i().set_xscale('log')
        self.__statPlot.canvas.getAx_i().grid(True)
        
        self.__statPlot.canvas.getAx_v().set_title("$\Delta  V_{on}$")
        self.__statPlot.canvas.getAx_v().set_xlabel("Time [s]")
        self.__statPlot.canvas.getAx_v().set_ylabel("$\Delta  V_{on}$ [V]")
        self.__statPlot.canvas.getAx_v().set_xscale('log')
        self.__statPlot.canvas.getAx_v().grid(True)
        
        if direction == "positive":
            self.__statPlot.canvas.getAx_i().scatter(delta_t,delta_i,color='b',marker='o',label="+1 MV/cm $\Delta I_{on}$")
            self.__statPlot.canvas.getAx_v().scatter(delta_t,delta_v,color='b',marker='o',label="+1 MV/cm $\Delta V_{on}$")
        else:
            self.__statPlot.canvas.getAx_i().scatter(delta_t,delta_i,color='r',marker='o',label="-1 MV/cm $\Delta I_{on}$")
            self.__statPlot.canvas.getAx_v().scatter(delta_t,delta_v,color='r',marker='o',label="-1 MV/cm $\Delta V_{on}$")
            
        self.__statPlot.canvas.draw()
        
'''
This class is responsible for calculating all statistics.
'''
class StatisticsController(object):
    
    def __init__(self,ui):
        self.__ui = ui
    
    def calculate_v_on(self,Id,V,currVon):
        #if the first element in the voltage array is not greater than the last one it means that the greatest value is on the end of the array.
        # we should reverse the array, as we want to start searching from the highest values towards the lower.
        if not float(V[0]) > float(V[len(V)-1]):
            V = V[::-1]
            Id = Id[::-1]
        
        for i_d in Id:
            if float(i_d) == float(currVon): #exceptional case that the measured currents contains the currVon value
                return V[Id.index(i_d)]
            elif float(i_d) < currVon:
                index_2 = Id.index(i_d)
                index_1 = index_2 -1
                return self.interpolateVoltage(index_1,index_2,Id,V,currVon)
            
    def interpolateVoltage(self,index_1,index_2,Id,V,currVon):   
        v1 = float(V[index_1])
        v2 = float(V[index_2])
        i1 = float(Id[index_1])
        i2 = float(Id[index_2])
        return v1+((v2-v1)/(i2-i1))*(currVon-i1)
        
    def interpolateCurrent(self,index_1,index_2,Id,V,v_def):
        v1 = float(V[index_1])
        v2 = float(V[index_2])
        i1 = float(Id[index_1])
        i2 = float(Id[index_2])
        return i1+((i2-i1)/(v2-v1))*(v_def-v1)
    
    def calculate_i_on(self,Id,V,v_on):
        
        #if the first element in the voltage array is not greater than the last one it means that the greatest value is on the end of the array.
        # we should reverse the array, as we want to start searching from the highest values towards the lower.
        if not float(V[0]) > float(V[len(V)-1]):
            V = V[::-1]
            Id = Id[::-1]
        
        for v in V:
            if float(v) == v_on: #exceptional case that the measured currents contains the currVon value
                return Id[V.index(v)]
            elif float(v) < v_on:
                index_2 = V.index(v)
                index_1 = index_2 -1
                return self.interpolateCurrent(index_1,index_2,Id,V,v_on)
        
    def calculateStatistics(self,Id,V,currVon,voltIon):
        Id = [abs(float(x)) for x in Id]
        v_on = self.calculate_v_on(Id,V,float(currVon))
        i_on = self.calculate_i_on(Id, V, float(voltIon))
        return (i_on,v_on)