from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version):
        parts = version.split('.')
        while len(parts) < 3:
            parts.append('0')
        self.parts = tuple(map(int, parts[:3]))

    def __str__(self):
        return '.'.join(map(str, self.parts))

    def __repr__(self):
        return f"Version('{self}')"

    def __eq__(self, other):
        if isinstance(other, Version):
            return self.parts == other.parts
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return self.parts < other.parts
        return NotImplemented