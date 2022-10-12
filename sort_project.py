import sys
from PyQt5.QtWidgets import *
import json


class cases(QGroupBox):
    def __init__(self):
        super().__init__()
        self.setTitle("cases")

        BCase = QRadioButton("best case")
        BCase.setChecked(True)
        ACase = QRadioButton("avrege case")
        WCase = QRadioButton("worse case")

        hbosLayout = QHBoxLayout()
        hbosLayout.setGeometry(self, 100, 100, 0, 0)
        hbosLayout.addWidget(BCase)
        hbosLayout.addWidget(ACase)
        hbosLayout.addWidget(WCase)

        self.setLayout(hbosLayout)
        self.setDisabled(True)


class checkBoxes(QCheckBox):
    def __init__(self, name, cases):
        super().__init__()
        # check = QCheckBox(name)
        # check.stateChanged.connect(lambda: self.show(self))
        self.setText(name)
        self.stateChanged.connect(lambda: self.show(cases))

    def show(self, cases):
        print("Ss")
        state = self.checkState()
        if (state == 2):
            cases.setDisabled(False)
        else:
            cases.setDisabled(True)


class all_sorts(QVBoxLayout):
    def __init__(self, names):
        super().__init__()
        for name in names:
            sort_cases = cases()
            check_sort = checkBoxes(name, sort_cases)
            self.addWidget(check_sort)
            self.addWidget(sort_cases)


class sort_app(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("all kind of sorts")
        self.setFixedWidth(1000)
        # self.setFixedHeight(500)
        self.setStyleSheet("background:#c5e3cf")
        layout = all_sorts(["bubble sort", "quick sort",
                            "insertion sort", "merge_sort"])
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sort_win = sort_app()
    sort_win.show()
    sys.exit(app.exec())
