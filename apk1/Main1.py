import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5 import uic
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QAbstractItemView


class DnD(QListWidget):
    def __init__(self):
        super().__init__()


class App(QWidget):
    def __init__(self):
        super().__init__()
        lst = QListWidget()
        itm1 = QListWidgetItem("Elemental")
        itm2 = QListWidgetItem("Supleemental")
        itm3 = QListWidgetItem("Just mental")
        lst.addItem(itm1)
        lst.addItem(itm2)
        lst.addItem(itm3)
        lst.insertItem(2, "Anymental")
        print(lst.count())
        lay = QGridLayout()
        lay.addWidget(lst)
        self.setLayout(lay)
        self.resize(480, 320)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = App()
    win.show()

sys.exit(app.exec_())