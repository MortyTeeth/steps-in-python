from collections.abc import Sequence

dictionary = {"A": ('A', 'T'), "G": ('G', 'C'), "T": ('T', 'A'), "C": ('C', 'G')}


class DNA(Sequence):
    def __init__(self, chain):
        self.chain = chain
        self.new_chain = []
        for value in self.chain:
            if value in dictionary:
                self.new_chain.append(dictionary[value])

    def __str__(self):
        return f"{self.chain}"

    def __len__(self):
        return len(self.new_chain)

    def __iter__(self):
        return iter(self.new_chain)

    def __getitem__(self, item):
        return self.new_chain[item]

    def __add__(self, other):
        if isinstance(other, list):
            return NotImplemented
        return DNA(self.chain + other.chain)

    def __eq__(self, other):
        if not isinstance(other, DNA):
            return NotImplemented
        return self.chain == other.chain

    def __contains__(self, item):
        return item in self.chain
