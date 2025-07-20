from time import perf_counter


class AdvancedTimer:
    def __init__(self):
        self.runs = []

    def __enter__(self):
        self._start = perf_counter()
        return self._start

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._end = perf_counter() - self._start
        self.runs.append(self._end)

    @property
    def min(self):
        return min(self.runs) if self.runs else None

    @property
    def max(self):
        return max(self.runs) if self.runs else None

    @property
    def last_run(self):
        return self.runs[-1] if self.runs else None
