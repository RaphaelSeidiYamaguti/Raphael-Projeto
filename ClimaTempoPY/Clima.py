#d9bc7b20371d46ff030518d3e40ebda6 api key
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                            QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class ClimaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.cidade_label = QLabel("Entre com o nome da cidade: ", self)
        self.cidade_input = QLineEdit(self)
        self.botao = QPushButton("Pegar o Clima", self)
        self.temperatura_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.descricao_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("ClimaTempo app")

        vbox = QVBoxLayout()

        vbox.addWidget(self.cidade_label)
        vbox.addWidget(self.cidade_input)
        vbox.addWidget(self.botao)
        vbox.addWidget(self.temperatura_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.descricao_label)
        self.setLayout(vbox)

        self.cidade_label.setAlignment(Qt.AlignCenter)
        self.cidade_input.setAlignment(Qt.AlignCenter)
        self.temperatura_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.descricao_label.setAlignment(Qt.AlignCenter)

        self.cidade_label.setObjectName("cidade_label")
        self.cidade_input.setObjectName("cidade_input")
        self.temperatura_label.setObjectName("temperatura_label")
        self.emoji_label.setObjectName("emoji_label")
        self.descricao_label.setObjectName("descricao_label")
        self.botao.setObjectName("botao")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#cidade_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#cidade_input{
                font-size: 40px;
            }
            QPushButton#botao{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperatura_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#descricao_label{
                font-size: 50px;
            }
        """)

        self.botao.clicked.connect(self.pegar_clima)
       
    def pegar_clima(self):

        api_key = "d9bc7b20371d46ff030518d3e40ebda6"
        cidade = self.cidade_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}"

        try:
            resposta = requests.get(url)
            resposta.raise_for_status()
            data = resposta.json()

            if data["cod"] == 200:
                self.mostrar_clima(data)
        except requests.exceptions.HTTPError as http_error:
            match resposta.status_code:
                case 400:
                    self.mostrar_erros("Bad request\nPor favor cheque o que você colocou!")
                case 401:
                    self.mostrar_erros("Unauthorized\nAPI_KEY inválido!")
                case 403:
                    self.mostrar_erros("Forbiden\nAcesso foi negado!")
                case 404:
                    self.mostrar_erros("Not Found\nCidade não foi achada!")
                case 500:
                    self.mostrar_erros("Internal Server Error\nPor favor tente novamente depois!")
                case 502:
                    self.mostrar_erros("Bad Gateaway\nTempo invalido do server!")
                case 503:
                    self.mostrar_erros("Service Unavailble\nO servidor caiu!")
                case 504:
                    self.mostrar_erros("Gateaway Timeout\nNenhuma resposta do servidor!")
                case _:
                    self.mostrar_erros(f"HTTP error ocorreu\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.mostrar_erros("Connection Error\nCheque a sua conexão com a internet")
        except requests.exceptions.Timeout:
            self.mostrar_erros("Timeout Error\nA solicitação expirou ")
        except requests.exceptions.TooManyRedirects:
            self.mostrar_erros("Too Many Redirects\n Cheuqe a URL")
        except requests.exceptions.RequestException as req_erro:
            self.mostrar_erros(f"Request Error\n{req_erro}")


    def mostrar_erros(self, mensagem):
        self.temperatura_label.setStyleSheet("font-size: 30px")
        self.temperatura_label.setText(mensagem)
        self.emoji_label.clear()
        self.descricao_label.clear()

    def mostrar_clima(self, data):
        self.temperatura_label.setStyleSheet("font-size: 75px")
        temperatura_k = data["main"]["temp"]
        temperatura_c = temperatura_k - 273.15
        clima_id = data["weather"][0]["id"]
        clima_descricao = data["weather"][0]["description"]

        self.temperatura_label.setText(f"{temperatura_c:.0f}°C")
        self.emoji_label.setText(self.pegar_clima_emoji(clima_id))
        self.descricao_label.setText(self.tradutor_clima_descricao(clima_descricao))

    @staticmethod
    def pegar_clima_emoji(clima_id):
        if 200 <= clima_id <= 232:
            return "⛈"
        elif 300 <= clima_id <= 321:
            return "🌦"
        elif 500 <= clima_id <= 531:
            return "🌧"
        elif 600 <= clima_id <= 622:
            return "❄"
        elif 701 <= clima_id <= 741:
            return "🌫"
        elif clima_id == 762:
            return "🌋"
        elif clima_id == 771:
            return "💨"
        elif clima_id == 781:
            return "🌪"
        elif clima_id == 800:
            return "☀"
        elif 801 <= clima_id <= 804:
            return "☁"
        else:
            return ""
    
    @staticmethod
    def tradutor_clima_descricao(clima_descricao):
        if clima_descricao == "thunderstorm with rain" or "thunderstorm with light rain" or "thunderstorm with heavy rain" or "light thunderstorm" or "thunderstorm" or "heavy thunderstorm" or "ragged thunderstorm" or "thunderstorm with light drizzle" or "thunderstorm with drizzle" or "thunderstorm with heavy drizzle":
            return "Tempestade"
        elif clima_descricao == "clear sky":
            return "Céu Limpo"
        elif clima_descricao == "broken clouds" or "few clouds" or "scattered clouds" or "overcast clouds":
            return "Nublado"
        elif clima_descricao == "light intensity drizzle" or "drizzle" or "heavy intensity drizzle" or "light intensity drizzle rain" or "drizzle rain" or "heavy intensity drizzle rain" or "	shower rain and drizzle" or "	heavy shower rain and drizzle" or "shower drizzle":
            return "Chuviscando"
        elif clima_descricao == "light rain" or "moderate rain" or "heavy intensity rain" or "very heavy rain" or "extreme rain" or "freezing rain" or "light intensity shower rain" or "shower rain" or "heavy intensity shower rain" or "ragged shower rain":
            return "Chovendo"
        elif clima_descricao == "light snow" or "snow" or "heavy snow" or "sleet" or "	light shower sleet" or "shower sleet" or "light rain and snow" or "rain and snow" or "	light shower snow" or "shower snow" or "heavy shower snow":
            return "Nevando"
        else:
            return "Qualquer Clima"
 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clima_app = ClimaApp()
    clima_app.show()
    sys.exit(app.exec_())