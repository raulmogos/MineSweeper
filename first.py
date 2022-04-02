from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QSlider, QTableWidget,
    QTableWidgetItem, QLineEdit
)

from constants import first_style, players_score_style, INTERVALS, add_player_style
from gameService import Game
from gui import GUI
from settings import Settings


class StartApp(QWidget):

    def __init__(self, parent=None):
        super(StartApp, self).__init__(parent)

        self.setWindowTitle('MineSweeper')
        self.setFixedSize(400, 400)
        self.setStyleSheet(first_style)
        vertical = QVBoxLayout()

        title = QLabel('MineSweeper')
        title.setAlignment(Qt.AlignCenter)
        vertical.addWidget(title)

        start = QPushButton()
        start.setText('start')
        start.setFixedHeight(50)
        start.clicked.connect(self.__start_game)
        vertical.addWidget(start)

        score = QPushButton()
        score.setText('score')
        score.setFixedHeight(50)
        score.clicked.connect(self.__show_players)
        vertical.addWidget(score)

        settings = QPushButton()
        settings.setText('settings')
        settings.setFixedHeight(50)
        settings.clicked.connect(self.__show_settings)
        vertical.addWidget(settings)

        close_button = QPushButton()
        close_button.setText('close')
        close_button.setFixedHeight(50)
        close_button.clicked.connect(self.close)
        vertical.addWidget(close_button)

        self.setLayout(vertical)

    def __show_players(self):
        settings = Settings()
        self.__window = QWidget()
        self.__window.setStyleSheet(players_score_style)
        layout = QVBoxLayout(self.__window)
        self.__window.setLayout(layout)
        title = QLabel('PLAYERS')
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        table_list = QTableWidget(self.__window)
        table_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        table_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        layout.addWidget(table_list)
        table_list.setRowCount(len(settings.get_players()))
        table_list.setColumnCount(2)
        row = 0
        players = settings.get_players()
        for key in players.keys():
            table_list.setItem(row, 0, QTableWidgetItem(str(key)))
            table_list.setItem(row, 1, QTableWidgetItem(str(players[key])))
            row += 1
        table_list.setHorizontalHeaderLabels(['name', 'score'])
        table_list.setMinimumSize(self.__getQTableWidgetSize(table_list))
        table_list.setMaximumSize(self.__getQTableWidgetSize(table_list))
        self.__window.show()

    def __getQTableWidgetSize(self, q_table_widget):
        w = q_table_widget.verticalHeader().width() + 2
        for i in range(q_table_widget.columnCount()):
            w += q_table_widget.columnWidth(i)
        h = q_table_widget.horizontalHeader().height() + 2
        for i in range(q_table_widget.rowCount()):
            h += q_table_widget.rowHeight(i)
        return QSize(w, h)

    def __show_settings(self):
        settings = Settings()
        self.__window = QWidget()
        self.__window.setFixedSize(350, 200)

        height_label = QLabel(f'height: {settings.get_table_settings().height}')

        height = QSlider(Qt.Horizontal)
        height.setMaximum(INTERVALS.height.max)
        height.setMinimum(INTERVALS.height.min)
        height.setValue(settings.get_table_settings().height)
        height.setTickInterval(1)
        height.setTickPosition(QSlider.TicksBelow)
        height.valueChanged.connect(lambda: {
            settings.set_height(height.value()),
            height_label.setText(f'height: {height.value()}')
        })

        width_label = QLabel(f'width: {settings.get_table_settings().width}')

        width = QSlider(Qt.Horizontal)
        width.setMaximum(INTERVALS.width.max)
        width.setMinimum(INTERVALS.width.min)
        width.setValue(settings.get_table_settings().width)
        width.setTickInterval(1)
        width.setTickPosition(QSlider.TicksBelow)
        width.valueChanged.connect(lambda: {
            settings.set_width(width.value()),
            width_label.setText(f'width: {width.value()}')
        })

        bombs_label = QLabel(f'bombs: {settings.get_table_settings().bombs}')

        bombs = QSlider(Qt.Horizontal)
        bombs.setMaximum(INTERVALS.bombs.max)
        bombs.setMinimum(INTERVALS.bombs.min)
        bombs.setValue(settings.get_table_settings().bombs)
        bombs.setTickInterval(10)
        bombs.setTickPosition(QSlider.TicksBelow)
        bombs.valueChanged.connect(lambda: {
            settings.set_no_bombs(bombs.value()),
            bombs_label.setText(f'bombs: {bombs.value()}')
        })

        layout = QVBoxLayout()
        layout.addWidget(height_label)
        layout.addWidget(height)
        layout.addWidget(width_label)
        layout.addWidget(width)
        layout.addWidget(bombs_label)
        layout.addWidget(bombs)
        self.__window.setLayout(layout)
        self.__window.show()

    def __add_new_player(self):
        settings = Settings()

        self.__window = QWidget()
        self.__window.setFixedSize(400, 400)
        self.__window.setStyleSheet(add_player_style)
        vertical = QVBoxLayout()
        self.__window.setLayout(vertical)

        user_name_label = QLabel('user name:')
        user_name_label.setAlignment(Qt.AlignCenter)
        vertical.addWidget(user_name_label)

        user_name_input = QLineEdit()
        user_name_input.setAlignment(Qt.AlignCenter)
        vertical.addWidget(user_name_input)

        play_button = QPushButton('play')
        play_button.clicked.connect(lambda: {
            settings.add_player(user_name_input.text()),
            self.__start_game(),
            self.__window.close()
        })
        vertical.addWidget(play_button)

        self.__window.show()

    def __start_game(self):
        settings = Settings()
        table_settings = settings.get_table_settings()
        height = table_settings.height
        width = table_settings.width
        bombs = table_settings.bombs
        game = Game(height, width, bombs)
        self.__gui = GUI(game)
        self.__gui.show()
