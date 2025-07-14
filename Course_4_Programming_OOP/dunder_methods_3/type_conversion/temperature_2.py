class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def __str__(self):
        return f"{round(self.temperature, 2)}°C"

    def to_fahrenheit(self):
        return self.temperature / (5 / 9) + 32

    @staticmethod
    def from_fahrenheit(value):
        return Temperature((5 / 9) * (value - 32))

    def __int__(self):
        return int(float(self.temperature))

    def __float__(self):
        return float(self.temperature)

    def __bool__(self):
        return True if self.temperature > 0 else False
