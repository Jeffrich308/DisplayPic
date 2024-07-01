# -------------------------------------------------------------------------------
# Name:             DisplayPic.py
# Purpose:          Simple dataBase app to save text and a photo
#
# Author:           Jeffreaux
#
# Created:          28June24
#
# Required Packages:    PyQt5, PyQt5-Tools
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QLabel
from PyQt5 import uic
from fileModule import *
from PyQt5.QtGui import QPixmap

import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("DisplayPic_GUI.ui", self)

        # define Widgets
        self.btnLoadPhoto = self.findChild(QPushButton, "btnLoadPhoto")
        self.btnExit = self.findChild(QPushButton, "btnExit")

        self.actExit = self.findChild(QAction, "actExit")

        self.lblFileName = self.findChild(QLabel, "lblFileName")
        self.lblPhoto = self.findChild(QLabel, "lblPhoto")

        # Define the actions
        self.btnExit.clicked.connect(self.closeEvent)
        self.btnLoadPhoto.clicked.connect(self.show_pic)    

        self.actExit.triggered.connect(self.closeEvent)
        
        # Show the app
        self.show()

    
    def show_pic(self):
        print("Going get file")
        fname = getFullFilename_txt(self)  # Select pic file to display
        print(fname)
        self.lblFileName.setText(fname)  # Display filename
        photo = QPixmap(fname)  # Create a Pixmap object
        picHeight = photo.height()
        picWidth = photo.width()

        if picWidth > picHeight:  # 
            scaled_photo = photo.scaledToWidth(250, 0) # This value is from the size of the label container
            print("Scaled by width")
            self.lblPhoto.setPixmap(scaled_photo)
        else:
            scaled_photo = photo.scaledToHeight(250, 0)
            print("Scaled to Height")
            self.lblPhoto.setPixmap(scaled_photo)
                
    
    def closeEvent(self, *args, **kwargs):
        # print("Program closed Successfully!")
        self.close()


# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
