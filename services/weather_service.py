import requests


class WeatherService:
    API_KEY = "774686071ea9af2ccf4c1b847f41d411"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def buscar_clima(self, cidade):
        params = {
            "q": cidade,
            "appid": self.API_KEY
        }

        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()