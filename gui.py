import sys
from PyQt4 import QtGui, QtCore
import random


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()  # parent object QMainWindow
        self.passlist = []

        self.length = QtGui.QLineEdit(self)   #input box to enter field 
        self.length.setGeometry(50,50,30,20)
        self.length.move(255,70)        
        
        self.textbr = QtGui.QTextBrowser(self) # display output box      
        self.textbr.setGeometry(210,90,230,20)
        self.textbr.move(255,90)    

        text2 = QtGui.QLabel("Enter Length(Max 30 {digits}):",self)   #input box label
        text2.setGeometry(100,50,230,20)
        text2.move(40,70)
        
        
        text1 = QtGui.QLabel("Password Generated:",self)
        text1.setGeometry(100,50,140,20)
        text1.move(40,90)
        
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Safe Password Generator")
        self.setWindowIcon(QtGui.QIcon('favicon-32x32.png'))

        extractAction = QtGui.QAction("&Close", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Closing Application!')
        extractAction.triggered.connect(self.close_application)

        extractAction2 = QtGui.QAction("&Save to random.txt", self)
        self.progress = QtGui.QProgressBar(self)                                # progress bar
        self.progress.setGeometry(200,80,250,20)
        self.progress.move(100,150)
        extractAction2.setShortcut("Ctrl+S")
        extractAction2.setStatusTip('Saving Passwords!')                         
        extractAction2.triggered.connect(self.save_application)                 # to save file on the desktop
        
        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu = mainMenu.addMenu('&Save')
        fileMenu.addAction(extractAction2)
 
        self.home()
       
    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application) # custom close :)
        btn.move(200,200)

        btn2 = QtGui.QPushButton("Generate", self)
        btn2.clicked.connect(self.random_gen)
        btn2.move(100,200)

        checkBox = QtGui.QCheckBox('Lowercase', self)
        checkBox.toggle()
        checkBox.stateChanged.connect(self.all_lowercase)
        checkBox.move(200,40)

        self.string = 'abcdefghijklmnopqrstuvwxyz!@#$%&*'
        self.show()

    def all_lowercase(self, state):
        if state == QtCore.Qt.Checked:
            self.string = 'abcdefghijklmnopqrstuvwxyz!@#$%&*'
        else:
            self.string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*'
     

    def close_application(self):             # alert box
        choice = QtGui.QMessageBox.question(self, 'Quit Alert',    
                                            "Are you Sure?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    
    
    def save_application(self):
        num = 0
        self.completed = 0
        while self.completed < 100:         # custom output file generation.
            f = open('random.txt', 'w')
            for txt in self.passlist:
                num += 1
                f.write("%s Password Generated: %s\n" % (num ,txt))
            f.close()
            self.completed = 100
            self.progress.setValue(self.completed)
        
    
    def random_gen(self):
                        # custom method to generate random passwords   
        final_len = self.length.text()
        if final_len  is '':
            final_len = 4
        else:
            pass
        passw = "".join(random.sample(self.string,int(final_len)))
        self.passlist.append(passw)
        self.textbr.setText(passw)
    
def main():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


main()
