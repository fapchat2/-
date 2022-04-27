
import sys
# from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
#                              QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
#                              QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
#                              QVBoxLayout)
from PyQt5 import QtWidgets, QtCore

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

import design  # Это наш конвертированный файл дизайна


class MainWindow(QMainWindow, design.Ui_MainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        UI->export_2.clicked.connect(self.chooseAFile)  # Выполнить функцию browse_folder
    def chooseAFile(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self, "Choose a file")


class LogInformationWindow(QMainWindow):
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
        self.resize(470, 200)
        self.centralWidget = QLabel("Файл лога не найден. Файл будет создан автоматически")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)

        button=QtWidgets.QPushButton("OK", self)
        button.move(200,160)
        button.clicked.connect(self.close)


    # def log(self):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    try:
        open('script18.log', 'rt')
    except IOError as err:
        log = LogInformationWindow(sys.argv)
        log.show()
        open('script18.log', 'w')    
    sys.exit(app.exec_())



