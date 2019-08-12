from domain import Board
from constants import COVERED

from queue import Queue


class Game:
    def __init__(self):
        self.__mainBoard = Board(16, 16)
        self.__mainBoard.fillBoardWithBombs()
        self.__mainBoard.fillBoardNumbers()
        self.__coveredBoard = Board(16, 16)
        self.__setUpCovered()

    def __setUpCovered(self):
        for i in range(10):
            for j in range(10):
                self.__coveredBoard.setSquare(i, j, COVERED)

    def bfsOnBoard(self, row, col):
        '''
        :param row:
        :param col:
        :return: list of squares that must be uncovered
        '''
        pass



    def uncoverSquare(self, row, col):
        pass

    def signalSquare(self, row, col):
        pass

    def getMainBoard(self):
        return self.__mainBoard.getCopyBoard()

    def getNuberOfRows(self):
        return self.__mainBoard.getNuberOfRows()

    def getNumberOfCols(self):
        return self.__mainBoard.getNumberOfCols()

    def getNumberOfBombs(self):
        return self.__mainBoard.getNumberOfBombs()
