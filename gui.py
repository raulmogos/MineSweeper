from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.Qt import Qt, QObject
import time
from gameService import Game

from constants import *


class GUI(QWidget):
    def __init__(self, service):
        QWidget.__init__(self)
        self.EXIT_CODE_REBOOT = -12345678
        self.__len_rows = service.getNuberOfRows()
        self.__len_cols = service.getNuberOfRows()
        self.__matrixButtons = [
            [0 for i in range(self.__len_cols)] for j in range(self.__len_rows)
        ]
        self.setMouseTracking(True)
        self.__service = service
        self.__setUp()

    def __setButtonCovered(self, button):
        button.setStyleSheet(BUTTON_COLOR_COVERED)

    def __setFlag(self, row, col):
        button = self.__matrixButtons[row][col]
        button.setEnabled(False)
        icon = QIcon()
        icon.addPixmap(QPixmap(ICONS[FLAG]), QIcon.Disabled)
        icon.addPixmap(QPixmap(ICONS[FLAG]), QIcon.Active)
        button.setIcon(icon)
        button.setStyleSheet(BUTTON_COLOR_COVERED)

    def __setButtonUncovered(self, button):
        row, col = self.__whichButton(button)
        value = self.__service.getMainBoard()[row][col]
        # print(value)
        button.setEnabled(False)
        icon = QIcon()
        icon.addPixmap(QPixmap(ICONS[value]), QIcon.Disabled)
        icon.addPixmap(QPixmap(ICONS[value]), QIcon.Active)
        button.setIcon(icon)
        button.setStyleSheet(BUTTON_COLOR_UNCOVERED)

    def __setButtonUncoveredByIndex(self, row, col):
        self.__setButtonUncovered(self.__matrixButtons[row][col])

    def __createButtonNameConvention(self, row, col):
        return str(row) + '-' + str(col)

    def __whichButton(self, button):
        indexes = button.objectName().split('-')
        return int(indexes[0]), int(indexes[1])

    def __createNewButton(self, row, col):
        place_row = row * BUTTON_SIZE
        place_col = col * BUTTON_SIZE
        new_button = QtWidgets.QPushButton(self)
        new_button.resize(BUTTON_SIZE, BUTTON_SIZE)
        new_button.move(place_col, place_row)
        new_button.setObjectName(self.__createButtonNameConvention(row, col))
        self.__setButtonCovered(new_button)
        new_button.installEventFilter(self)
        new_button.clicked.connect(self.__onClickButton)
        self.__matrixButtons[row][col] = new_button
        new_button.setStyleSheet(BUTTON_COLOR_COVERED)

    def __setUp(self):
        self.setWindowTitle(WINDOW_NAME)
        self.setFixedSize(self.__len_cols * BUTTON_SIZE, self.__len_rows * BUTTON_SIZE)
        # set up the buttons
        for i in range(self.__len_rows):
            for j in range(self.__len_cols):
                self.__createNewButton(i, j)


    def __onClickButton(self):
        sender = self.sender()
        print(sender.objectName())
        row, col = self.__whichButton(sender)
        print('value: ', self.__service.getMainBoard()[row][col])

        lst = self.__service.bfsOnBoard(row, col)

        # if QtGui.qApp.mouseButtons() and QtCore.Qt.RightButton:
        #     print(self.sender().toolTip())

        if lst == BOMB:
            print('bomb')
            self.__setButtonUncovered(sender)
            buttonReply = QMessageBox.information(self, 'you have lost', 'you have lost', QMessageBox.Close | QMessageBox.Retry)
            return

        for b in lst:
            r = b.get_row
            c = b.get_col
            self.__setButtonUncoveredByIndex(r, c)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                print(obj.objectName(), "Left click")
            elif event.button() == QtCore.Qt.RightButton:
                print(obj.objectName(), "Right click")
                r, c = self.__whichButton(obj)
                self.__setFlag(r,c)
            elif event.button() == QtCore.Qt.MiddleButton:
                print(obj.objectName(), "Middle click")
        return QtCore.QObject.event(obj, event)
