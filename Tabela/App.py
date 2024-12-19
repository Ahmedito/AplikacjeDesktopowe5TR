import os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QGridLayout, QTableWidget, \
    QTableWidgetItem


class Table(QTableWidget):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        self.setColumnCount(3);
        self.setRowCount(3);
        self.horizontalHeader().setStretchLastSection(True)
        self.setHorizontalHeaderLabels(['Przyciski', 'Czas [HH:MM:SS]', 'Tekst'])
        self.setColumnWidth(0, 50)
        self.setColumnWidth(1, 150)
        self.resizeColumnsToContents()
        self.cellClicked.connect(self.getData)
        self.cellChanged.connect(self.addRow)
        btnUp = QPushButton("⬆")
        btnDw = QPushButton("⬇")

        btnUp.clicked.connect(self.moveUp)
        btnDw.clicked.connect(self.moveDown)

        lay = QHBoxLayout()
        lay.addWidget(btnUp)
        lay.addWidget(btnDw)
        bttns = QWidget()
        bttns.setLayout(lay)
        self.setCellWidget(0, 0, bttns)

    def getData(self,row,column):
        cell = self.item(row,column)
        #print(" x = "+str(row)+" y = "+str(column))
        if cell is None:
            print("Pusta")
        else:
            print(cell.text())

       # print(self.item(row.column))
        #print(self.item(row.column).text)
        #print("get data")

    def addRow(self,row,column):
        print("Change/add row")
        print(str(row) + "" + str(self.rowCount()))
        if row ==(self.rowCount()-1):
            print("Last Row")
            self.insertRow(self.rowCount())
            self.rowCount()

    def moveUp(self):
        print("move up")

    def moveDown(self):
        print("move down")


class App(QWidget):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        lay = QGridLayout()

        vid = QLabel("Wideo")
        lay.addWidget(vid)

        tbl = Table()
        lay.addWidget(tbl)

        toolbar = QHBoxLayout()
        btnOpen = QPushButton("Open")
        btnSave = QPushButton("Save")
        toolbar.addWidget(btnOpen)
        toolbar.addWidget(btnSave)
        tblLay = QWidget()
        tblLay.setLayout(toolbar)
        lay.addWidget(tblLay)

        self.setLayout(lay)
        self.resize(640, 480)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = App()
    win.show()

sys.exit(app.exec_())
