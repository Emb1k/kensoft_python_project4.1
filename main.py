#!/usr/bin/env python3
# coding=utf-8

import sys
import random

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        """
        заполняем таблицу случайными числами
        :return:
        """

        row = 0
        col = 0

        # заполняем таблицу случайными числами
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                k = random.choice([True, False])
                if k:
                    number = random.uniform(0, 20)
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str("{:5.1f}".format(number))))
                else:
                    number = random.randint(0, 20)
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(number)))
                col += 1
            row += 1
            col = 0

        provercka = find_zero(self.tableWidget)

        if provercka is None:
            self.label_error.setText('Введены некорректные данные!!')
        elif not provercka:
            self.label_max.setText("Нет нулевого элемента!")
        else:
            self.label_max.setText("Есть нулевой элемент!")

    def solve(self):
        try:
            provercka = find_zero(self.tableWidget)

            if provercka is None:
                self.label_error.setText('Введены некорректные данные!!')
                return
            elif not provercka:
                self.label_error.setText("Нулевого элемента нет!!!")
                return
            else:
                self.label_max.setText("Есть нулевой элемент!")

            row = 0
            col = 0
            # -*- решение задания -*-
            while row < self.tableWidget.rowCount():
                while col < self.tableWidget.columnCount():
                    try:
                        number = int(self.tableWidget.item(row, col).text())
                    except ValueError:
                        number = float(self.tableWidget.item(row, col).text())
                    if not isinstance(number, int):
                        self.tableWidget.setItem(row, col, QTableWidgetItem("1"))
                    col += 1
                row += 1
                col = 0
        except:
            self.label_error.setText('Введены некорректные данные!')


def find_zero(table_widget):
    """
    находим есть ли нулевой элемент
    :param table_widget: таблица
    :return: zero, если выкинуто исключение,
            то None
    """
    zero = False
    row = 0
    col = 0

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                try:
                    number = int(table_widget.item(row, col).text())
                except ValueError:
                    number = float(table_widget.item(row, col).text())
                if number == 0:
                    zero = True
                col += 1
            row += 1
            col = 0
    except Exception:
        return None
    return zero


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
