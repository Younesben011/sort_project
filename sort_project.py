from ast import match_case
from re import S
import sys
from time import time
from unicodedata import name
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, Qt
import json
from sorting_techniques import pysort
import threading
import random


class sortFunction():
    def __init__(self, dic, timer_list):
        print("from sort function")
        for item in dic:
            if (dic[item]['state']):
                case = dic[item]['case']
                length = dic[item]['length']
                timer_list[item].timer.start()
                print(self.generate_list(case, length))

    def generate_list(self, state, length):
        match state:
            case "best case":
                return [i for i in range(1, length+1)]
            case "avrege case":
                randList = []
                for i in range(0, length):
                    n = random.randint(1, 100)
                    randList.append(n)
                return randList
            case "worse case":
                l = [i for i in range(1, length+1)]
                l.reverse()
                return l


class List_length(QLineEdit):
    def __init__(self, name, sorts_dic):
        super().__init__()
        self.setText("10")
        self.resize(280, 40)
        self.textChanged.connect(lambda: self.set_length(name, sorts_dic))

    def set_length(self, name, dic):
        dic[name]['length'] = int(self.text())


class cases(QGroupBox):
    def __init__(self, name, sorts_dic):
        super().__init__()
        self.setTitle("cases")
        cases_layout = QVBoxLayout()
        self.BCase = QRadioButton("best case")
        self.BCase.setChecked(True)
        self.BCase.clicked.connect(
            lambda: self.set_cases(name, sorts_dic, self.BCase))
        self.ACase = QRadioButton("avrege case")
        self.ACase.clicked.connect(
            lambda: self.set_cases(name, sorts_dic, self.ACase))
        self.WCase = QRadioButton("worse case")
        self.WCase.clicked.connect(
            lambda: self.set_cases(name, sorts_dic, self.WCase))
        self.list_lngth = List_length(name, sorts_dic)
        hbosLayout = QHBoxLayout()
        hbosLayout.setAlignment(QtCore.Qt.AlignLeft)
        # cases_layout.setGeometry(100, 100, 0, 0)
        # hbosLayout.setGeometry(100, 100, 0, 0)
        hbosLayout.addWidget(self.BCase)
        hbosLayout.addWidget(self.ACase)
        hbosLayout.addWidget(self.WCase)
        cases_layout.addWidget(self.list_lngth)

        self.setLayout(cases_layout)
        cases_layout.addLayout(hbosLayout)
        self.setDisabled(True)

    def set_cases(self, name, sorts_dic, Case):
        sorts_dic[name]["case"] = Case.text()


class checkBoxes(QCheckBox):
    def __init__(self, name, cases, sorts_dic):
        super().__init__()
        # check = QCheckBox(name)
        # check.stateChanged.connect(lambda: self.show(self))
        self.setText(name)
        self.stateChanged.connect(lambda: self.show(cases, sorts_dic, name))

    def show(self, cases, sorts_dic, name):
        state = self.checkState()
        if (state == 2):
            sorts_dic[name]["state"] = True
            cases.setDisabled(False)
        else:
            sorts_dic[name]["state"] = False
            cases.setDisabled(True)


class all_sorts(QVBoxLayout):
    def __init__(self, names):
        self.sorts_dic = {'bubble sort': {'state': False, 'length': 10, 'case': 'best case'}, 'quick sort': {'state': False, 'length': 10, 'case': 'best case'},
                          'insertion sort': {'state': False, 'length': 10, 'case': 'best case'}, 'merge_sort': {'state': False, 'length': 10, 'case': 'best case'}}
        super().__init__()
        for name in names:
            self.sort_cases = cases(name, self.sorts_dic)
            self.check_sort = checkBoxes(name, self.sort_cases, self.sorts_dic)
            self.addWidget(self.check_sort)
            self.addWidget(self.sort_cases)


class sort_timer(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.timer_lable = QLabel("0 ms")
        self.timer_lable.setStyleSheet("""
                color:#2d7487;
                font-size:20px;
                margin-top:20px;
                padding-left:200px
                """)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.counter)
        self.addWidget(self.timer_lable)
        self.c = 0

    def counter(self):
        self.c += 1
        self.timer_lable.setText(str(self.c)+" ms")

    def reset(self):
        self.c = 0
        self.timer_lable.setText("0 ms")


class sort_app(QWidget):
    c = 0

    def __init__(self):
        super().__init__()
        self.setWindowTitle("all kind of sorts")
        self.setFixedWidth(1000)
        # self.setFixedHeight(500)
        main_layout = QVBoxLayout()
        second_layout = QHBoxLayout()
        layout2 = QVBoxLayout()

        self.sort_layout = all_sorts(["bubble sort", "quick sort",
                                      "insertion sort", "merge_sort"])

        self.start_btn = QPushButton("Start", objectName="start")
        self.start_btn.clicked.connect(self.start)

        self.timer = sort_timer()
        self.timer1 = sort_timer()
        self.timer2 = sort_timer()
        self.timer3 = sort_timer()
        self.timer_list = {"bubble sort": self.timer, "quick sort": self.timer1,
                           "insertion sort": self.timer2, "merge_sort": self.timer3}
        layout2.addLayout(self.timer)
        layout2.addLayout(self.timer1)
        layout2.addLayout(self.timer2)
        layout2.addLayout(self.timer3)
        second_layout.addLayout(self.sort_layout)
        second_layout.addLayout(layout2)

        main_layout.addLayout(second_layout)
        main_layout.addWidget(self.start_btn, 0, QtCore.Qt.AlignCenter)

        self.setLayout(main_layout)

    def sortFunc(self):
        sortF = sortFunction(self.sort_layout.sorts_dic, self.timer_list)

    def start(self):
        if (self.start_btn.text() == "Start"):

            self.start_btn.setText("Stop")
            self.sortFunc()
        else:
            self.timer.timer.stop()
            self.timer1.timer.stop()
            self.timer2.timer.stop()
            self.timer3.timer.stop()
            self.timer.reset()
            self.timer1.reset()
            self.timer2.reset()
            self.timer3.reset()
            self.start_btn.setText("Start")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
    #start{
        color:white;
        margin:10;
        padding:5;
        padding-left:20;
        padding-right:20;
        border: 2px solid #3fa3bf;
        border-radius:10;
        font-size:16px;
        background-color:#3fa3bf;
    }
    #start:hover{
        border: 2px solid #2d7487;        

     }
    """)
    sort_win = sort_app()
    sort_win.show()
    sys.exit(app.exec())
