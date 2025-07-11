class HourClock:
    def __init__(self, hours):
        if isinstance(hours, int) and 1 <= hours <= 12:
            self.hours = hours
        else:
            raise ValueError('Некорректное время')

    def get_hours(self):
        return self._hours

    def set_hours(self, new_hours):
        if isinstance(new_hours, int) and 1 <= new_hours <= 12:
            self._hours = new_hours
        else:
            raise ValueError('Некорректное время')

    hours = property(get_hours, set_hours)
