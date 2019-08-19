from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon

from gameService import Game

from constants import BUTTON_SIZE, ICONS, BOMB, WINDOW_NAME, BUTTON_COLOR_UNCOVERED, BUTTON_COLOR_COVERED


class GUI(QWidget):
    def __init__(self, service):
        QWidget.__init__(self)
        self.__listButtons = []
        self.__len_rows = service.getNuberOfRows()
        self.__len_cols = service.getNuberOfRows()
        self.__service = service
        self.__setUp()

    def __setButtonCovered(self, button):
        button.setStyleSheet(BUTTON_COLOR_COVERED)

    def __setButtonUncovered(self, button):
        row, col = self.__whichButton(button)
        value = self.__service.getMainBoard()[row][col]
        # print(value)
        button.setIcon(QIcon(ICONS[value]))
        button.setStyleSheet(BUTTON_COLOR_UNCOVERED)

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
        new_button.setStyleSheet(BUTTON_COLOR_COVERED)
        self.__setButtonUncovered(new_button)

    def __setUp(self):
        self.setWindowTitle(WINDOW_NAME)
        self.setFixedSize(self.__len_cols * BUTTON_SIZE, self.__len_rows * BUTTON_SIZE + BUTTON_SIZE)
        # set up the buttons
        for i in range(self.__len_rows):
            for j in range(self.__len_cols):
                self.__createNewButton(i, j)

    def __onClickButton(self):
        sender = self.sender()
        print(sender.objectName())
        row, col = self.__whichButton(sender)
        print('value: ', self.__service.getMainBoard()[row][col])
        # print(self.__listButtons)
        # for i in self.__service.getMainBoard():
        #     print(i)
        # self.__setButtonUncovered(sender)

