#!/usr/bin/python
import sys
import os
import time
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    dir_ = "None"

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(250, 300, 400, 400)
        self.setWindowTitle("pyporg")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.setFixedHeight(400)
        self.setFixedWidth(400)
        
        mainMenu = self.menuBar()

        file = mainMenu.addMenu("File")
        open = QtGui.QAction("Open", self)
        open.setShortcut("Ctrl+O")
        open.setStatusTip("Open a folder to sort")
        open.triggered.connect(self.openFolder)
        file.addAction(open)
            
        save = QtGui.QAction("Save",self)
        save.setShortcut("Ctrl+S")
        save.setStatusTip("Save the output log to a file")
        save.triggered.connect(self.saveFile)
        file.addAction(save)
            
        quit = QtGui.QAction("Quit",self) 
        quit.setShortcut("Ctrl+X")
        quit.setStatusTip("Close the application")
        quit.triggered.connect(self.close_application)
        file.addAction(quit)

        help = mainMenu.addMenu("Help")
        about = QtGui.QAction("About", self)
        about.setStatusTip("About pyporg")
        #about.triggered.connect(self.OPENNEWFORM?)
        help.addAction(about)
            
        self.statusBar()    
        self.home()

    def home(self):
        lbl_ext = QtGui.QLabel("Select the file types you'd like to sort:", self)
        lbl_ext.move(10,35)
        lbl_ext.resize(lbl_ext.minimumSizeHint())

        self.chk_jpg = QtGui.QCheckBox('.jpg', self)
        self.chk_jpg.move(20, 60)
        self.chk_jpg.resize(self.chk_jpg.minimumSizeHint())

        self.chk_jpeg = QtGui.QCheckBox('.jpeg', self)
        self.chk_jpeg.move(20, 85)
        self.chk_jpeg.resize(self.chk_jpeg.minimumSizeHint())

        self.chk_img = QtGui.QCheckBox('.img', self)
        self.chk_img.move(150, 60)
        self.chk_img.resize(self.chk_img.minimumSizeHint())

        self.chk_png = QtGui.QCheckBox('.png', self)
        self.chk_png.move(150, 85)
        self.chk_png.resize(self.chk_png.minimumSizeHint())

        self.chk_bmp = QtGui.QCheckBox('.bmp', self)
        self.chk_bmp.move(280, 60)
        self.chk_bmp.resize(self.chk_bmp.minimumSizeHint())

        self.chk_tiff = QtGui.QCheckBox('.tiff', self)
        self.chk_tiff.move(280, 85)
        self.chk_tiff.resize(self.chk_tiff.minimumSizeHint())

        self.chk_del_duplicate = QtGui.QCheckBox("Delete duplicate files", self)
        self.chk_del_duplicate.move(20, 130)
        self.chk_del_duplicate.resize(self.chk_del_duplicate.minimumSizeHint())

        lbl_cwd = QtGui.QLabel("Current working directory: ", self)
        lbl_cwd.move(10, 160)
        lbl_cwd.resize(lbl_cwd.minimumSizeHint())

        self.lbl_filepath = QtGui.QLabel("                                                                              ", self)
        self.lbl_filepath.move(25, 185)
        self.lbl_filepath.resize(self.lbl_filepath.minimumSizeHint())

        self.lst_log = QtGui.QListWidget(self)
        self.lst_log.move(10,210)
        self.lst_log.resize(380,120)

        btn_open = QtGui.QPushButton("Open folder", self)
        btn_open.clicked.connect(self.openFolder)
        btn_open.resize(btn_open.minimumSizeHint())
        btn_open.move(50,340)

        btn_start = QtGui.QPushButton("Start", self)
        btn_start.clicked.connect(self.start_application)
        btn_start.resize(btn_start.minimumSizeHint())
        btn_start.move(250,340)
        self.show()

    def openFolder(self):
        Window.dir_ = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder to sort:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
        print(Window.dir_)
        self.lbl_filepath.setText(Window.dir_)

    def close_application(self):
        sys.exit()

    def start_application(self):
        try:
            file_path = Window.dir_
            file_path = os.chdir(file_path)
        except:
                self.lst_log.addItem("Please select a folder to sort first!")

        # Iterate through directory.
        for self.f in os.listdir(str(self.dir_)):
            try:
                # Split file name and file extension
                file_name, file_ext = os.path.splitext(self.f)
            except IOError:
                print('Error: file doesn\'t exist')
            else:
                # Store file mod time info
                file_stats = time.ctime(os.stat(self.f).st_mtime)
                f_day, f_month, f_date, f_time, f_year = file_stats.split()

            # Set a new folder name for f
            self.new_folder = f_year + " " + f_month
 
            if self.chk_bmp.isChecked() == True and file_ext == ".bmp":
                self.fileTransfer()
            if self.chk_img.isChecked() == True and file_ext == ".img":
                self.fileTransfer()
            if self.chk_jpeg.isChecked() == True and file_ext == ".jpeg":
                self.fileTransfer()
            if self.chk_jpg.isChecked() == True and file_ext == ".jpg":
                self.fileTransfer()
            if self.chk_png.isChecked() == True and file_ext == ".png":
                self.fileTransfer()
            if self.chk_tiff.isChecked() == True and file_ext == ".tiff":
                self.fileTransfer()

        # After checking each file in dir, let user know it's done.
        self.lst_log.addItem("Done.")

    def fileTransfer(self):
        if os.path.isdir(self.new_folder):
            self.lst_log.addItem("Moving '" + self.f + "' to '" + self.new_folder + "'")
            #print("Moving '" + self.f + "' to '" + self.new_folder + "'")
            os.rename(self.f, self.new_folder + "/" + self.f)
        else:
            self.lst_log.addItem("Creating directory: \'" + self.new_folder +"'")
            #print("Creating directory: \'" + self.new_folder +"'")
            os.makedirs(self.new_folder)
            self.lst_log.addItem("Moving '" + self.f + "' to '" + self.new_folder + "'")
            #print("Moving '" + self.f + "' to '" + self.new_folder + "'")
            os.rename(self.f, self.new_folder + "/" + self.f)

            #if del_duplicate == True:
                # Check for duplicate files and remove
    
    def saveFile(self, showDialog):
        # save to log.txt in current working directory
        savePath = os.path.join(os.getcwd(), 'log.txt')

        # allow user to override location if requested
        savePath = QtGui.QFileDialog.getSaveFileName(self, 'Save the log file', savePath, 'log.txt')

        # if just saving, or user didn't cancel, make and save file
        if len(savePath) > 0:
            with open(savePath, 'w') as theFile:
                for i in xrange(self.lst_log.count()):
                    theFile.write(''.join([str(self.lst_log.item(i).text()), '\n']))

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()




