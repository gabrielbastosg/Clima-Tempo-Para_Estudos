import requests
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout
)
from PyQt5.QtCore import Qt

from services.weather_service import WeatherService
from utils.weather_emoji import pegar_emoji_clima


class ClimaTempo(QWidget):
    def __init__(self):
        super().__init__()

        self.cidade_label = QLabel("Entre com o nome da cidade:")
        self.cidade_input = QLineEdit()
        self.btn_clima = QPushButton("Ver clima")
        self.temperatura_label = QLabel()
        self.emoji_label = QLabel()
        self.descricao_label = QLabel()

        self.service = WeatherService()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Clima Tempo")

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.cidade_label)
        vbox.addWidget(self.cidade_input)
        vbox.addWidget(self.btn_clima)
        vbox.addWidget(self.temperatura_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.descricao_label)

        for widget in [
            self.cidade_label,
            self.cidade_input,
            self.temperatura_label,
            self.emoji_label,
            self.descricao_label
        ]:
            widget.setAlignment(Qt.AlignCenter)

        self.btn_clima.clicked.connect(self.pegar_clima)
        self.aplicar_estilos()

    def aplicar_estilos(self):
        self.setStyleSheet("""
            QLabel,QPushButton{ font-family: calibri; }
            QLabel{ font-size: 40px; }
            QLineEdit{ font-size: 40px; }
            QPushButton{ font-size: 30px; font-weight: bold; }
        """)

    def pegar_clima(self):
        cidade = self.cidade_input.text()

        try:
            data = self.service.buscar_clima(cidade)
            self.mostrar_clima(data)

        except Exception as erro:
            self.mostrar_erro(str(erro))

    def mostrar_clima(self, data):
        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.15
        clima_id = data["weather"][0]["id"]
        descricao = data["weather"][0]["description"]

        self.temperatura_label.setText(f"{temp_c:.2f}°C")
        self.emoji_label.setText(pegar_emoji_clima(clima_id))
        self.descricao_label.setText(descricao)

    def mostrar_erro(self, mensagem):
        self.temperatura_label.setText(mensagem)
        self.emoji_label.clear()
        self.descricao_label.clear()