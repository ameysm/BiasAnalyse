'''
Created on Sep 16, 2013

@author: Incalza Dario
'''

from PyQt4 import QtGui
import sys
from BiasAnalyse import BiasAnalyse
'''
Entry point of BiasAnalyse
'''
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.processEvents()
    controller = BiasAnalyse()
    controller.show()
    sys.exit(app.exec_())

