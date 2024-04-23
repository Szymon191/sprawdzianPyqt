import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.sumKcal = 0.00
        self.maxKcal = 0.00
        self.ui.dodaj.clicked.connect(self.addmeal)
        self.show()


    def addmeal(self):
        self.kcall()
        meal = self.ui.nazwaPosilku.text()
        kcal = self.ui.liczbaKalori.text()
        kcal = float(kcal.replace(',','.'))
        self.sumKcal += float(kcal)
        print(self.maxKcal)

        self.ui.listWidget.addItem(f'{meal} - {kcal}')
        self.ui.sumKalorii.setText(f'{self.sumKcal}')
        if self.ui.kobieta.isChecked() or self.ui.mezczyzna.isChecked():
            self.color()

    def color(self):
        k = float(self.ui.sumKalorii.text())
        if k <= (self.maxKcal*0.8):
            self.ui.sumKalorii.setStyleSheet('background-color: rgb(0, 255, 0)')
            pixmap = QPixmap(f'./1.jpg')
            pixmap = pixmap.scaled(self.ui.zdj.width(), self.ui.zdj.height())
            self.ui.zdj.setPixmap(pixmap)
        elif k > (self.maxKcal*0.8) and k <= self.maxKcal:
            self.ui.sumKalorii.setStyleSheet(f'background-color: black;color: rgb(255, 255, 255);')
            pixmap = QPixmap(f'./2.jpg')
            pixmap = pixmap.scaled(self.ui.zdj.width(), self.ui.zdj.height())
            self.ui.zdj.setPixmap(pixmap)
        elif k > self.maxKcal:
            self.ui.sumKalorii.setStyleSheet('background-color: #ff0000')
            pixmap = QPixmap(f'./3.jpg')
            pixmap = pixmap.scaled(self.ui.zdj.width(), self.ui.zdj.height())
            self.ui.zdj.setPixmap(pixmap)

    def kcall(self):
        women = self.ui.kobieta.isChecked()
        men = self.ui.mezczyzna.isChecked()
        if self.ui.malaAkt.isChecked() and women:
            self.maxKcal = 1700
        elif self.ui.malaAkt.isChecked() and men:
            self.maxKcal = 1900
        elif self.ui.sredniaAkt.isChecked() and women:
            self.maxKcal = 1900
        elif self.ui.sredniaAkt.isChecked() and men:
            self.maxKcal = 2200
        elif self.ui.duzaAkt.isChecked() and women:
            self.maxKcal = 2100
        elif self.ui.duzaAkt.isChecked() and men:
            self.maxKcal = 2500



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.setWindowTitle('Kalkulator kalorii')
    w.show()
    sys.exit(app.exec())