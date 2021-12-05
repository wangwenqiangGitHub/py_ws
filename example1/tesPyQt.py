import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from functools import partial
import testui

def convert(ui):
    input = ui.lineEdit.txt() #获取第一个文本编辑框的数字
    result = float(input) * 6.5
    ui.lineEdit_2.setText(str(result)) # 在第二个文本框中显示

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = testui.Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.pushButton.clicked.connect(partial(convert, ui))
    sys.exit(app.exec_())
