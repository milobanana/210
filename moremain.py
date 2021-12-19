from os import close
import sys
from time import clock
from typing import Counter
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow

###############
import platform

import psutil
import time
import re
import uuid
###############

#Globals
counter = 0


class pp(QMainWindow):
    def __init__(self):
        super(pp, self).__init__()
        loadUi("pp.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.gridLayout_2.setStyleSheet("background: transparent;")
            

####################################################
        self.exitButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.doAllbotton)

        self.data_animate()

        #output data system
    def data_animate(self):
        self.platform_2.setText(platform.system())
        
        self.arcitecture.setText(platform.machine())
        self.host_name_2.setText(platform.node())
            
        self.address_2.setText(':'.join(re.findall('..',
                                                      '%012x' % uuid.getnode())))
        
        self.processor_2.setText(platform.processor())
        self.ram_2.setText(str(
                round(psutil.virtual_memory().total / (1024.0 ** 3)))+" GB")


    
        
        # self.platform_2.setText(platform.system())
        # self.arcitecture.setText(platform.machine())
        # self.host_name_2.setText(platform.node())
            
        # self.address_2.setText(platform.machine())##
        
        # self.processor_2.setText(platform.processor())
        # self.ram_2.setText(ram)
    def doAllbotton(self):

        # SHOW MAIN WINDOW
        self.main = doAll()
        self.main.show()

        # CLOSE SPLASH SCREEN
        self.close()

        
class doAll(QMainWindow):
    def __init__(self):
        super(doAll, self).__init__()
        loadUi("doAll.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.exitButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.backbotton)

        #set new type data
        self.label_16.setText("Round")
        self.label_18.setText("CRU")
        self.label_17.setText("Create")
            
        self.label_22.setText("Read")
        
        self.label_23.setText("Write")
        self.label_24.setText("Delete")


    def backbotton(self):

        # SHOW MAIN WINDOW
        self.main = pp()
        self.main.show()

        # CLOSE SPLASH SCREEN
        self.close()
        

        
    # def close(self):
    #     self.close()

# class doAll(QMainWindow):
#     def __init__(self):
#         super(doAll, self).__init__()
#         loadUi("doAll.ui",self)

    
 



############################################

class splashprogram(QMainWindow):
    def __init__(self):
        super(splashprogram, self).__init__()
        loadUi("splashprogram.ui",self)
        self.splashframe.setStyleSheet("background-color: transparent;")

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(10)


    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = pp()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1






# main
app = QApplication(sys.argv)
welcome = splashprogram()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(800)


#Remove title bar
widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)



widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")