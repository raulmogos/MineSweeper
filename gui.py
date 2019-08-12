from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow, QMenu
from PyQt5.QtGui import QIcon

from gameService import Game

from constants import BUTTON_SIZE, ICONS, BOMB, WINDOW_NAME


class GUI(QMainWindow):
    def __init__(self, service):
        QMainWindow.__init__(self)
        self.__menu = self.menuBar()
        self.__listButtons = []
        self.__len = service.getNuberOfRows()
        self.__service = service
        self.__setUp()

    def __setButtonCovered(self, button):
        button.setIcon(QIcon())

    def __setButtonUncovered(self, button):
        row, col = self.__whichButton(button)
        value = self.__service.getMainBoard()[row][col]
        button.setIcon(QIcon(ICONS[value]))

    def __createButtonNameConvention(self, row, col):
        return str(row) + '-' + str(col)

    def __whichButton(self, button):
        indexes = button.objectName().split('-')
        return int(indexes[0]), int(indexes[1])

    def __createNewButton(self, row, col):
        place_row = row * BUTTON_SIZE + BUTTON_SIZE
        place_col = col * BUTTON_SIZE
        new_button = QtWidgets.QPushButton(self)
        new_button.resize(BUTTON_SIZE, BUTTON_SIZE)
        new_button.move(place_col, place_row)
        new_button.setObjectName(self.__createButtonNameConvention(row, col))
        self.__setButtonCovered(new_button)
        new_button.clicked.connect(self.__onClickButton)
        self.__listButtons.append(new_button)

    def __setUp(self):
        self.setWindowTitle(WINDOW_NAME)
        self.setFixedSize(self.__len * BUTTON_SIZE, self.__len * BUTTON_SIZE + BUTTON_SIZE)
        # set up the buttons
        for i in range(self.__len):
            for j in range(self.__len):
                self.__createNewButton(i, j)

    def __onClickButton(self):
        sender = self.sender()
        print(sender.objectName())
        print(self.__listButtons)
        for i in self.__service.getMainBoard():
            print(i)
        self.__setButtonUncovered(sender)
