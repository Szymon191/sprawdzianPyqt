# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(657, 703)
        font = QtGui.QFont()
        font.setPointSize(16)
        Dialog.setFont(font)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 631, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.liczbaKalori = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.liczbaKalori.setMaximum(10000.0)
        self.liczbaKalori.setObjectName("liczbaKalori")
        self.gridLayout.addWidget(self.liczbaKalori, 1, 1, 1, 1)
        self.sumKalorii = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sumKalorii.setFont(font)
        self.sumKalorii.setText("")
        self.sumKalorii.setObjectName("sumKalorii")
        self.gridLayout.addWidget(self.sumKalorii, 4, 1, 1, 1)
        self.label2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.label2.setFont(font)
        self.label2.setStyleSheet("color: rgb(0, 85, 0);")
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 1, 0, 1, 1)
        self.nazwaPosilku = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.nazwaPosilku.setObjectName("nazwaPosilku")
        self.gridLayout.addWidget(self.nazwaPosilku, 0, 1, 1, 1)
        self.label1 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.label1.setFont(font)
        self.label1.setStyleSheet("color: rgb(0, 85, 0);")
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.dodaj = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dodaj.setFont(font)
        self.dodaj.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.dodaj.setObjectName("dodaj")
        self.gridLayout.addWidget(self.dodaj, 2, 0, 1, 2)
        self.listWidget = QtWidgets.QListWidget(parent=self.gridLayoutWidget)
        self.listWidget.setEnabled(False)
        self.listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.listWidget.setProperty("showDropIndicator", True)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 3, 0, 1, 2)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 319, 631, 151))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.zdj = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.zdj.setText("")
        self.zdj.setObjectName("zdj")
        self.gridLayout_2.addWidget(self.zdj, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=Dialog)
        self.line.setGeometry(QtCore.QRect(10, 485, 631, 21))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 510, 381, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.kobieta = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kobieta.setFont(font)
        self.kobieta.setObjectName("kobieta")
        self.horizontalLayout.addWidget(self.kobieta)
        self.mezczyzna = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mezczyzna.setFont(font)
        self.mezczyzna.setObjectName("mezczyzna")
        self.horizontalLayout.addWidget(self.mezczyzna)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 570, 381, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.malaAkt = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.malaAkt.setFont(font)
        self.malaAkt.setObjectName("malaAkt")
        self.verticalLayout.addWidget(self.malaAkt)
        self.sredniaAkt = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sredniaAkt.setFont(font)
        self.sredniaAkt.setObjectName("sredniaAkt")
        self.verticalLayout.addWidget(self.sredniaAkt)
        self.duzaAkt = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.duzaAkt.setFont(font)
        self.duzaAkt.setObjectName("duzaAkt")
        self.verticalLayout.addWidget(self.duzaAkt)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label2.setText(_translate("Dialog", "liczba kalorii"))
        self.label1.setText(_translate("Dialog", "nazwa posilku"))
        self.label_3.setText(_translate("Dialog", "Suma Spozytych kalorii: "))
        self.dodaj.setText(_translate("Dialog", "Dodaj"))
        self.kobieta.setText(_translate("Dialog", "Kobieta"))
        self.mezczyzna.setText(_translate("Dialog", "Mężczyzna"))
        self.malaAkt.setText(_translate("Dialog", "Mala aktywnosc fizyczna"))
        self.sredniaAkt.setText(_translate("Dialog", "Srednia aktywnosc fizyczna"))
        self.duzaAkt.setText(_translate("Dialog", "Duza aktywnosc fizyczna"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())