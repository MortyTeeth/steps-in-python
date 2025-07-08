from itertools import permutations


def permutations_s(string):
    for perm in sorted(set(permutations(string))):
        print(''.join(perm))


permutations_s(input())
