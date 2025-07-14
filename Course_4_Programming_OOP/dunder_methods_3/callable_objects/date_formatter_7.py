from datetime import date


class DateFormatter:
    def __init__(self, country_code):
        self.country_code = country_code
        self.data = {
            'ru': '%d.%m.%Y',
            'us': '%m-%d-%Y',
            'ca': '%Y-%m-%d',
            'br': '%d/%m/%Y',
            'fr': '%d.%m.%Y',
            'pt': '%d-%m-%Y'
        }

    def __call__(self, d):
        return d.strftime(self.data[self.country_code])
