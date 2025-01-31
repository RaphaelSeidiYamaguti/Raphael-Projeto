#d9bc7b20371d46ff030518d3e40ebda6 api key
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                            QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class ClimaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.cidade_label = QLabel("Entre com o nome da cidade: \n(Digite o nome da cidade em Inglês)", self)
        self.cidade_input = QLineEdit(self)
        self.botao = QPushButton("Buscar o Clima", self)
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
            self.mostrar_erros("Too Many Redirects\n Cheque a URL")
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
        if clima_descricao == "thunderstorm with rain":
            return "Tempestade com chuva"
        elif clima_descricao == "thunderstorm with light rain":
            return "Tempestade com chuva leve"
        elif clima_descricao == "thunderstorm with heavy rain":
            return "Tempestade com chuva pesada"
        elif clima_descricao == "light thunderstorm":
            return "Tempestade Leve"
        elif clima_descricao == "thunderstorm":
            return "Tempestade"
        elif clima_descricao == "heavy thunderstorm":
            return "Tempestade Pesada"
        elif clima_descricao == "ragged thunderstorm":
            return "Tempestade Irregular"
        elif clima_descricao == "thunderstorm with light drizzle":
            return "Trovoada com leve garoa"
        elif clima_descricao == "thunderstorm with drizzle":
            return "Trovoada com garoa"
        elif clima_descricao == "thunderstorm with heavy drizzle":
            return "Trovoada com forte garoa"
        elif clima_descricao == "clear sky":
            return "Céu Limpo"
        elif clima_descricao == "few clouds":
            return "Poucas Nuvens"
        elif clima_descricao == "broken clouds":
            return "Nuvens Quebradas"
        elif clima_descricao == "scattered clouds":
            return "nuvens dispersas"
        elif clima_descricao == "overcast clouds":
            return "Nuvens nubladas"
        elif clima_descricao == "light intensity drizzle":
            return "Chuvisco de baixa intensidade"
        elif clima_descricao == "heavy intensity drizzle":
            return "Chuvisco de alta intensidade"
        elif clima_descricao == "light intensity drizzle rain":
            return "Chuva de chuvisco de baixa intensidade"
        elif clima_descricao == "drizzle rain":
            return "Chuva de chuvisco"
        elif clima_descricao == "heavy intensity drizzle rain":
            return "Chuva de chuvisco de alta intensidade"
        elif clima_descricao == "shower rain and drizzle":
            return "Pancada de chuva e chuvisco"
        elif clima_descricao == "heavy shower rain and drizzle":
            return "Pancada de chuva forte e chuvisco"
        elif clima_descricao == "shower drizzle":
            return "Pancada de chuvisco"
        elif clima_descricao == "light rain":
            return "Chuva leve"
        elif clima_descricao == "moderate rain":
            return "Chuva moderada"
        elif clima_descricao == "heavy intensity rain":
            return "Chuva forte"
        elif clima_descricao == "very heavy rain":
            return "Chuva muito forte"
        elif clima_descricao == "extreme rain":
            return "Chuva extrema"
        elif clima_descricao == "freezing rain":
            return "Chuva congelante"
        elif clima_descricao == "light intensity shower rain":
            return "Pancada de chuva fraca"
        elif clima_descricao == "shower rain":
            return "Pancada de chuva"
        elif clima_descricao == "heavy intensity shower rain":
            return "Pancada de chuva intensa"
        elif clima_descricao == "ragged shower rain":
            return "Pancada de chuva irregular"
        elif clima_descricao == "light snow":
            return "Neve leve"
        elif clima_descricao == "snow":
            return "Neve"
        elif clima_descricao == "heavy snow":
            return "Neve intensa"
        elif clima_descricao == "sleet":
            return "Chuva misturada com neve"
        elif clima_descricao == "light shower sleet":
            return "Pancada leve de chuva e neve"
        elif clima_descricao == "shower sleet":
            return "Pancada de chuva e neve"
        elif clima_descricao == "light rain and snow":
            return "Chuva leve e neve"
        elif clima_descricao == "rain and snow":
            return "Chuva e neve"
        elif clima_descricao == "light shower snow":
            return "Pancada leve de neve"
        elif clima_descricao == "shower snow":
            return "Pancada de neve"
        elif clima_descricao == "heavy shower snow":
            return "Pancada intensa de neve"
        elif clima_descricao == "mist":
            return "Névoa"
        elif clima_descricao == "smoke":
            return "Fumaça"
        elif clima_descricao == "haze":
            return "Neblina"
        elif clima_descricao == "sand/dust whirls":
            return "Redemoinhos de areia/poeira"
        elif clima_descricao == "fog":
            return "Nevoeiro"
        elif clima_descricao == "sand":
            return "Areia"
        elif clima_descricao == "dust":
            return "Poeira"
        elif clima_descricao == "volcanic ash":
            return "Cinza vulcânica"
        elif clima_descricao == "squalls":
            return "Rajadas de vento"
        elif clima_descricao == "tornado":
            return "Tornado"
        else:
            return "Esse Clima não foi identificado"
 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clima_app = ClimaApp()
    clima_app.show()
    sys.exit(app.exec_())