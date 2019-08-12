import sys
from PyQt5.QtWidgets import QApplication


from domain import *
from gameService import *
from consoleUi import *
from gui import *



# board = Board()
# game = Game(board)
# ui = UI(game)
#
# ui.run()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    service = Game()
    gui = GUI(service)

    gui.show()

    sys.exit(app.exec_())
