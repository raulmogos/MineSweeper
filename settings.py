import json
import bunch
from copy import deepcopy

from constants import USERS_FILE_NAME, CONFIG_FILE_NAME


class Settings:

  def __init__(self):
    self.__read_from_file()

  def __read_from_file(self):
    with open(USERS_FILE_NAME, 'r') as input_file:
      self.__players = bunch.bunchify(json.load(input_file))
    with open(CONFIG_FILE_NAME, 'r') as input_file:
      self.__table = bunch.bunchify(json.load(input_file))

  def __write_to_file(self):
    with open(USERS_FILE_NAME, 'w') as output_file:
      output_file.write(json.dumps(self.__players, indent=2))
    with open(CONFIG_FILE_NAME, 'w') as output_file:
      output_file.write(json.dumps(self.__table, indent=2))

  def get_players(self):
    return deepcopy(self.__players)

  def get_table_settings(self):
    return deepcopy(self.__table)
  
  def add_player(self, name):
    if name in self.__players:
      return
    self.__players[name] = 0
    self.__write_to_file()

  def set_player_score(self, name, score):
    self.__players[name] = score
    self.__write_to_file()

  def set_height(self, value):
    self.__table.height = value
    self.__write_to_file()

  def set_width(self, value):
    self.__table.width = value
    self.__write_to_file()
    
  def set_no_bombs(self, value):
    self.__table.bombs = value
    self.__write_to_file()

  def printPlayers(self):
    print(self.__players)