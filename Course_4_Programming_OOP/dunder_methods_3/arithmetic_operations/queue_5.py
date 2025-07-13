class Queue:
    def __init__(self, *args):
        self.iterable = []
        for item in args:
            if isinstance(item, (list, tuple)):
                self.iterable.extend(item)
            else:
                self.iterable.append(item)

    def add(self, *others):
        for item in others:
            if isinstance(item, Queue):
                self.iterable.extend(item.iterable)
            elif isinstance(item, (list, tuple)):
                self.iterable.extend(item)
            else:
                self.iterable.append(item)
        return self

    def __repr__(self):
        packing = ' -> '.join([str(i) for i in self.iterable])
        return f"{packing}"

    def pop(self):
        if len(self.iterable) < 1:
            return None
        else:
            value = self.iterable.pop(0)
        return value

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.iterable == other.iterable

        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Queue):
            iterable = self.iterable + other.iterable
            packing = ' -> '.join([str(i) for i in iterable])
            return f"{packing}"
        return NotImplemented

    def __iadd__(self, *other):
        if isinstance(*other, str):
            return NotImplemented
        self.iterable += other
        return self

    def __rshift__(self, other):
        if isinstance(other, int):
            return Queue(self.iterable[other:])
        return NotImplemented
