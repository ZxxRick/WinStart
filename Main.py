import sys
from UIClass.main import Main
from threading import Thread

from PyQt5.QtWidgets import QApplication

from UIClass.testDialog import TestDialog

if __name__ == '__main__':
    app = QApplication(sys.argv)

    myapp = Main()
    # myapp=TestDialog()
    myapp.show()

    sys.exit(app.exec_())
