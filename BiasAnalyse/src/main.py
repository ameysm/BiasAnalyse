'''
Created on Sep 16, 2013

@author: Incalza Dario
'''

from PyQt4 import QtGui
import sys,time
from BiasAnalyse import BiasAnalyse
'''
Entry point of BiasAnalyse
'''
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    splash_pix = QtGui.QPixmap('splash.png')
    splash = QtGui.QSplashScreen(splash_pix)
    splash.show()
    app.processEvents()
    controller = BiasAnalyse()
    time.sleep(3)
    splash.finish(controller)
    controller.show()
    sys.exit(app.exec_())
