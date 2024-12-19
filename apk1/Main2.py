import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5 import uic, Qt
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QAbstractItemView
from PyQt5.QtGui import QDrag
from PyQt5.QtCore import Qt, QMimeData


class DnD(QListWidget):
    def __init__(self,parent=None):
        super(DnD,self).__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropOverwriteMode(False)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setDefaultDropAction(Qt.MoveAction)
        itm1 = QListWidgetItem("Elemental")
        itm2 = QListWidgetItem("Supleemental")
        itm3 = QListWidgetItem("Just mental")
        self.addItem(itm1)
        self.addItem(itm2)
        self.addItem(itm3)
        self.insertItem(2, "Anymental")
        print(self.count())

    def handleDropEvent(self,e):
        src = e.source()
        selItems = src.selectedItems()
        for item in selItems:
            i = selItems
            elmNo = src.indexFromItem(item).row()
            src.takeItem(elmNo)
            self.addItem(item)

    def dragEnterEvent(self, e):
        e.accept()


class App(QWidget):
    def __init__(self,parent=None):
        super(App, self).__init__(parent)
        #lst = QListWidget()
        #lay = QGridLayout()
        #lay.addWidget(lst)
        #self.setLayout(lay)
        self.view = DnD(self)
        self.resize(480, 320)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = App()
    win.show()

sys.exit(app.exec_())