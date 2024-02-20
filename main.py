import sys


import PyQt5
from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow

# from Main import


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        PyQt5.uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('coffee.sqlite')
        self.db.open()

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('Sorts')
        self.model.select()

        self.view.setModel(self.model)
        self.view.move(10, 10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
