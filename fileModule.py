from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QFileDialog
from PyQt5 import uic
import sys
import os
from pathlib import Path


# Declare in main program - "from fileModule import *

# -------------------------------------------------------------------------------
#  Will return the number of subdirectories from the root of given path
#  path must be sent
#
#  Created: 18June24
# -------------------------------------------------------------------------------

def subCount(self, path):
    ctr = 0
    for root, dirs, files in os.walk(path):
        for x in dirs:
            #ctr = 0
            #print(root + "\\" + x)
            ctr = ctr + 1
            #print(ctr)

    print("final Count", ctr)
    return(ctr)


# -------------------------------------------------------------------------------
#  Will return a list of the subdirectories/folder in the current directory that was sent
#
#  Created: 18June24
# -------------------------------------------------------------------------------

def subCountCurrent(self, home_folder):
    p = Path(home_folder)
    #print(p)
    d = [f.name for f in p.iterdir() if f.is_dir()]
    c = 0
    for x in d:
         #print(x)
         c += 1
         print(c)
    #print(d)
    return(d)

    #p = home_folder
    #print(home_folder)



# -------------------------------------------------------------------------------
#  Will return the path selected
#  path must be sent
#
#  Created: 18Jun24
# -------------------------------------------------------------------------------

def getPath(self):     
        #print("Choosing Path")
        dialog = QFileDialog()
        f_path = dialog.getExistingDirectory(None,"Select folder")
        #print(f_path)
        return(f_path)




# -------------------------------------------------------------------------------
#  Will return the filename only 
#  path must be sent
#
#  Created: 18Jun24
# -------------------------------------------------------------------------------

def getFilename_txt(self):
    print("Filename returned")
    fname = QFileDialog.getOpenFileName(self, "Select File", "", "Text File (*.txt)" )
    filePath =str(fname[0])
    fileOnly = filePath.split("/")[-1]

    print(filePath)
    print(fileOnly)
    return(fileOnly)



# -------------------------------------------------------------------------------
#  Will return the path and filenam 
#  path must be sent
#
#  Created: 18Jun24
# -------------------------------------------------------------------------------

def getFullFilename_txt(self):
    #print("Filename returned")
    fname = QFileDialog.getOpenFileName(self, "Select File", "", "PNG File (*.png) ;; JPG Files (*.jpg) ;; JPEG Files (*.jpeg) ;; GIF Files (*.gif)")
    filePath =str(fname[0])
    fileOnly = filePath.split("/")[-1]

    #print(filePath)
    #print(fileOnly)
    return(filePath)