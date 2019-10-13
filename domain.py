from copy import deepcopy

from random import randint
from constants import BOMB


class Square:
  def __init__(self, row, col):
    self.__row = row
    self.__col = col
    self.__covered = True

  @property
  def get_row(self):
    return self.__row

  @property
  def get_col(self):
    return self.__col

  def __eq__(self, other):
    return self.__row == other.__row and self.__col == other.__col

  def set_uncovered(self):
    self.__covered = False

  def is_covered(self):
    return self.__covered

class Board:

  def __init__(self, rows=10, columns=10, no_bombs=15):
    '''
    decare a matrix 10x10
    initialized with 0's
    '''
    self.__board = []
    self.__max_size_rows = rows
    self.__max_size_cols = columns
    self.__max_number_bombs = no_bombs
    self.__setUp()

  def __setUp(self):
    self.__board = [
      [0 for i in range(self.__max_size_cols)] for j in range(self.__max_size_rows)
    ]

  def getEmptySquares(self):
    # return a list of Squares objects which are = 0
    return_list_empty_squares = []
    for row in range(0, self.__max_size_rows):
      for col in range(0, self.__max_size_cols):
        if self.__board[row][col] == 0:
          return_list_empty_squares.append(Square(row, col))
    return return_list_empty_squares

  def fillBoardWithBombs(self):
    # we fill the board with random numbers
    index = 0
    while index < self.__max_number_bombs:
      row = randint(0, self.__max_size_rows - 1)
      col = randint(0, self.__max_size_cols - 1)
      if self.__board[row][col] == BOMB:
        index -= 1
      else:
        self.__board[row][col] = BOMB
      index += 1

  def fillBoardNumbers(self):
    # we put inn each square the number of bombs in its area
    for row in range(0, self.__max_size_rows):
      for col in range(0, self.__max_size_cols):
        if self.__board[row][col] == 0:
          self.__board[row][col] = self.__numberOfBombsAround(row, col)

  def __isRowInBoardRange(self, row):
    return row >= 0 and row < self.__max_size_rows

  def __isColumnInBoardRange(self, col):
    return col >= 0 and col < self.__max_size_cols

  def getListOfNeighbours(self, row, col):
    list_of_neighbours = []
    moves = [[0, 1], [1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1], [0, -1], [-1, 0]]
    for move in moves:
      neighbour_square_row = row + move[0]
      neighbour_square_col = col + move[1]
      if self.__isColumnInBoardRange(neighbour_square_col) \
          and self.__isRowInBoardRange(neighbour_square_row):
        list_of_neighbours.append(Square(neighbour_square_row, neighbour_square_col))
    return list_of_neighbours

  def __numberOfBombsAround(self, row, col):
    number_of_bombs = 0
    for sq in self.getListOfNeighbours(row, col):
      if self.__board[sq.get_row][sq.get_col] == BOMB:
        number_of_bombs += 1
    return number_of_bombs

  def getCopyBoard(self):
    return deepcopy(self.__board)

  def getNuberOfRows(self):
    return self.__max_size_rows

  def getNumberOfCols(self):
    return self.__max_size_cols

  def getNumberOfBombs(self):
    return self.__max_number_bombs
