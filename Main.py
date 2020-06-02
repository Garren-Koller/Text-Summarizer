from PyQt5.QtWidgets import QApplication
from UI import Summarizer

# Main program
if __name__ == "__main__":
    app = QApplication([])
    window = Summarizer()
    window.run()
    app.exec_()
