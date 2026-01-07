def pegar_emoji_clima(clima_id):
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
    elif clima_id == 800:
        return "☀"
    elif 801 <= clima_id <= 804:
        return "☁"
    else:
        return "❓"