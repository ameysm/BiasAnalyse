'''
Created on Sep 18, 2013

@author: adminssteudel
'''

'''
Created on Sep 6, 2013

@author: Incalza Dario
'''

from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT
 
class MplCanvas(FigureCanvas):
 
    def __init__(self):
        self.fig = Figure()
        self.ax_i = self.fig.add_subplot(211)
        self.ax_v = self.fig.add_subplot(212)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
    
    def getFig(self):
        return self.fig
    
    def getAx_i(self):
        return self.ax_i
    
    def getAx_v(self):
        return self.ax_v
 
class statplotlibWidget(QtGui.QWidget):
 
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.canvas.ax_i.set_title("$\Delta  I_{on}$")
        self.canvas.ax_i.set_ylabel("$\Delta$ I")
        
        self.canvas.ax_v.set_title("$\Delta V_{on}$")
        self.canvas.ax_v.set_xlabel("Time [s]")
        self.canvas.ax_v.set_ylabel("$\Delta$ V")
        
        self.toolbar = NavigationToolbar2QT(self.canvas, None, True)
        self.vbl = QtGui.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.vbl.addWidget(self.toolbar)
        self.setLayout(self.vbl)
