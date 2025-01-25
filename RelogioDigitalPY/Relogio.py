import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class RelogioDigiral(QWidget):
    def __init__(self):
        super().__init__()
        self.tempo_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    
    def initUI(self):
        self.setWindowTitle("Relógio Digital")
        self.setGeometry(600, 400, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.tempo_label)
        self.setLayout(vbox)

        self.tempo_label.setAlignment(Qt.AlignCenter)

        self.tempo_label.setStyleSheet("font-size: 120px;"
                                       "color: green;")
        self.setStyleSheet("background-color: black;")
        
        fonte_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        fonte_familia = QFontDatabase.applicationFontFamilies(fonte_id)[0]
        minha_fonte = QFont(fonte_familia, 150)
        self.tempo_label.setFont(minha_fonte)
        
        self.timer.timeout.connect(self.tempo_atualizado)
        self.timer.start(1000)

        self.tempo_atualizado()

    def tempo_atualizado(self):
        tempo_atual = QTime.currentTime().toString("hh:mm:ss")
        self.tempo_label.setText(tempo_atual)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    relogio = RelogioDigiral()
    relogio.show()
    sys.exit(app.exec_())