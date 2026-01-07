import sys
from PyQt5.QtWidgets import QApplication
from ui.clima_tempo import ClimaTempo

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clima_tempo = ClimaTempo()
    clima_tempo.show()
    sys.exit(app.exec_())

    