from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QImage
from constants import WINDOW_NAME


import sys
from PyQt5.QtWidgets import QApplication
from gameService import *
from gui import *


class StartApp(QWidget):

    def __init__(self, parent=None):
        super(StartApp, self).__init__(parent)

        self.setWindowTitle('start window')
        self.setFixedSize(400, 400)

        self.setStyleSheet('''
                       
            QWidget{
                background-color: #506477;
            }
        
            QLabel{
                margin-left: 93px;
                color: white;
                font-size: 30px;
            }
        
            QPushButton{
                background-color: #423D26;
                color: white;
                border-radius: 20px;
                border: 2px solid black;
                font-size: 23px;
                margin: 3px;
            }
        ''')

        vertical = QVBoxLayout()

        title = QLabel('MineSweeper')
        vertical.addWidget(title)

        start = QPushButton()
        start.setText('start')
        start.setFixedHeight(50)
        start.clicked.connect(self.__start_game)
        vertical.addWidget(start)

        score = QPushButton()
        score.setText('score')
        score.setFixedHeight(50)
        vertical.addWidget(score)

        settings = QPushButton()
        settings.setText('settings')
        settings.setFixedHeight(50)
        vertical.addWidget(settings)

        self.setLayout(vertical)

    def __start_game(self):
        service = Game()
        self.__gui = GUI(service)
        self.__gui.show()
