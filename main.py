import sys
from PyQt5.QtWidgets import QApplication
from gui.interface import TesTimaGeNBWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TesTimaGeNBWindow()
    window.show()
    sys.exit(app.exec_())
