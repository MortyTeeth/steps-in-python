from collections import defaultdict


def wins(pairs):
    result = defaultdict(set)
    for winner, loser in pairs:
        result[winner].add(loser)
    return result
