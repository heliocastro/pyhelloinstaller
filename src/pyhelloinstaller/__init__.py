from __future__ import annotations

import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QWidget


def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    textlabel = QLabel(widget)
    textlabel.setText("Hello World!")
    textlabel.move(110, 85)

    widget.setGeometry(50, 50, 320, 200)
    widget.setWindowTitle("PyQt5 Example")
    widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()
