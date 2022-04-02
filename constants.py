# MODULE FOR CONSTANTS

from bunch import bunchify as toJSObject

BOMB = -1

ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8

COVERED = 99
UNCOVERED = -99

BUTTON_SIZE = 40

WINDOW_NAME = 'minesweeper'

USERS_FILE_NAME = 'users.json'
CONFIG_FILE_NAME = 'config.json'

BUTTON_COLOR_COVERED = 'background-color: grey'
BUTTON_COLOR_UNCOVERED = 'background-color: #cccccc'

FLAG = '-15'

INTERVALS = toJSObject({
    'height': {
        'min': 10,
        'max': 24
    },
    'width': {
        'min': 10,
        'max': 35
    },
    'bombs': {
        'min': 20,
        'max': 130
    }
})

ICONS = {
    BOMB: 'icons/bomb-2.jpg',
    FLAG: 'icons/flag.jpg',
    0: '',
    1: 'icons/one-4.png',
    2: 'icons/two-4.png',
    3: 'icons/three.jpg',
    4: 'icons/four.png',
    5: 'icons/five.png',
    6: 'icons/six.png',
    7: 'icons/seven.jpg',
    8: 'icons/eight.png',
}

first_style = '''   
  QWidget{
    background-color: #506477;
  }
  QLabel{
    color: white;
    font-size: 30px;
  }
  QPushButton{
    background-color: #423D26;
    color: white;
    border-radius: 15px;
    border: 2px solid black;
    font-size: 23px;
    margin: 3px;
  }
'''

add_player_style = '''
  QLabel{
    color: white;
    font-size: 30px;
  }
  QWidget{
    background-color: #506477;
  }
  QPushButton{
    background-color: #423D26;
    color: white;
    border-radius: 15px;
    border: 2px solid black;
    font-size: 23px;
    padding: 15px;
    margin: 3px;
  }
  QLineEdit{
    border: 2px solid black;
    background-color: white;
    color: black;
    border-radius: 15px;
    margin-bottom: 80px;
    font-size: 23px;
    padding: 10px;
  }
'''

players_score_style = '''
  QWidget{
    background-color: #506477;
  }
  QLabel{
    color: white;
    font-size: 18px;
  }
  QTableWidget{
    background-color: white;
  }
'''
