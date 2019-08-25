from domain import Board, Square
from constants import BOMB

from queue import Queue


class Game:
    def __init__(self):
        self.__mainBoard = Board(20, 20, 70)
        self.__mainBoard.fillBoardWithBombs()
        self.__mainBoard.fillBoardNumbers()

    def bfsOnBoard(self, row, col):
        '''
        :param row:
        :param col:
        :return: list of squares that must be uncovered
        '''
        copy_board = self.__mainBoard.getCopyBoard()
        current = copy_board[row][col]
        if current == BOMB:
            return BOMB
        if current != 0:
            return [Square(row, col)]
        q = Queue()
        q.put(Square(row, col))
        visited = []
        ret_lst = []
        while not q.empty():
            now = q.get()
            r = now.get_row
            c = now.get_col
            print(r, c)
            if copy_board[r][c] == 0:
                visited.append(now)
                neigh = self.__mainBoard.getListOfNeighbours(r, c)
                for n in neigh:
                    v = copy_board[n.get_row][n.get_col]
                    if n not in visited and v != BOMB:
                        q.put(n)
            if copy_board[r][c] != BOMB:
                ret_lst.append(now)
        # ret_lst = self.__mainBoard.getListOfNeighbours(row, col)
        # ret_lst += [Square(row, col)]
        return ret_lst


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
