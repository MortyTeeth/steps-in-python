from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        self.args = args
        self.seq = []
        for i in self.args:
            if isinstance(i, int):
                self.seq.append(i)
            elif isinstance(i, str):
                split = i.split('-')
                new_seq = [e for e in range(int(split[0]), int(split[-1]) + 1)]
                self.seq.extend(new_seq)

    def __getitem__(self, item):
        return self.seq[item]

    def __len__(self):
        return len(self.seq)

    def __iter__(self):
        return iter(self.seq)
