'''
Created on Sep 17, 2013

@author: Incalza Dario
'''

class PlotController(object):

    def __init__(self,plotWidget,statPlot):
        self.__plotWidget = plotWidget
        self.__statPlot = statPlot
    def clearBiasPlot(self):
        self.__plotWidget.canvas.ax.cla()
    def clearDeltaPlot(self):
        self.__statPlot.canvas.getAx_i().cla()
        self.__statPlot.canvas.getAx_v().cla()
    def plotIV_bias(self,Id,V):
        
        Id = [abs(float(x)) for x in Id]
        
        self.__plotWidget.canvas.ax.set_title("Bias I-V Curve")
        self.__plotWidget.canvas.ax.set_xlabel("V_gate [V]")
        self.__plotWidget.canvas.ax.set_ylabel("I [A]")
        self.__plotWidget.canvas.ax.set_yscale('log')
        self.__plotWidget.canvas.ax.grid(True)
        self.__plotWidget.canvas.ax.plot(V,Id,'g',label='I_ds')
        
        self.__plotWidget.canvas.draw()
    
    def saveCurrentPlot(self,savepath):
        self.__plotWidget.canvas.getFig().savefig(savepath,dpi=150)
    
    def plotDeltaStat(self,delta_i,delta_v,delta_t):
        
        self.clearDeltaPlot()
        delta_i = [float(i)*1e6 for i in delta_i]
        
        self.__statPlot.canvas.getAx_i().set_title("Delta I_on")
        self.__statPlot.canvas.getAx_i().set_ylabel("Delta I_On [uA]")
        self.__statPlot.canvas.getAx_i().set_xscale('log')
        self.__statPlot.canvas.getAx_i().grid(True)
        self.__statPlot.canvas.getAx_i().scatter(delta_t,delta_i,marker='o')
        
        self.__statPlot.canvas.getAx_v().set_title("Delta V_on")
        self.__statPlot.canvas.getAx_v().set_xlabel("Time [s]")
        self.__statPlot.canvas.getAx_v().set_ylabel("Delta V_on [V]")
        self.__statPlot.canvas.getAx_v().set_xscale('log')
        self.__statPlot.canvas.getAx_v().grid(True)
        self.__statPlot.canvas.getAx_v().scatter(delta_t,delta_v,marker='o')
        
        self.__statPlot.canvas.draw()
        

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
        
    def interpolateCurrent(self,index_1,index_2,Id,V,v_on):
        v1 = float(V[index_1])
        v2 = float(V[index_2])
        i1 = float(Id[index_1])
        i2 = float(Id[index_2])
        return i1+((i2-i1)/(v2-v1))*(v_on-v1)
    
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