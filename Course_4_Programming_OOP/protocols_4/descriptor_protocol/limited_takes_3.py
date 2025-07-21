class MaxCallsException(Exception):
    pass


class LimitedTakes:
    def __init__(self, times):
        self._times = times
        self.time = 0

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, job, owner):
        if job is None and self.time < self._times:
            self.time += 1
            return self
        elif self.name in job.__dict__ and self.time < self._times:
            self.time += 1
            return job.__dict__[self.name]
        elif self.time >= self._times:
            raise MaxCallsException("Превышено количество доступных обращений")
        else:
            raise AttributeError("Атрибут не найден")

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value
