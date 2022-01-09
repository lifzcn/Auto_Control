# -*- coding : utf-8 -*-
# @File : main.py
# @Author : Leonard
# @Time : 2022/01/09 11:36:03


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from interface import Ui_Form

import control as ctrl
import matplotlib.pyplot as plt


class mainWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.pushButton_Print.clicked.connect(self.print)
        self.pushButton_Exit.clicked.connect(self.exit)

    def print(self, parent=None):
        str1 = self.lineEdit_Zero.text()
        str2 = self.lineEdit_Peak.text()
        f = ctrl.tf(eval(str1), eval(str2))
        if self.checkBox_Nyquist.isChecked():
            plt.plot(ctrl.nyquist(f))
            plt.savefig("nyquist.jpg")
        elif self.checkBox_Bode.isChecked():
            plt.plot(ctrl.bode(f))
            plt.savefig("bode.jpg")

    def exit(self, parent=None):
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = mainWindow()
    myWin.show()
    sys.exit(app.exec_())
