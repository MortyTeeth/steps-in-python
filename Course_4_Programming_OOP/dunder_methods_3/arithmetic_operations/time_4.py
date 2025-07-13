class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        while self.hours >= 24:
            self.hours = self.hours - 24

        while self.minutes >= 60:
            self.hours += 1
            self.minutes -= 60

    def __str__(self):
        if len(str(self.minutes)) == 1 and len(str(self.hours)) == 1:
            return f"0{self.hours}:0{self.minutes}"
        elif len(str(self.minutes)) == 1:
            return f"{self.hours}:0{self.minutes}"
        elif len(str(self.hours)) == 1:
            return f"0{self.hours}:{self.minutes}"
        else:
            return f"{self.hours}:{self.minutes}"

    def __add__(self, other):
        if isinstance(other, Time):
            this_time = Time(self.hours + other.hours, self.minutes + other.minutes)
            while this_time.hours >= 24:
                self.hours -= 24
            return this_time
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Time):
            return Time(other.hours + self.hours, other.minutes + self.minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours += other.hours
            self.minutes += other.minutes
            while self.hours >= 24:
                self.hours -= 24
            while self.minutes >= 60:
                self.hours += 1
                self.minutes -= 60
            return self
        return NotImplemented
