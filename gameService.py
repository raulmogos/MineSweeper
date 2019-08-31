from domain import Board, Square
from constants import BOMB

from queue import Queue


n = 20
m = 20
b = 60

class Game:
    def __init__(self):
        self.__mainBoard = Board(n, m, b)
        self.__coveredBoard = [[0 for i in range(m)] for j in range(n)]
        self.__visited = [[0 for i in range(m)] for j in range(n)]
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
        ret_lst = []
        while not q.empty():
            now = q.get()
            r = now.get_row
            c = now.get_col
            if copy_board[r][c] == 0:
                self.__visited[r][c] = 1
                self.__coveredBoard[r][c] == 1
                neigh = self.__mainBoard.getListOfNeighbours(r, c)
                for n in neigh:
                    v = copy_board[n.get_row][n.get_col]
                    vis = self.__coveredBoard[n.get_row][n.get_col]
                    isVisited = self.__visited[n.get_row][n.get_col]
                    if not isVisited and v != BOMB and vis == 0:
                        q.put(n)
            if copy_board[r][c] != BOMB:
                ret_lst.append(now)
        return ret_lst

    def getMainBoard(self):
        return self.__mainBoard.getCopyBoard()

    def getNuberOfRows(self):
        return self.__mainBoard.getNuberOfRows()

    def getNumberOfCols(self):
        return self.__mainBoard.getNumberOfCols()

    def getNumberOfBombs(self):
        return self.__mainBoard.getNumberOfBombs()