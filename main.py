import sqlite3
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QApplication
from PyQt6 import uic
import sys
import io

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1000</width>
    <height>850</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>0</y>
      <width>781</width>
      <height>791</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1000</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class AdminPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.db = sqlite3.connect("coffee.sqlite").cursor()
        self.update_table()

    def update_table(self):
        request = "SELECT * FROM 'coffee'"
        self.result = self.db.execute(request).fetchall()
        self.tableWidget.setRowCount(len(self.result))
        self.tableWidget.setColumnCount(len(self.result[0]))
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Название сорта", "Степень обжарки", "Молотый/в зернах", "Описание вкуса", "Цена (руб.)", "Объем упаковки (гр)"])
        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.tableWidget.setColumnWidth(0, 20)
        self.tableWidget.setColumnWidth(1, 130)
        self.tableWidget.setColumnWidth(2, 110)
        self.tableWidget.setColumnWidth(3, 130)
        self.tableWidget.setColumnWidth(4, 280)
        self.tableWidget.setColumnWidth(5, 100)
        self.tableWidget.setColumnWidth(6, 130)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AdminPanel()
    ex.show()
    sys.exit(app.exec())