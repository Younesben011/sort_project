import sys
from PyQt5.QtWidgets import *
import json


class checkBoxes(QCheckBox):
    def __init__(self, name, btn):
        super().__init__()
        # check = QCheckBox(name)
        # check.stateChanged.connect(lambda: self.show(self))
        self.setText(name)
        self.stateChanged.connect(lambda: self.show(btn))

    def show(self, btn):
        state = self.checkState()
        if (state == 2):
            btn.setVisible(True)
        else:
            btn.setVisible(False)


class all_sorts(QVBoxLayout):
    def __init__(self, names):
        super().__init__()
        for name in names:
            btn = QPushButton("hi "+name)
            check_sort = checkBoxes(name, btn)
            btn.setVisible(False)

            self.addWidget(check_sort)
            self.addWidget(btn)


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
