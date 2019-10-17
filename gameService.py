from domain import Board, Square
from constants import BOMB, FLAG

from queue import Queue
from copy import deepcopy

class Game:

  def __init__(self, height, width, bombs):
    self.__mainBoard = Board(height, width, bombs)
    self.__visited = [[0 for i in range(width)] for j in range(height)]
    self.__flags = [[0 for i in range(width)] for j in range(height)]
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
    self.__visited[row][col] = 1
    ret_lst = []
    while not q.empty():
      now = q.get()
      r = now.get_row
      c = now.get_col
      if copy_board[r][c] == 0:
        neighbours = self.__mainBoard.getListOfNeighbours(r, c)
        for neigh in neighbours:
          value = copy_board[neigh.get_row][neigh.get_col]
          is_visited = self.__visited[neigh.get_row][neigh.get_col]
          if not is_visited and value != BOMB:
            q.put(neigh)
            self.__visited[neigh.get_row][neigh.get_col] = 1
      if copy_board[r][c] != BOMB:
        ret_lst.append(now) 
    return ret_lst
  
  def getNeighboursNotFlaged(self, row, col):
    neighbours = self.__mainBoard.getListOfNeighbours(row, col)
    l = filter(lambda square: self.__visited[square.get_row][square.get_col],
               neighbours)
    return deepcopy(l)
  
  def setFlag(self, row, col):
    self.__flags[row][col] = FLAG

  def unsetFlag(self, row, col):
    self.__flags[row][col] = 0
    
  def isFlag(self, row, col):
    return self.__flags[row][col] == FLAG
  
  def getFlagedBoard(self):
    return deepcopy(self.__flags)

  def getMainBoard(self):
    return self.__mainBoard.getCopyBoard()

  def getNuberOfRows(self):
    return self.__mainBoard.getNuberOfRows()

  def getNumberOfCols(self):
    return self.__mainBoard.getNumberOfCols()

  def getNumberOfBombs(self):
    return self.__mainBoard.getNumberOfBombs()
