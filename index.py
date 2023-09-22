import sys
from PyQt6.QtWidgets import QApplication, QWidget


class SaveSafe(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(300, 300, 650, 650)
        self.setWindowTitle("Save Safe")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = SaveSafe()
    sys.exit(app.exec())
