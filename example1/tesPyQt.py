# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
import testui


def convert(inputui):
    input = inputui.lineEdit.text()
    result = float(input) * 6.5
    inputui.lineEdit_2.setText(str(result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = testui.Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.pushButton.clicked.connect(partial(convert, ui))
    MainWindow.show()
    sys.exit(app.exec_())
