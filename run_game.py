import sys
from PyQt5.QtWidgets import QApplication

from gameService import *
from gui import *

from first import StartApp


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    #
    # service = Game()
    # gui = GUI(service)
    #
    # sys.exit(app.exec_())

    app = QApplication(sys.argv)

    start = StartApp()
    start.show()

    sys.exit(app.exec_())

