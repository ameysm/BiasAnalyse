'''
Created on Sep 20, 2013

@author: adminssteudel
'''
from py2exe.build_exe import py2exe
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT
from distutils.core import setup
import matplotlib

d_files = matplotlib.get_py2exe_datafiles()
d_files.append('splash.png')
d_files.append('imec.png')


setup(
      windows=[{"script" : "main.py"}],
      data_files=d_files,
      options={"py2exe" : {"includes" : ["PyQt4.QtGui",
                                         "PyQt4.QtCore",
                                         "matplotlib.figure","matplotlib.backends.backend_qt4agg",
                                         "matplotlib.backends.backend_qt4"],
                           "excludes" : [],
                           "dll_excludes": ["MSVCP90.dll"]}})