from datetime import date


class WeatherWarning:
    def __init__(self):
        pass

    def rain(self):
        print("Ожидаются сильные дожди и ливни с грозой")

    def snow(self):
        print("Ожидается снег и усиление ветра")

    def low_temperature(self):
        print("Ожидается сильное понижение температуры")


class WeatherWarningWithDate(WeatherWarning):
    def __init__(self):
        super().__init__()

    def rain(self, date=None):
        print(date.strftime('%d.%m.%Y'))
        print("Ожидаются сильные дожди и ливни с грозой")

    def snow(self, date=None):
        print(date.strftime('%d.%m.%Y'))
        print("Ожидается снег и усиление ветра")

    def low_temperature(self, date=None):
        print(date.strftime('%d.%m.%Y'))
        print("Ожидается сильное понижение температуры")