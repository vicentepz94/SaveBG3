import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    #When you subclass a Qt class you must always call the super __init__ function to allow Qt to set up the object.
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SaveBG3")

        self.button_checked = True

        button = QPushButton("Testo testo!")
        button.setCheckable(True)
        button.clicked.connect(self.button_toggled)
        button.setChecked(self.button_checked)

        button.setFixedSize(QSize(120,30))

        self.setFixedSize(QSize(600,700))
        self.setMinimumSize(QSize(600,700))
        self.setMaximumSize(QSize(900,850))

        #set the central widget of the Window
        self.setCentralWidget(button)
    
    def button_toggled(self, checked):
        self.button_checked = checked
        print(self.button_checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()