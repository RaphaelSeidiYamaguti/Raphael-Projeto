import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QPushButton, QVBoxLayout, QHBoxLayout)

from PyQt5.QtCore import QTimer, QTime, Qt


class Cronometro(QWidget):
    def __init__(self):
        super().__init__()
        self.tempo = QTime(0, 0, 0, 0)
        self.tempo_label = QLabel("00:00:00:00", self)
        self.botao_comecar = QPushButton("Começar", self)
        self.botao_pausar = QPushButton("Pausar", self)
        self.botao_resetar = QPushButton("Resetar", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Cronometro")

        vbox = QVBoxLayout()
        vbox.addWidget(self.tempo_label)
        vbox.addWidget(self.botao_comecar)
        vbox.addWidget(self.botao_pausar)
        vbox.addWidget(self.botao_resetar)

        self.setLayout(vbox)

        self.tempo_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()

        hbox.addWidget(self.botao_comecar)
        hbox.addWidget(self.botao_pausar)
        hbox.addWidget(self.botao_resetar)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QpushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family = calibri
            }
            QPushButton{
                font-size: 50px;
            }
            QLabel{
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 20px;
            }
        """)
        self.botao_comecar.clicked.connect(self.comecar)
        self.botao_pausar.clicked.connect(self.pausar)
        self.botao_resetar.clicked.connect(self.resetar)
        self.timer.timeout.connect(self.atualizar_display)

    def comecar(self):
        self.timer.start(10)

    def pausar(self):
        self.timer.stop()

    def resetar(self):
        self.timer.stop()
        self.tempo = QTime(0, 0, 0, 0)
        self.tempo_label.setText(self.formato_tempo(self.tempo))

    def formato_tempo(self, tempo):
        horas = tempo.hour()
        minutos = tempo.minute()
        segundos = tempo.second()
        milisegundos = tempo.msec() //10
        return f"{horas:02}:{minutos:02}:{segundos:02}.{milisegundos:02}"

    def atualizar_display(self):
        self.tempo = self.tempo.addMSecs(10)
        self.tempo_label.setText(self.formato_tempo(self.tempo))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cronometro = Cronometro()
    cronometro.show()
    sys.exit(app.exec_())