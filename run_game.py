import sys
from PyQt5.QtWidgets import QApplication

from gameService import *
from gui import *


if __name__ == '__main__':
    app = QApplication(sys.argv)

    service = Game()
    gui = GUI(service)

    sys.exit(app.exec_())
