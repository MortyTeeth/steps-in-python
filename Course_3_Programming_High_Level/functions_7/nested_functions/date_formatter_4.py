from datetime import datetime
from datetime import date

loc = {
    'ru': '%d.%m.%Y',
    'us': '%m-%d-%Y',
    'ca': '%Y-%m-%d',
    'br': '%d/%m/%Y',
    'fr': '%d.%m.%Y',
    'pt': '%d-%m-%Y'
}


def date_formatter(country_code):
    def today(data):
        return datetime.strftime(data, loc[country_code])

    return today
